# M00 trainer guide: Orientation and Safe Lab Practice

## Purpose

Deliver a hands-on session in which learners produce learner-agreement, baseline, and evidence-folder and can explain its evidence and limitations.

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
| Demonstrate | 20 min | Create a fictional request, show how to remove personal details, and demonstrate an evidence file that records the tool, date, input boundary, output, limitation, and human decision. |
| Build | 40 min | Coach from the checkpoints without completing the learner's artifact. |
| Review | 20 min | Inspect evidence against the rubric and capture safe failure cases. |
| Debrief | 10 min | Ask the questions in debrief.md and record friction. |

## Coaching prompts

- What would make this request unsafe or too high impact?
- What can be completed manually if the tool is unavailable?
- What evidence would let another person reproduce your baseline?

## Common failure modes

- Learner chooses a high-impact decision as the first lab.
- Learner treats a fluent output as proof of accuracy.
- Learner saves a secret or personal data in the portfolio.

## Safety and escalation

Stop the exercise if a learner is about to use real sensitive data, disclose a secret, test an unauthorized system, access another person's account, or trigger an irreversible external action. Preserve only safe evidence and notify the trainer or owner through the approved private channel.

Do not ask learners to reveal hidden model reasoning. Ask for concise explanations, visible inputs and outputs, test evidence, assumptions, and decisions.

## Assessment

Use the rubric. A critical safety failure is a non-pass regardless of the numeric score. Give feedback using: evidence observed, capability demonstrated, risk or gap, one next action, and resubmission decision.
