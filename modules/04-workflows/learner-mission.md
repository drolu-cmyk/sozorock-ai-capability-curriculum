# M04 learner mission: Structured Workflows and Automation

## Mission

Practice how to decompose a task into observable workflow steps. Practice how to define inputs, outputs, decisions, and approvals. Practice how to design a manual fallback and failure path. Practice how to test a workflow with incomplete and out-of-scope cases.

## Time and prerequisites

- Time: 150 minutes
- Prerequisite: M03
- Work in the approved lab workspace.
- Use public, synthetic, or approved de-identified data only.

## Safety first

Do not test an unauthorized system, scan, exploit, exfiltrate, or disrupt anything external. Do not place secrets, credentials, personal information, protected health information, or confidential client material in the lab or portfolio. Stop before any irreversible action and ask for human approval.

## Steps

1. Bring your M03 source or knowledge map and select one low-risk recurring task.
2. Write the trigger, user, input contract, source boundary, transformation steps, decision points, output contract, and completion condition.
3. Create a baseline by completing the task manually or with one simple AI interaction.
4. Build a bounded workflow using a no-code, low-code, code, or paper-and-pencil path.
5. Add a human approval gate before any consequential recommendation or external action.
6. Test five cases: normal, missing information, conflicting information, out-of-scope request, and a sensitive-data attempt.
7. Record results, time, cost estimate, failure behavior, fallback path, and the next improvement.
8. Submit the workflow specification, test log, approval boundary, and fallback plan.

## Required submission

Submit:

- workflow-specification and tested-evidence-log
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
