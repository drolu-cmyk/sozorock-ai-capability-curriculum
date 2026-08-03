# M08 learner mission: Secure Design and Incident Response

## Mission

Practice how to translate threats into layered controls. Practice how to design secure data, identity, logging, and output boundaries. Practice how to practice an AI incident response tabletop. Practice how to define recovery and improvement actions.

## Time and prerequisites

- Time: 180 minutes
- Prerequisite: M07
- Work in the approved lab workspace.
- Use public, synthetic, or approved de-identified data only.

## Safety first

Do not test an unauthorized system, scan, exploit, exfiltrate, or disrupt anything external. Do not place secrets, credentials, personal information, protected health information, or confidential client material in the lab or portfolio. Stop before any irreversible action and ask for human approval.

## Steps

1. Use your M07 threat model and select the three highest-priority risks.
2. Design controls for data minimization, source permissions, identity, secrets, output validation, logging, rate limits, human approval, and shutdown.
3. Assign an owner, evidence source, test method, and review frequency to each control.
4. Write an incident playbook for a fictional failure such as a leaked synthetic secret, unsafe output, compromised source, or unauthorized tool attempt.
5. Run a tabletop: detect, contain, triage, communicate, recover, and improve.
6. Test one control with a safe synthetic case and record the result.
7. Identify one control that is detective rather than preventive and explain why both are needed.
8. Submit the control plan, playbook, tabletop record, and control test.

## Required submission

Submit:

- security-control-plan and incident-playbook
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
