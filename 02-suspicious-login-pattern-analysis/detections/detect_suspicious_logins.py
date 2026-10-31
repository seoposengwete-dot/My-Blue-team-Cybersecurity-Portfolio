
import csv
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

THRESHOLD = 5
WINDOW_MINUTES = 10

# Locate the dataset relative to this script.
PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "data" / "sample-authentication-events.csv"

events_by_account = defaultdict(list)

# Read and prepare the authentication events.
with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["time"] = datetime.strptime(
            row["timestamp"], "%Y-%m-%d %H:%M:%S"
        )

        key = (row["username"], row["source_ip"])
        events_by_account[key].append(row)

print("SUSPICIOUS LOGIN ANALYSIS")
print("=" * 40)

alerts_found = 0

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

        # Suppress duplicate alerts from overlapping windows.
        if (
            previous_alert_end is not None
            and window_start <= previous_alert_end
        ):
            continue

        threshold_event = window_failures[THRESHOLD - 1]
        threshold_time = threshold_event["time"]

        later_successes = [
            event for event in successes
            if event["time"] > threshold_time
        ]

        print("\n[MEDIUM ALERT] Repeated failed logins")
        print("Username:", username)
        print("Source IP:", source_ip)
        print("Failures in window:", len(window_failures))
        print("Window start:", window_start)
        print("Window end:", window_end)

        alerts_found += 1

        if later_successes:
            first_success = later_successes[0]

            print(
                "\n[HIGH ALERT] Successful login after "
                "repeated failures"
            )
            print("Username:", username)
            print("Source IP:", source_ip)
            print("Successful login:", first_success["time"])

        previous_alert_end = window_end

print("\nAnalysis complete.")
print("Detection windows found:", alerts_found)
