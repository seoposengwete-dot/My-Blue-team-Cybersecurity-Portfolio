# Detection Test Results

## 1. Test Objective

The purpose of testing was to evaluate whether the suspicious login detection logic correctly identifies repeated failed authentication attempts.

The detection threshold is five or more failed logins from the same username and source IP address within a 10-minute window.

## 2. Test Environment

- Test environment 1: Programiz online Python compiler
- Test environment 2: Windows Command Prompt using a local GitHub clone
- Dataset: Simulated authentication events
- Detection logic: Python detection script
- Failed login event: Windows Event ID 4625
- Successful login event: Windows Event ID 4624
- Threshold: 5 failed attempts
- Time window: 10 minutes

The initial detection scenarios were tested using an embedded copy of the simulated dataset. Subsequent validation was performed using the committed GitHub detection script and the actual project CSV dataset.

## 3. Test Scenarios and Results

| Test | Scenario | Expected Result | Actual Result |
|---|---|---|---|
| A | Five failed logins within four minutes, followed by a successful login | Medium and High alerts | Passed |
| B | One normal successful login | No alert | Passed |
| C | Eight failed logins within seven minutes, with no success | Medium alert only | Passed |
| D | Five failed logins over exactly ten minutes | Medium alert | Passed |
| E | Five failed logins over ten minutes and one second | No alert | Passed |

All five controlled detection scenarios passed in the Programiz test environment.

## 4. Direct Git Clone-and-Run Validation

The published GitHub repository was cloned to a local Windows environment.

The committed detection script was executed against the actual project CSV dataset.

**Observed results:**

| Measurement | Result |
|---|---:|
| Detection windows found | 3 |
| Medium alerts | 3 |
| High alerts | 1 |
| Total alerts | 4 |

The local CSV dataset was compared against the committed GitHub version using the Windows FC file comparison command.

Result: No differences encountered.

The detection script produced the expected baseline results.

The Git working tree was also checked after removing temporary validation files. No uncommitted changes remained.

## 5. Findings

The tests demonstrated that the detection logic:

- Identifies repeated failed logins.
- Applies the five-attempt threshold.
- Includes failures occurring exactly at the ten-minute boundary.
- Excludes attempts outside the ten-minute window.
- Identifies a successful login occurring after the fifth failed attempt.
- Avoids repeated alerts for overlapping detection windows.
- Executes successfully against the committed project CSV dataset.

## 6. Limitations

- The dataset contains simulated authentication events.
- Testing was not conducted against live Windows security logs.
- The detection script has been validated locally but has not been integrated into a live SIEM environment.
- A detection alert indicates suspicious activity and does not independently prove account compromise.

## 7. Conclusion

All five controlled detection scenarios passed in the initial testing environment.

The committed GitHub detection script was subsequently cloned and executed locally against the original project CSV dataset.

The results matched the expected baseline of three detection windows, three medium alerts and one high alert.

The project successfully passed local clone-and-run validation. Further development could include testing against real Windows security event data in an appropriately controlled environment.
