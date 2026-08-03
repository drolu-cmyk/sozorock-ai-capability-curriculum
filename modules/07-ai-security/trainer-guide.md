# M07 trainer guide: AI Cybersecurity

## Purpose

Deliver a hands-on session in which learners produce threat-model and safe-attack-log and can explain its evidence and limitations.

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
| Demonstrate | 20 min | Use a toy retrieval workflow with a fictional instruction hidden in a source. Demonstrate detection and containment without accessing a live website, account, or production service. |
| Build | 100 min | Coach from the checkpoints without completing the learner's artifact. |
| Review | 20 min | Inspect evidence against the rubric and capture safe failure cases. |
| Debrief | 10 min | Ask the questions in debrief.md and record friction. |

## Coaching prompts

- Where can untrusted instructions enter the system?
- What can the model do that the user cannot directly do?
- How can you prove the mitigation worked without testing a real target?

## Common failure modes

- Learner tests a real system without explicit authorization.
- Attack content includes real secrets or harmful payloads.
- Mitigation is a generic warning with no control, owner, or test.

## Safety and escalation

Stop the exercise if a learner is about to use real sensitive data, disclose a secret, test an unauthorized system, access another person's account, or trigger an irreversible external action. Preserve only safe evidence and notify the trainer or owner through the approved private channel.

Do not ask learners to reveal hidden model reasoning. Ask for concise explanations, visible inputs and outputs, test evidence, assumptions, and decisions.

## Assessment

Use the rubric. A critical safety failure is a non-pass regardless of the numeric score. Give feedback using: evidence observed, capability demonstrated, risk or gap, one next action, and resubmission decision.
