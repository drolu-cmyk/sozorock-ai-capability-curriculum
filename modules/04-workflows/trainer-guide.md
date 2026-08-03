# M04 trainer guide: Structured Workflows and Automation

## Purpose

Deliver a hands-on session in which learners produce workflow-specification and tested-evidence-log and can explain its evidence and limitations.

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
| Demonstrate | 20 min | Map a fictional service-request summary from intake to reviewed response. Pause at the approval gate and show how a missing source causes the workflow to stop instead of inventing an answer. |
| Build | 70 min | Coach from the checkpoints without completing the learner's artifact. |
| Review | 20 min | Inspect evidence against the rubric and capture safe failure cases. |
| Debrief | 10 min | Ask the questions in debrief.md and record friction. |

## Coaching prompts

- Which step is a transformation and which step is a human decision?
- What happens when the required input is missing?
- What is the least harmful failure mode?

## Common failure modes

- Workflow is only a prompt with no inputs, outputs, or stop conditions.
- Automation is allowed to send, delete, purchase, or change an external record.
- Learner tests only the happy path.

## Safety and escalation

Stop the exercise if a learner is about to use real sensitive data, disclose a secret, test an unauthorized system, access another person's account, or trigger an irreversible external action. Preserve only safe evidence and notify the trainer or owner through the approved private channel.

Do not ask learners to reveal hidden model reasoning. Ask for concise explanations, visible inputs and outputs, test evidence, assumptions, and decisions.

## Assessment

Use the rubric. A critical safety failure is a non-pass regardless of the numeric score. Give feedback using: evidence observed, capability demonstrated, risk or gap, one next action, and resubmission decision.
