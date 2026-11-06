# Detection Test Results

## 1. Test Objective

The purpose of testing was to evaluate whether the suspicious login detection logic correctly identifies repeated failed authentication attempts.

The detection threshold is five or more failed logins from the same username and source IP address within a 10-minute window.

## 2. Test Environment

- Test environment: Isolated Python execution environment
- Source code: Committed GitHub detection script
- Dataset: Actual project CSV file containing 25 simulated authentication events
- Folder structure: Recreated to match the GitHub project
- Failed login event: Windows Event ID 4625
- Successful login event: Windows Event ID 4624
- Threshold: 5 failed attempts
- Time window: 10 minutes

The committed detection script and actual project CSV file were tested together in a recreated folder structure. No changes were made to the GitHub repository during testing.

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
- Detection windows found: 3
- Medium alerts: 3
- High alerts: 1

All five scenarios produced the expected results when the detection script was executed against the actual project CSV dataset.

## 5. Findings

The tests demonstrated that the detection logic:

- Identifies repeated failed logins.
- Applies the five-attempt threshold.
- Groups authentication events by username and source IP address.
- Includes failures occurring exactly at the ten-minute boundary.
- Excludes attempts outside the ten-minute window.
- Identifies a successful login occurring after the fifth failed attempt.

An additional dataset observation was that the `event_type` column contains both `Failed` and `Failure` labels for failed authentication events. The detection logic identifies failed events using Windows Event ID 4625.

## 6. Limitations

- The dataset contains simulated authentication events.
- Testing was conducted in an isolated Python environment, not against live Windows security logs.
- The folder structure was recreated for testing rather than performing a direct Git clone-and-run.
- A detection alert indicates suspicious activity and does not independently prove account compromise.

## 7. Conclusion

All five detection test scenarios passed.

The detection script successfully processed the actual 25-record project CSV dataset in the recreated folder structure.

The results demonstrate that the detection logic correctly applies the configured failed-login threshold and 10-minute detection window to the simulated authentication events.
