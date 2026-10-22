---
title: "Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.29669
priority: low
status: unread
interest: medium
next_step: skim
---
# Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement
> 原文: [https://arxiv.org/abs/2610.29669](https://arxiv.org/abs/2610.29669)

arXiv:2610.29669v1 Announce Type: new
Abstract: LLM-generated records increasingly populate production information systems where they are treated as data assets subject to the same quality expectations as records from operational databases. A single such record can simultaneously satisfy and violate a quality rule: a grounded fact adjacent to a hallucination, a useful answer adjacent to a stereotype. Classical data cleaning cannot resolve this because the two judgments are incompatible over the same span; a single LLM judge cannot either, since it shares the training biases that produced the conflict. Existing interventions such as prompt engineering, chain-of-thought, and RLHF reduce surface error rates but provide no audit trail and cannot distinguish genuine remediation from blanket suppression. The question is whether a deterministic check over structured inter-agent records can catch the defects that referential checks alone miss. We present BiasGuard-D: two adversarial roles drawn from distinct model families exchange typed claim documents, a three-model quorum adjudicates by majority vote, and a combined referential-plus-semantic invariant validates the verdict. The semantic component fires on verdicts referential checks miss; removing the iterative loop drops invariant satisfaction sharply. The deliberation layer transfers from stereotype to hallucination remediation on HaluEval QA with only role-framing changes, raising right-answer recovery by 49 percentage points; the triage gate required a cross-family second auditor to maintain recall on objective hallucination. Every claim, vote, and instruction is stored as a typed record giving operators a provenance trail auditable under emerging AI regulations.
