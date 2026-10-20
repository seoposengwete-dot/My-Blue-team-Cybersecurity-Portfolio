# Detection Rule Test Results: Repeated Failed Logons

## 1. Objective

Validate the documented detection rule using simulated authentication events.

The rule should trigger when five or more Event ID 4625 events from the same source address occur within a rolling 10-minute window.

## 2. Test Environment

- **Data type:** Simulated test data
- **Event ID:** 4625 — Failed logon
- **Threshold:** Five or more failures
- **Time window:** Rolling 10 minutes
- **Purpose:** Validate the rule's threshold and time-window logic

These tests do not represent a live detection system or prove that the rule has been deployed operationally.

## 3. Test Cases

### Test A — Threshold Reached

**Scenario:** Five failed logons from `192.0.2.25` between 09:00:00 and 09:04:40.

**Expected result:** Alert.

**Reason:** All five failures originate from the same source and occur within 10 minutes.

**Outcome:** Pass — the expected alert condition is met.

### Test B — Threshold Not Reached

**Scenario:** Four failed logons from `192.0.2.30` between 10:00 and 10:03.

**Expected result:** No alert.

**Reason:** Only four failures occur within the 10-minute window, below the threshold of five.

**Outcome:** Pass — the alert condition is not met.

### Test C — Events Span More Than 10 Minutes

**Scenario:** Five failed logons from `192.0.2.40` at 09:00, 09:03, 09:06, 09:09, and 09:12.

**Expected result:** No alert.

**Reason:** The five events span 12 minutes. No rolling 10-minute window contains all five events; at most four occur within such a window.

**Outcome:** Pass — the alert condition is not met.

## 4. Results Summary

| Test | Condition | Expected result | Result |
|---|---|---|---|
| A | Five failures within 10 minutes | Alert | Pass |
| B | Four failures within 10 minutes | No alert | Pass |
| C | Five failures spanning 12 minutes | No alert | Pass |

## 5. Limitations

- Tests use simulated data, not live security events.
- The rule's logic has been evaluated manually; no automated detection engine was executed.
- Missing source addresses and distributed attempts require additional detection logic.
- Real deployments should test event parsing, timestamp handling, deduplication, and rolling-window calculations.

## 6. Conclusion

All three scenarios meet their expected outcomes under the documented detection criteria. The manual tests support the logical design of the rule but do not establish operational effectiveness in a live monitoring environment.

**Status:** Manual logic validation completed. Automated and live-system testing remain outstanding.
