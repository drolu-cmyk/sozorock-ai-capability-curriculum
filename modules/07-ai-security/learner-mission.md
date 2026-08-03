# M07 learner mission: AI Cybersecurity

## Mission

Practice how to identify AI-specific attack surfaces. Practice how to map threats to a recognized vocabulary. Practice how to run bounded security tests with synthetic inputs. Practice how to recommend mitigations and document residual risk.

## Time and prerequisites

- Time: 180 minutes
- Prerequisite: M06
- Work in the approved lab workspace.
- Use public, synthetic, or approved de-identified data only.

## Safety first

Do not test an unauthorized system, scan, exploit, exfiltrate, or disrupt anything external. Do not place secrets, credentials, personal information, protected health information, or confidential client material in the lab or portfolio. Stop before any irreversible action and ask for human approval.

## Steps

1. Draw the system boundary for your M05 or M06 workflow: user, model, data, retrieval, tools, outputs, and logs.
2. Identify at least five threats, including prompt injection, sensitive-information disclosure, insecure output handling, excessive agency, and supply-chain or source risk.
3. Map each threat to OWASP LLM or MITRE ATLAS terminology using the current reference register.
4. Create safe test prompts that use fictional or synthetic content only. Do not scan, exploit, exfiltrate, or disrupt any external system.
5. Run the tests in the approved lab and record expected behavior, actual behavior, evidence, severity, and confidence.
6. Propose one preventive, one detective, and one corrective control for the most important threat.
7. Record residual risk, owner, and next test date.
8. Submit the threat model, safe attack log, mitigation plan, and residual-risk note.

## Required submission

Submit:

- threat-model and safe-attack-log
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
