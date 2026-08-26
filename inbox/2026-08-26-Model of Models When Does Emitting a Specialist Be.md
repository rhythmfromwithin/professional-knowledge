---
title: "Model of Models: When Does Emitting a Specialist Beat Attending, Adapting, or Tuning?"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2608.21386
priority: high
status: unread
interest: medium
next_step: skim
---
# Model of Models: When Does Emitting a Specialist Beat Attending, Adapting, or Tuning?
> 原文: [https://arxiv.org/abs/2608.21386](https://arxiv.org/abs/2608.21386)

arXiv:2608.21386v1 Announce Type: new
Abstract: Given a task described by a few examples, how should a model be specialized to it? Four mechanisms are available -- zero-shot, in-context attention, test-time gradient adaptation, and emitting specialist weights from a hypernetwork -- yet the operating regime of the last is rarely mapped. We run the identical four-way comparison across six tasks spanning regression, generation, language modeling, reinforcement learning, and clinical and genomic classification, holding the specialist, the context, and (where we can) the training budget fixed. The clearest wins for emission are about cost at matched quality: it ties the state-of-the-art amortized tabular model (TabPFN) on clinical few-shot classification while emitting a reusable specialist instead of re-attending the support set per query, and reaches noise-floor shape generation with a $132$-float per-instance program. On few-shot sinusoid regression it is $2$--$3$ orders of magnitude below MAML at zero test-time gradient steps -- a margin that narrows to $\sim$$30\times$ but persists once training budgets are equalized. Emission cannot match in-context attention on high-dimensional sequence modeling: under matched-budget pre-training a one-pass adapter recovers only a minority of the in-context gain ($14.0\pm0.9\%$ at $5$M, $11.2\pm0.5\%$ at $15$M), and a LoRA-rank sweep shows this shortfall is a partial capacity limit -- capture climbs from $5\%$ to $21\%$ as rank grows but plateaus far below full recovery. Mechanism ablations confirm the emitted specialist is genuinely task-conditioned, not a memorized prior; and, more speculatively, emitted specialists compose in weight space -- interpolating two of them tracks the corresponding blend of their functions. We close with a falsifiable thesis, operationalized through a per-task resolution measure, bounding when each conditioning mechanism should be preferred.
