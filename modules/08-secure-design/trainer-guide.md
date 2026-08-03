# M08 trainer guide: Secure Design and Incident Response

## Purpose

Deliver a hands-on session in which learners produce security-control-plan and incident-playbook and can explain its evidence and limitations.

## Prepare

- Review the manifest, learner mission, rubric, debrief, and [safe lab setup](../../lab-kit/SAFE-LAB-SETUP.md).
- Prepare synthetic examples and a no-code or manual fallback.
- Confirm the approved workspace and access level.
- Verify that no learner needs secrets, personal data, or unauthorized external access.
- Have the learner evidence template available.

## Suggested delivery

| Segment | Time | Trainer action |
|---|---:|---|
| Frame | 10 min | State capability, boundary, evidence, and safety stop conditions. |
| Demonstrate | 20 min | Walk through a fictional prompt-injection incident. Show the difference between stopping the workflow, preserving safe evidence, notifying the owner, restoring a manual fallback, and improving the test set. |
| Build | 100 min | Coach from the checkpoints without completing the learner's artifact. |
| Review | 20 min | Inspect evidence against the rubric and capture safe failure cases. |
| Debrief | 10 min | Ask the questions in debrief.md and record friction. |

## Coaching prompts

- Which control prevents the event and which one detects it?
- What should be disabled first?
- What information can be shared without exposing a secret or personal data?

## Common failure modes

- Incident response begins with public disclosure of a secret.
- Controls have no owner, evidence, or test.
- Learner assumes recovery means deleting the evidence.

## Safety and escalation

Stop the exercise if a learner is about to use real sensitive data, disclose a secret, test an unauthorized system, access another person's account, or trigger an irreversible external action. Preserve only safe evidence and notify the trainer or owner through the approved private channel.

Do not ask learners to reveal hidden model reasoning. Ask for concise explanations, visible inputs and outputs, test evidence, assumptions, and decisions.

## Assessment

Use the rubric. A critical safety failure is a non-pass regardless of the numeric score. Give feedback using: evidence observed, capability demonstrated, risk or gap, one next action, and resubmission decision.
