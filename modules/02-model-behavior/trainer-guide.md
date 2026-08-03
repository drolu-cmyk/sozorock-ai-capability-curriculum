# Trainer Guide — Mission 02

## Trainer objective

Teach learners to treat model behavior as something to test and document, not something to assume.

## Preparation checklist

- Verify the approved lab workspace.
- Prepare the Module 01 example and five safe test cases.
- Prepare one baseline instruction and one improved instruction.
- Confirm that no sensitive data is available.
- Prepare a comparison worksheet.
- Confirm how learners will preserve outputs without exposing confidential material.

## Suggested timing

- 15 minutes: explain model behavior and test design
- 15 minutes: demonstrate baseline versus revised interaction
- 55 minutes: learner testing
- 25 minutes: failure analysis and version log
- 20 minutes: peer review
- 20 minutes: debrief and assessment

## Demonstration guidance

Use one ordinary example and one incomplete example. Show that a longer instruction is not automatically a better instruction. Demonstrate how explicit boundaries, output requirements, evidence requirements, and human-review rules improve the testable behavior.

Do not present one prompt as universally correct. The learner must connect the interaction design to the task, data, users, and risk.

## Coaching prompts

- What did you predict before running the test?
- Which test case exposed the limitation?
- What evidence would make this answer trustworthy?
- What should happen when information is missing?
- Which output requires human verification?
- Did the new instruction improve one case while harming another?
- What is the smallest useful change you can test next?

## Common failure modes

### Prompt accumulation

The learner keeps adding rules without testing which rule changed behavior. Ask them to change one variable at a time.

### Output judged by confidence

Ask the learner to compare the answer with the expected result and evidence, not with how persuasive it sounds.

### No out-of-scope boundary

Require the learner to define what the system should decline, flag, or route to a person.

### Hidden reasoning treated as evidence

Redirect the learner toward source citations, test records, assumptions, and concise explanations.

### One successful example

Require all five test cases before accepting the interaction design.

## Safety escalation

Pause the exercise if the learner tries to:

- Use real personal or protected data
- Connect the model to an unauthorized system
- Request an irreversible external action
- Treat an unverified output as final evidence
- Bypass an approval or access boundary

## Debrief questions

- Which failure would matter most in real work?
- Which metric should be added to the test set?
- What did the model not know?
- What should remain outside the model's authority?
- How will this interaction be monitored after deployment?

## Assessment

Use the Module 02 rubric. Learners should show baseline and revised behavior, preserve the test cases, document failure, and define a human-review boundary.
