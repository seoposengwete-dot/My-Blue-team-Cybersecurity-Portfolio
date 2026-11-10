
import csv
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# Detection configuration
THRESHOLD = 5
WINDOW_MINUTES = 10
SUCCESS_CORRELATION_MINUTES = 10

# Locate the project dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "data" / "sample-authentication-events.csv"

REQUIRED_COLUMNS = {
    "timestamp",
    "username",
    "source_ip",
    "event_id"
}


def load_events():
    """Load and validate authentication events."""

    if not CSV_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {CSV_FILE}"
        )

    events_by_account = defaultdict(list)

    with CSV_FILE.open(
        "r", newline="", encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("CSV file is empty.")

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            raise ValueError(
                f"Missing CSV columns: {', '.join(sorted(missing_columns))}"
            )

        for row_number, row in enumerate(reader, start=2):
            try:
                row["time"] = datetime.strptime(
                    row["timestamp"],
                    "%Y-%m-%d %H:%M:%S"
                )
            except (ValueError, TypeError):
                print(
                    f"Skipping row {row_number}: invalid timestamp."
                )
                continue

            if not row["username"] or not row["source_ip"]:
                print(
                    f"Skipping row {row_number}: missing account or source IP."
                )
                continue

            key = (row["username"], row["source_ip"])
            events_by_account[key].append(row)

    return events_by_account


def analyse_events(events_by_account):
    """Detect repeated failed logins and subsequent successes."""

    detection_windows_found = 0
    medium_alerts = 0
    high_alerts = 0

    print("\nSUSPICIOUS LOGIN ANALYSIS")
    print("=" * 40)

    for (username, source_ip), events in events_by_account.items():

        events.sort(key=lambda event: event["time"])

        failures = [
            event for event in events
            if event["event_id"] == "4625"
        ]

        successes = [
            event for event in events
            if event["event_id"] == "4624"
        ]

        previous_alert_end = None

        for start_index in range(len(failures)):

            window_start = failures[start_index]["time"]
            window_end = window_start + timedelta(
                minutes=WINDOW_MINUTES
            )

            window_failures = [
                event for event in failures
                if window_start <= event["time"] <= window_end
            ]

            if len(window_failures) < THRESHOLD:
                continue

            # Suppress overlapping detection windows
            if (
                previous_alert_end is not None
                and window_start <= previous_alert_end
            ):
                continue

            threshold_event = window_failures[THRESHOLD - 1]
            threshold_time = threshold_event["time"]

            correlation_end = threshold_time + timedelta(
                minutes=SUCCESS_CORRELATION_MINUTES
            )

            later_successes = [
                event for event in successes
                if threshold_time < event["time"] <= correlation_end
            ]

            print("\n[MEDIUM ALERT] Repeated failed logins")
            print("Username:", username)
            print("Source IP:", source_ip)
            print("Failures in window:", len(window_failures))
            print("Window start:", window_start)
            print("Window end:", window_end)

            detection_windows_found += 1
            medium_alerts += 1

            if later_successes:
                first_success = later_successes[0]
                high_alerts += 1

                print(
                    "\n[HIGH ALERT] Successful login after "
                    "repeated failures"
                )
                print("Username:", username)
                print("Source IP:", source_ip)
                print("Successful login:", first_success["time"])

            previous_alert_end = window_end

    print("\nANALYSIS SUMMARY")
    print("=" * 40)
    print("Detection windows found:", detection_windows_found)
    print("Medium alerts:", medium_alerts)
    print("High alerts:", high_alerts)

    return detection_windows_found, medium_alerts, high_alerts


def main():
    try:
        events = load_events()
        analyse_events(events)

    except (FileNotFoundError, ValueError, OSError) as error:
        print("\nERROR:", error)


if __name__ == "__main__":
    main()
