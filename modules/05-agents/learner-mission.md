# M05 learner mission: Agents Tools and Permissions

## Mission

Practice how to define an agent boundary and allowed task. Practice how to separate read, propose, approve, and execute permissions. Practice how to design stop conditions and audit evidence. Practice how to test ambiguous, conflicting, and unauthorized requests safely.

## Time and prerequisites

- Time: 150 minutes
- Prerequisite: M04
- Work in the approved lab workspace.
- Use public, synthetic, or approved de-identified data only.

## Safety first

Do not test an unauthorized system, scan, exploit, exfiltrate, or disrupt anything external. Do not place secrets, credentials, personal information, protected health information, or confidential client material in the lab or portfolio. Stop before any irreversible action and ask for human approval.

## Steps

1. Choose a low-risk task that can be simulated without connecting to email, finance, production, or personal accounts.
2. Define the agent goal, user, allowed task, prohibited task, data boundary, and accountable owner.
3. List every proposed tool or action and classify it as read, draft, recommend, approve, or execute.
4. Set least-privilege defaults: read-only where possible, no secrets, no unauthorized access, and human approval for side effects.
5. Create stop conditions for missing information, conflicting instructions, sensitive data, policy violations, and uncertain results.
6. Simulate five requests: allowed read, draft for review, ambiguous request, unauthorized request, and attempted external side effect.
7. Record the action, permission decision, approval result, log evidence, and residual risk.
8. Submit the action map, permission matrix, test log, and approval rules.

## Required submission

Submit:

- agent-action-map and permission test log
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
