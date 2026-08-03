# Mission 03 — Data, Retrieval, and Citations

## Mission goal

Create a small, approved knowledge set and test whether an AI workflow retrieves relevant information, cites it accurately, and handles missing or conflicting sources safely.

## Why this matters

An AI answer is not grounded merely because it sounds plausible. A trustworthy knowledge workflow needs source authority, permissions, freshness, retrieval tests, citations, and a process for correcting or withdrawing information.

## Time

180 minutes.

## You will produce

- A source register
- A knowledge map
- A retrieval test set
- A citation audit

## Safety boundary

Use three to five public or trainer-approved documents. Do not ingest personal, protected, confidential, or copyrighted material unless the trainer has confirmed permission and scope.

## Step 1 — Select the sources

Choose documents that answer a defined community, organizational, or public-information need.

For each source, record:

- Title
- Owner or publisher
- URL or location
- Publication date
- Last update date
- Scope
- Authority
- Permission
- Sensitivity
- Expected review date

Reject sources you cannot identify, access, or explain.

## Step 2 — Build the source register

Use the source register template. Mark each source:

- Approved
- Needs review
- Out of scope
- Withdrawn

Do not mix sources with different permissions without documenting the difference.

## Step 3 — Create the knowledge map

For each source, record:

- Topics covered
- Questions it should answer
- Questions it cannot answer
- Terms or labels users may use
- Known limitations
- Potential conflicts with another source

## Step 4 — Create the retrieval test set

Write at least six questions:

- Two directly supported questions
- One question requiring information from two sources
- One question where the answer is missing
- One question where sources conflict or have different dates
- One out-of-scope question

For each question, write the expected source and expected response behavior.

## Step 5 — Establish a baseline

Ask the same questions without connecting the approved knowledge set.

Record:

- Answer
- Confidence or uncertainty
- Whether a source was cited
- Whether the answer was supported

The baseline shows what the model may produce without grounding.

## Step 6 — Build the knowledge workflow

Using the approved lab environment:

1. Add only the approved sources.
2. Label each source clearly.
3. Require the system to answer only from the approved knowledge set.
4. Require citations or source identifiers.
5. Require the system to say when the answer is not found.
6. Set a human-review instruction for conflicting or high-impact information.

## Step 7 — Run the retrieval tests

Run all six questions. Record:

- Retrieved source
- Relevance
- Citation accuracy
- Completeness
- Freshness
- Unsupported claims
- Required human review

## Step 8 — Test knowledge boundaries

Test:

- A question with no answer in the source set
- A question using a synonym
- A question using an outdated term
- A question that combines two sources
- A question that attempts to make the system answer beyond its scope

Do not add a new source until you record why it is needed and whether it is approved.

## Step 9 — Complete the citation audit

For each answer, mark:

- Citation present
- Citation supports the claim
- Citation is the correct source
- Citation is current enough
- Citation is understandable to the user

## Step 10 — Define maintenance

Write:

- Who owns each source
- How often it is reviewed
- What triggers an update
- How a withdrawn source is removed
- How users report an incorrect answer
- What happens while a source is under review

## Submission checklist

Submit:

- Source register
- Knowledge map
- Six-question retrieval test set
- Baseline results
- Grounded results
- Citation audit
- Maintenance and withdrawal plan

## Extension challenge

Create a deliberately conflicting pair of safe documents with different dates. Design a response rule that identifies the conflict and routes the answer for human review instead of silently choosing one.
