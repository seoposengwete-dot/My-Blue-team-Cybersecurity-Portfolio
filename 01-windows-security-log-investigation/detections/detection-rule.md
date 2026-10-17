# Detection Rule: Repeated Failed Logons

## 1. Objective

Detect repeated failed Windows logon attempts that may indicate password guessing or other suspicious authentication activity.

## 2. Detection Logic

Generate an alert when **5 or more failed logon events occur from the same source address within 10 minutes**.

## 3. Event Sources

- **Event ID 4625:** Failed logon
- **Event ID 4624:** Successful logon, used for additional investigation context

The alert condition is based on Event ID 4625. Event ID 4624 does not count toward the failure threshold.

## 4. Required Fields

Where available, collect:

- Event timestamp
- Event ID
- Source network address
- Account name
- Logon type
- Failure status and substatus

Events with missing source addresses require separate handling because they cannot reliably be grouped by source IP.

## 5. Example Test Scenario

The following is **simulated test data**, not evidence collected from the investigated Windows computer.

| Time | Event ID | Source IP |
|---|---:|---|
| 09:00:00 | 4625 | 192.0.2.25 |
| 09:01:00 | 4625 | 192.0.2.25 |
| 09:02:00 | 4625 | 192.0.2.25 |
| 09:03:00 | 4625 | 192.0.2.25 |
| 09:04:40 | 4625 | 192.0.2.25 |

**Expected result:** The rule triggers because five failed logons from the same source occur within 10 minutes.

## 6. Limitations

- Repeated failures can result from legitimate mistakes or misconfigured services.
- A source address may be missing or may not identify the original device.
- Distributed attempts from multiple addresses may not meet this threshold.
- This document defines detection logic; it does not claim that an alert has been deployed or tested in a live monitoring system.

## 7. Recommended Analyst Response

1. Review the affected account and surrounding authentication events.
2. Check whether the activity is expected.
3. Examine related source addresses and logon types.
4. Escalate according to the organisation's incident response procedure if suspicious activity is supported by evidence.

## 8. Status

Detection logic documented. Implementation and operational testing remain outstanding.
