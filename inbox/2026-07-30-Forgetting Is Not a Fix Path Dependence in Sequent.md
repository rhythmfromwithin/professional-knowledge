---
interest: medium
link: https://arxiv.org/abs/2607.24805
next_step: skim
priority: low
slack_ts: '1785469004.492239'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'Forgetting Is Not a Fix: Path Dependence in Sequential Engram Editing'
---
# Forgetting Is Not a Fix: Path Dependence in Sequential Engram Editing
> 原文: [https://arxiv.org/abs/2607.24805](https://arxiv.org/abs/2607.24805)

arXiv:2607.24805v1 Announce Type: new
Abstract: AI Engram (Kwon et al., 2026) formalizes the four engram criteria of neuroscience as a constrained inverse problem in weight space and solves it closed-form: concept-specific memory traces become linear objects that can be extracted once and combined arithmetically. Appendix F states the Compositional Memory States Hypothesis: edited models live on "a commutative manifold where the integration of A and B reaches a consistent equilibrium regardless of the learning sequence." The evidence base is single and paired edits -- in materials terms, single-cycle tests, in which fatigue accumulation is structurally invisible. Whether the hypothesis holds under sequential load is exactly the "temporal dynamics" question the paper defers to future work. We run that test on the authors' own reference implementation, at their reported best edit strength (TOFU alpha=0.6, a choice favoring the linearity hypothesis), with pre-registered predictions, across three model charges (two vendors, two architecture families). Four findings replicate across all three: (1) zero-shot composition and sequential re-calibrated editing diverge by 61-71% of the edit magnitude; (2) cut order is not interchangeable, and the effect scales with concept overlap -- in one charge the order of cutting two Paris landmarks decides whether an uninvolved third concept survives; (3) the survivors' layer-input covariances -- the method's own sufficient statistics, read as strain gauges -- drift monotonically with every further cut, in every surviving concept, in every charge; (4) erased knowledge partially returns under subsequent unrelated cuts. Appendix F's commutative-manifold hypothesis is thereby falsified for sequential editing; the single-edit results of the original paper are untouched. For unlearning-as-compliance: erasure certified today does not certify the artifact after its next edit.
