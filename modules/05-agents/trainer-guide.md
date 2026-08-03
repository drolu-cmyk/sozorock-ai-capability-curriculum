# M05 trainer guide: Agents Tools and Permissions

## Purpose

Deliver a hands-on session in which learners produce agent-action-map and permission test log and can explain its evidence and limitations.

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
| Demonstrate | 20 min | Use a fictional agent that drafts a public-resource response. Show that it may read approved synthetic data and draft text, but cannot publish, message, or change a record without human approval. |
| Build | 70 min | Coach from the checkpoints without completing the learner's artifact. |
| Review | 20 min | Inspect evidence against the rubric and capture safe failure cases. |
| Debrief | 10 min | Ask the questions in debrief.md and record friction. |

## Coaching prompts

- What is the smallest permission that enables the task?
- What evidence proves the agent stopped?
- Who is accountable when a human approves an agent proposal?

## Common failure modes

- Agent is described as autonomous without a permission model.
- Learner treats a tool call as harmless because it is technically possible.
- Logs contain a secret or a real personal record.

## Safety and escalation

Stop the exercise if a learner is about to use real sensitive data, disclose a secret, test an unauthorized system, access another person's account, or trigger an irreversible external action. Preserve only safe evidence and notify the trainer or owner through the approved private channel.

Do not ask learners to reveal hidden model reasoning. Ask for concise explanations, visible inputs and outputs, test evidence, assumptions, and decisions.

## Assessment

Use the rubric. A critical safety failure is a non-pass regardless of the numeric score. Give feedback using: evidence observed, capability demonstrated, risk or gap, one next action, and resubmission decision.
