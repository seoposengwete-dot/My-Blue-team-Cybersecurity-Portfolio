# Detection Rule: Suspicious Login Patterns

## 1. Rule Name

Suspicious Login Pattern Detection

## 2. Detection Objective

Identify repeated failed Windows authentication attempts and detect successful logins that occur after repeated failures.

The objective is to identify potentially suspicious authentication activity that requires further investigation.

## 3. Relevant Windows Event IDs

- Event ID 4625: Failed logon.
- Event ID 4624: Successful logon.

## 4. Detection Conditions

### Alert A: Repeated Failed Logins

Generate an alert when:

- Five or more failed login attempts occur.
- The attempts involve the same username.
- The attempts originate from the same source IP address.
- The attempts occur within a rolling 10-minute window.

### Alert B: Successful Login Following Repeated Failures

Generate an additional alert when:

- The repeated failed-login threshold has been reached.
- A subsequent successful login occurs.
- The successful login involves the same username and source IP address.

## 5. Alert Severity

**Medium — Repeated Failed Logins**

Repeated authentication failures may indicate suspicious login activity and require investigation.

**High — Successful Login Following Repeated Failures**

A successful login following repeated failures increases the priority of the investigation but does not independently prove account compromise.

## 6. Expected Detection Results

| Scenario | Expected Result |
|---|---|
| Five failures followed by success | Both alerts |
| Normal successful login | No alert |
| Eight failures without success | Repeated failed-login alert |

## 7. False-Positive Considerations

Legitimate users may repeatedly enter incorrect passwords.

Automated services and incorrectly configured applications may also generate repeated authentication failures.

Alerts must therefore be investigated before malicious activity is concluded.

## 8. Detection Limitations

This rule uses simulated authentication events.

It does not independently establish the identity of the source, the intent behind the activity, or whether an account has been compromised.

Additional evidence is required during a real-world investigation.
