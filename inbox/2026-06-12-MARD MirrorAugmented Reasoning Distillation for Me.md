---
interest: medium
link: https://arxiv.org/abs/2606.12578
next_step: skim
priority: high
slack_ts: '1781239685.624819'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'MARD: Mirror-Augmented Reasoning Distillation for Mechanism-Level Drug-Drug
  Interaction Prediction'
---
# MARD: Mirror-Augmented Reasoning Distillation for Mechanism-Level Drug-Drug Interaction Prediction
> 原文: [https://arxiv.org/abs/2606.12578](https://arxiv.org/abs/2606.12578)

arXiv:2606.12578v1 Announce Type: new
Abstract: Mechanism-level drug-drug interaction (DDI) prediction requires identifying which enzyme or pharmacodynamic axis is implicated, in which direction, and with which evidence -- not merely whether two drugs interact. We introduce a reproducible mechanism-level DDI labelling and evaluation protocol with a structured 7-family/147-subtype taxonomy, leakage-safe cold-split protocols, and auditable reasoning metrics for evaluating pharmacological prediction beyond flat interaction classification. We propose a pipeline that produces a 7B reasoning MARD (Mirror-Augmented Reasoning Distillation), combining three training innovations: a single-token KL divergence on direction tag that ties the model's prediction, per-loss PRM-weighted DPO with programmatic hard negatives, and a leakage-safe mechanism-aware retrieval channel. Process-reward step labels are automatically verifiable against DrugBank-structured fields, requiring no human or LLM judges. On the April-2026 DrugBank release, our MARD-7B is the only system in a 32-system comparison whose accuracy survives drug-pair novelty, beating the best baseline by +13.9 pp and GPT-4o by +6.7 pp at ~1% of frontier API cost. Further analysis reveals an anti-memorisation signature where accuracy improves on rarely seen drugs, suggesting that gain comes from structured pharmacological reasoning rather than drug-frequency memorisation. We release corpus, DDI-PRM, retrieval index, and training code.
