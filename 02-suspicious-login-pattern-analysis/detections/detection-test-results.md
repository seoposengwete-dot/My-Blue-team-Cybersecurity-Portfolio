
# Detection Test Results

## 1. Test Objective

The purpose of testing was to evaluate whether the suspicious login detection logic correctly identifies repeated failed authentication attempts.

The detection threshold is five or more failed logins from the same username and source IP address within a 10-minute window.

## 2. Test Environment

- Test environment: Programiz online Python compiler
- Dataset: Simulated authentication events
- Detection logic: Python detection script
- Failed login event: Windows Event ID 4625
- Successful login event: Windows Event ID 4624
- Threshold: 5 failed attempts
- Time window: 10 minutes

The tests were performed using an embedded copy of the simulated dataset. The committed GitHub script was subsequently adapted to read the project CSV file directly.

## 3. Test Scenarios and Results

| Test | Scenario | Expected Result | Actual Result |
|---|---|---|---|
| A | Five failed logins within four minutes, followed by a successful login | Medium and High alerts | Passed |
| B | One normal successful login | No alert | Passed |
| C | Eight failed logins within seven minutes, with no success | Medium alert only | Passed |
| D | Five failed logins over exactly ten minutes | Medium alert | Passed |
| E | Five failed logins over ten minutes and one second | No alert | Passed |

## 4. Overall Results

- Total scenarios tested: 5
- Passed: 5
- Failed: 0

All five scenarios produced the expected results in the Programiz test environment.

## 5. Findings

The tests demonstrated that the detection logic:

- Identifies repeated failed logins.
- Applies the five-attempt threshold.
- Includes failures occurring exactly at the ten-minute boundary.
- Excludes attempts outside the ten-minute window.
- Identifies a successful login occurring after the fifth failed attempt.
- Avoids repeated alerts for overlapping detection windows.

## 6. Limitations

- The dataset contains simulated authentication events.
- The tests were conducted in Programiz, not against live Windows security logs.
- The committed GitHub version still requires execution against the project CSV file.
- A detection alert indicates suspicious activity and does not independently prove account compromise.

## 7. Conclusion

The five test scenarios passed in the Programiz environment.

Further validation is required by executing the committed detection script against the project's CSV dataset.
