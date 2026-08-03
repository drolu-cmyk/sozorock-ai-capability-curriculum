# Mission 02 — Model Behavior and Interaction Design

## Mission goal

Improve an AI interaction by testing how the model behaves, identifying failure patterns, and creating instructions that make the workflow more reliable and reviewable.

## Why this matters

AI systems can produce confident, incomplete, inconsistent, or unsupported outputs. Reliable work begins with a test set and an explicit definition of what good output looks like.

## Time

150 minutes.

## You will produce

- An interaction specification
- A five-case test set
- A prompt or instruction version log
- A behavior report

## Safety boundary

Use the approved lab workspace and safe test data only. Do not include secrets, personal information, protected information, or confidential material. Do not give the system permission to take external or irreversible actions.

## Step 1 — Bring forward the Module 01 task

Copy the AI task, user, intended output, success measures, and five test cases from Module 01.

If Module 01 is incomplete, use the provided public community-resource example.

## Step 2 — Write the baseline instruction

Write the shortest instruction that describes:

- The role of the system
- The task
- The input
- The desired output

Do not add every possible rule yet. This is your baseline.

## Step 3 — Predict the behavior

Before running the instruction, write what you expect for each test case.

Record:

- What the model should include
- What it should refuse or flag
- What evidence it should provide
- What it should do when information is missing

This prediction becomes part of your test evidence.

## Step 4 — Run the five cases

Run the same baseline instruction against:

- Normal case
- Incomplete case
- Ambiguous case
- Difficult case
- Unsafe or out-of-scope case

Save the outputs. Mark each result:

- Correct
- Partly correct
- Unsupported
- Unsafe
- Out of scope
- Requires human review

## Step 5 — Define the interaction specification

Add explicit requirements for:

- Task boundaries
- Required source or evidence
- Output structure
- Missing information
- Uncertainty
- Out-of-scope requests
- Human approval

Ask for concise justification or supporting evidence. Do not treat hidden model reasoning as an audit record.

## Step 6 — Run the same cases again

Do not change the test cases. Run the revised instruction and compare:

- What improved
- What became worse
- What remained unresolved
- Whether the new constraints created unnecessary friction

## Step 7 — Test failure deliberately

Use harmless, synthetic examples to test:

- Ambiguous wording
- Conflicting instructions
- Missing source information
- A request outside the system's purpose
- A request for an action that should require approval

Do not test against external systems or attempt to bypass safeguards.

## Step 8 — Create the version log

Record each change:

| Version | Change | Expected effect | Observed effect | Keep or revert |
|---|---|---|---|---|

Do not delete failed versions. Failed versions are evidence.

## Step 9 — Define the human boundary

Write:

- What the system may draft or suggest
- What a person must verify
- What a person must approve
- What the system must never do
- What happens when the system is uncertain

## Step 10 — Write the behavior report

Summarize:

- Strongest behavior
- Weakest behavior
- Most important failure
- Remaining uncertainty
- Recommended next step
- Conditions required before broader use

## Submission checklist

Submit:

- Interaction specification
- Five-case test set
- Baseline and revised outputs
- Version log
- Behavior report
- Human-oversight boundary

## Extension challenge

Compare two approved models or configurations using the same test set. Do not select a winner based on one impressive answer. Compare reliability, evidence quality, safety, latency, cost, and user effort.
