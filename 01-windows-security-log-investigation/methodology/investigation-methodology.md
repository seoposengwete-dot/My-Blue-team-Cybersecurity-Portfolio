# Windows Security Log Investigation Methodology

## 1. Objective

Document a repeatable process for reviewing Windows Security events, identifying authentication activity, and recording evidence-based findings.

## 2. Tools Used

- Windows Event Viewer
- Windows Security event logs
- GitHub for documenting the investigation
- CSV files for organising event details

## 3. Investigation Procedure

### Step 1: Locate Security Events

Open Event Viewer and navigate to:

`Windows Logs → Security`

Review the available Security events for the relevant investigation period.

### Step 2: Identify Relevant Event IDs

Focus on these authentication events:

- **4624:** An account successfully logged on.
- **4625:** An account failed to log on.

These events provide useful context but must be interpreted alongside their details and surrounding activity.

### Step 3: Record Event Details

For each relevant event, record the available:

- Event ID
- Date and time
- Logon type
- Account information
- Source network address
- Process name and process ID, where available
- Status and substatus codes, where available

Do not assume that missing fields indicate malicious activity.

### Step 4: Compare Events

Compare timestamps, account information, logon types, process details, and source addresses.

Events occurring close together in time are not automatically related. Look for supporting evidence before establishing a connection.

### Step 5: Assess the Findings

Classify findings according to the available evidence.

Possible outcomes include:

- **Benign:** Evidence supports an ordinary activity explanation.
- **Suspicious:** Evidence warrants further investigation.
- **Inconclusive:** Available evidence is insufficient to determine what happened.

Avoid declaring an incident confirmed without sufficient evidence.

### Step 6: Document and Preserve Evidence

Record the observations, investigation scope, limitations, and recommended follow-up actions.

Where possible, preserve the original event details or export the relevant events for independent review. Protect sensitive information before publishing evidence.

### Step 7: Develop Detection Opportunities

Look for repeatable patterns, such as multiple failed logons within a defined time window.

Document the detection condition, data fields required, limitations, and test results. Validate detection logic against suitable test data before using it operationally.

## 4. Investigation Limitations

A limited review of selected events cannot establish the complete security state of a computer. Findings depend on the available logs, audit settings, investigation period, and accuracy of recorded evidence.

## 5. Quality Principles

- Record facts separately from assumptions.
- Use timestamps consistently.
- Verify status codes before interpreting them.
- Do not claim causation from timing alone.
- Document missing evidence and uncertainty.
- Keep reports and datasets consistent with the underlying records.

## 6. Project Status

This methodology was applied to the initial WIN-001 training investigation. The initial review remains inconclusive, and additional evidence would be needed for stronger conclusions.
