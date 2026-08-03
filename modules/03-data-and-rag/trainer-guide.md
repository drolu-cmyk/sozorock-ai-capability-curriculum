# Trainer Guide — Mission 03

## Trainer objective

Teach learners that grounded AI depends on the quality, authority, permissions, freshness, and maintenance of its knowledge sources.

## Preparation checklist

- Prepare three to five public or approved documents on one topic.
- Confirm the source register and knowledge-map templates.
- Prepare one missing-answer question and one conflicting-source exercise.
- Confirm that all documents may be used in the lab.
- Verify the lab can preserve source identifiers without exposing private data.

## Suggested timing

- 15 minutes: explain grounding and source governance
- 20 minutes: demonstrate source registration
- 60 minutes: learner knowledge-set build
- 35 minutes: retrieval and citation testing
- 25 minutes: boundary and conflict exercise
- 25 minutes: debrief and assessment

## Demonstration guidance

Show one answer that sounds correct but lacks a supporting source. Then show an answer grounded in an approved document with a clear citation. Demonstrate that “I do not find that in the approved sources” is a successful result when the knowledge set does not contain the answer.

## Coaching prompts

- Who owns this source?
- How do you know it is authoritative?
- What is the source's update date?
- What questions should it not answer?
- What happens when two sources disagree?
- Can a user access the cited source?
- How will the knowledge set be updated or withdrawn?
- What is the risk of retrieving the wrong document?

## Common failure modes

### Source dumping

The learner adds many documents without recording scope, ownership, or permission. Require a source register before adding another document.

### Citation theater

A citation is present but does not support the claim. Ask the learner to trace each claim back to the source.

### Silent missing-answer behavior

Require an explicit not-found response and human-review route.

### Stale information

Ask the learner to compare publication dates and define a review interval.

### Permission blindness

Ask whether the user and the system are permitted to access and redistribute the source.

## Safety escalation

Pause the exercise if the learner attempts to ingest:

- Protected or confidential data
- Documents without permission
- Credentials or private system exports
- Materials from a system they do not own
- A source that could create a high-impact decision without human review

## Debrief questions

- Which source was most authoritative and why?
- Which source was hardest to use correctly?
- How did the system respond when the answer was missing?
- What would happen if a source changed tomorrow?
- Who should own the knowledge base in a real organization?
- What evidence would an auditor need?

## Assessment

Use the Module 03 rubric. A learner must preserve the source register, test missing and conflicting information, and complete the citation audit before proceeding.
