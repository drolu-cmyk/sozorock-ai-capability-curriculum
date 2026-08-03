# Release checklist

Use this checklist before merging a release to main or publishing a tag.

## Scope

- [ ] Version is updated in VERSION.
- [ ] CHANGELOG describes learner-visible changes.
- [ ] README current-status text matches the actual module state.
- [ ] Curriculum map matches manifests.

## Curriculum quality

- [ ] Every released module has learner mission, trainer guide, lab setup, evidence, rubric, debrief, extension, and safety review.
- [ ] A trainer has delivered the module.
- [ ] At least one learner has completed the module.
- [ ] Timing, prerequisites, and required tools are accurate.
- [ ] Core, build, and stretch paths are clearly separated.
- [ ] Rubric scores sum correctly and passing rules are explicit.

## Safety and privacy

- [ ] Labs use public, synthetic, or approved de-identified data.
- [ ] No secrets, personal information, protected health information, or learner submissions are present.
- [ ] No exercise authorizes testing an external system.
- [ ] Irreversible external actions are disabled or require a human approval gate.
- [ ] Incident and escalation instructions are visible.

## Standards and attribution

- [ ] Framework names, versions, and URLs are current.
- [ ] External sources are listed in docs/REFERENCE_REGISTER.md.
- [ ] Third-party material is attributed and redistributable.
- [ ] MIT and CC BY scopes remain clear.
- [ ] No certification or legal-compliance claim is implied.

## Repository quality

- [ ] Curriculum validation passes.
- [ ] Local-link validation passes.
- [ ] Markdown lint passes.
- [ ] Secret scan passes.
- [ ] Pull request has a focused description and review evidence.
- [ ] At least one maintainer reviews the release.
- [ ] Tag and release notes are prepared after merge.
