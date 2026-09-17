---
title: "Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2609.17560
priority: high
status: unread
interest: medium
next_step: skim
---
# Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds
> 原文: [https://arxiv.org/abs/2609.17560](https://arxiv.org/abs/2609.17560)

arXiv:2609.17560v1 Announce Type: new
Abstract: Every production model is updated, by retraining, fine-tuning, quantization, or a silent vendor swap, and each update risks being worse than what it replaced. We formalize update promotion as certified paired risk-difference auditing. Our starting point is a support identity: the risk difference between two models lives on the inputs where they disagree, observable without labels. We build DISCERN, a sequential two-tier protocol. A zero-label tier certifies benign updates whose disagreement rate is below tolerance from unlabeled traffic alone. An audited tier labels only sampled disagreements through an anytime-valid confidence sequence, valid at every stopping time and under any label-routing rule, even an adversarial judge. We prove finite-sample validity and matching label-complexity bounds of order rho^2/eps^2 at the rate level, so exploiting free disagreement provably saves a factor 1/rho over any pairing-blind auditor, and the guarantee composes across an unbounded sequence of promotions from one error budget. Across 14,000+ replayed audit streams over 785 update pairs, including LoRA fine-tunes of language models up to 1.4B parameters, miscoverage is 0.0002 (nominal 5%), power 0.986 with zero false alarms, and 56% of benign updates certify with zero labels. Each audit emits a machine-checkable evidence record for post-market monitoring.
