# Investigation Methodology: Suspicious Login Pattern Analysis

## 1. Investigation Scope

The purpose of this investigation is to analyse simulated Windows authentication events and identify potentially suspicious login patterns.

The investigation focuses on repeated failed login attempts, successful logins following failures, and authentication activity that may require further investigation.

## 2. Data Preparation

The investigation uses a simulated authentication dataset stored in:

`data/sample-authentication-events.csv`

The dataset contains 15 fictional authentication events across three scenarios.

The following fields are examined:

- Timestamp
- Computer
- Username
- Source IP address
- Windows Event ID
- Event type
- Logon type
- Authentication status

## 3. Event Analysis

Windows Security Event IDs are used to distinguish authentication outcomes.

- Event ID 4624: Successful logon.
- Event ID 4625: Failed logon.

The investigation examines the frequency, timing and distribution of failed authentication attempts.

## 4. Event Correlation

Authentication events are correlated using:

- Username
- Source IP address
- Computer
- Timestamp

Particular attention is given to five or more failed login attempts involving the same account and source IP address within a 10-minute period.

The investigation also checks whether a successful authentication event occurs after the failed attempts.

## 5. Risk Assessment

Authentication patterns are assessed according to their frequency, timing and outcome.

The following patterns are investigated:

- Repeated failed logins followed by a successful login.
- Normal successful authentication without preceding failures.
- Repeated failed logins without a subsequent successful login.

Repeated failures may indicate suspicious activity, but do not independently establish malicious intent.

A successful login following repeated failures also requires further investigation before compromise can be confirmed.

## 6. Investigation Limitations

This investigation uses simulated authentication data rather than live Windows security logs.

The dataset does not establish the identity of the person behind a source IP address or prove that an account was compromised.

Additional evidence would be required for a real-world investigation.

## 7. Investigation Outcome

The findings from the authentication analysis will be documented in a separate investigation report.

Detection logic will subsequently be developed and tested against the simulated dataset.
