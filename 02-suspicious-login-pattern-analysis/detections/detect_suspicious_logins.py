
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Detection settings
FAILED_LOGIN_THRESHOLD = 5
TIME_WINDOW_MINUTES = 10

# Locate the CSV dataset relative to this script
PROJECT_DIR = Path(__file__).resolve().parents[1]
CSV_FILE = PROJECT_DIR / "data" / "sample-authentication-events.csv"

# Store authentication events by username and source IP
events_by_user = defaultdict(list)

# Read the authentication dataset
with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        timestamp = datetime.strptime(
            row["timestamp"], "%Y-%m-%d %H:%M:%S"
        )

        key = (row["username"], row["source_ip"])

        events_by_user[key].append({
            "timestamp": timestamp,
            "event_id": row["event_id"]
        })

print("SUSPICIOUS LOGIN ANALYSIS")
print("=" * 40)

# Analyse each account and source IP combination
for (username, source_ip), events in events_by_user.items():

    events.sort(key=lambda event: event["timestamp"])

    failed_events = [
        event for event in events
        if event["event_id"] == "4625"
    ]

    successful_events = [
        event for event in events
        if event["event_id"] == "4624"
    ]

    threshold_time = None

    # Check for five failures within a rolling 10-minute window
    for index in range(
        FAILED_LOGIN_THRESHOLD - 1,
        len(failed_events)
    ):
        first_failure = failed_events[
            index - FAILED_LOGIN_THRESHOLD + 1
        ]["timestamp"]

        current_failure = failed_events[index]["timestamp"]

        elapsed = current_failure - first_failure

        if elapsed.total_seconds() <= TIME_WINDOW_MINUTES * 60:
            threshold_time = current_failure
            break

    # Generate repeated-failure alert
    if threshold_time is not None:
        print("\n[MEDIUM ALERT] Repeated failed logins")
        print(f"Username: {username}")
        print(f"Source IP: {source_ip}")
        print(f"Failed attempts: {len(failed_events)}")
        print(f"Threshold reached: {threshold_time}")

        # Check for a successful login after the threshold
        later_successes = [
            event for event in successful_events
            if event["timestamp"] > threshold_time
        ]

        if later_successes:
            print("\n[HIGH ALERT] Successful login after repeated failures")
            print(f"Username: {username}")
            print(f"Source IP: {source_ip}")
            print(f"Successful login: {later_successes[0]['timestamp']}")

print("\nAnalysis complete.")
