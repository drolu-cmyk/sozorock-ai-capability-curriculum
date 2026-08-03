# M06 trainer guide: Evaluation and Monitoring

## Purpose

Deliver a hands-on session in which learners produce evaluation-report and monitoring-plan and can explain its evidence and limitations.

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
| Demonstrate | 20 min | Run a five-case miniature evaluation and show why one average score cannot hide a critical safety failure. Demonstrate a threshold that routes uncertain cases to human review. |
| Build | 100 min | Coach from the checkpoints without completing the learner's artifact. |
| Review | 20 min | Inspect evidence against the rubric and capture safe failure cases. |
| Debrief | 10 min | Ask the questions in debrief.md and record friction. |

## Coaching prompts

- What failure matters most to the user, not just to the model score?
- Which test case should become a permanent regression case?
- What evidence would cause you to pause the system?

## Common failure modes

- Learner reports an accuracy number with no test set or definition.
- Monitoring is defined as watching the tool without an owner or threshold.
- Hidden model reasoning is treated as an audit record.

## Safety and escalation

Stop the exercise if a learner is about to use real sensitive data, disclose a secret, test an unauthorized system, access another person's account, or trigger an irreversible external action. Preserve only safe evidence and notify the trainer or owner through the approved private channel.

Do not ask learners to reveal hidden model reasoning. Ask for concise explanations, visible inputs and outputs, test evidence, assumptions, and decisions.

## Assessment

Use the rubric. A critical safety failure is a non-pass regardless of the numeric score. Give feedback using: evidence observed, capability demonstrated, risk or gap, one next action, and resubmission decision.
