# M06 learner mission: Evaluation and Monitoring

## Mission

Practice how to turn a use case into a measurable test plan. Practice how to define quality and safety thresholds. Practice how to classify failures and regression cases. Practice how to design monitoring, alerting, and rollback decisions.

## Time and prerequisites

- Time: 180 minutes
- Prerequisite: M05
- Work in the approved lab workspace.
- Use public, synthetic, or approved de-identified data only.

## Safety first

Do not test an unauthorized system, scan, exploit, exfiltrate, or disrupt anything external. Do not place secrets, credentials, personal information, protected health information, or confidential client material in the lab or portfolio. Stop before any irreversible action and ask for human approval.

## Steps

1. Select the workflow or agent from M04 or M05 and state the intended behavior.
2. Build a ten-case test set with normal, ambiguous, missing, conflicting, out-of-scope, and safe adversarial cases.
3. Define metrics such as task success, groundedness, citation quality, escalation quality, cost, and latency.
4. Set a target, minimum acceptable threshold, and decision rule for each metric.
5. Run the baseline and record outputs without rewriting results to make them look better.
6. Classify failures by cause: data, instruction, retrieval, tool, model, human process, or unknown.
7. Define what is monitored, who owns the signal, what triggers an alert, and when the workflow is disabled or rolled back.
8. Submit the evaluation report, test set, failure taxonomy, and monitoring plan.

## Required submission

Submit:

- evaluation-report and monitoring-plan
- the test cases and observed results
- the tool/model/version and date, if a tool was used
- the data and source boundary
- the limitation or residual risk
- the human-review or approval boundary

## Pathways

- Core: complete the task with the repository templates and a manual fallback.
- Build: use an approved low-code, API, or code implementation.
- Stretch: add a stronger evaluation, automation, or governance improvement without widening the safety boundary.

## Success check

You are finished when another person can understand what you built, reproduce the stated test, see where a human must decide, and identify what remains uncertain.
