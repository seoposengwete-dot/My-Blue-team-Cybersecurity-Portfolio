from datetime import datetime, timedelta
from collections import defaultdict

THRESHOLD = 5
WINDOW = timedelta(minutes=10)

tests = {
    "Test A - Five failures within 10 minutes": [
        ("09:00", "192.0.2.25"),
        ("09:01", "192.0.2.25"),
        ("09:02", "192.0.2.25"),
        ("09:03", "192.0.2.25"),
        ("09:04", "192.0.2.25"),
    ],
    "Test B - Four failures within 10 minutes": [
        ("10:00", "192.0.2.30"),
        ("10:01", "192.0.2.30"),
        ("10:02", "192.0.2.30"),
        ("10:03", "192.0.2.30"),
    ],
    "Test C - Five failures across 12 minutes": [
        ("09:00", "192.0.2.40"),
        ("09:03", "192.0.2.40"),
        ("09:06", "192.0.2.40"),
        ("09:09", "192.0.2.40"),
        ("09:12", "192.0.2.40"),
    ],
}

def should_alert(events):
    grouped = defaultdict(list)

    for time_text, source in events:
        timestamp = datetime.strptime(time_text, "%H:%M")
        grouped[source].append(timestamp)

    for timestamps in grouped.values():
        timestamps.sort()

        for start_time in timestamps:
            end_time = start_time + WINDOW
            count = sum(
                1 for timestamp in timestamps
                if start_time <= timestamp <= end_time
