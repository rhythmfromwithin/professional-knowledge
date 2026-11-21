---
interest: medium
link: https://arxiv.org/abs/2611.25001
next_step: skim
priority: high
slack_ts: '1795243601.079599'
source: cs.LG - Machine Learning
status: unread
title: Density Feedback Control for Transferability of Generative Sparse Adversarial
  Attacks
---
# Density Feedback Control for Transferability of Generative Sparse Adversarial Attacks
> 原文: [https://arxiv.org/abs/2611.25001](https://arxiv.org/abs/2611.25001)

arXiv:2611.25001v1 Announce Type: new
Abstract: Generator-based sparse adversarial attacks train encoder--decoder networks to produce transferable sparse perturbations for black-box robustness evaluation. Their perturbation density, however, is set only indirectly by a fixed sparsity coefficient whose mapping to density is unknown and shifts during training, so reaching a target density requires re-tuning; this fixed pressure also yields little transferability gain once density reduction begins. We propose Density Feedback Control (DFC), which tightens or relaxes this coefficient at the end of each epoch according to the gap between the observed hard-mask density and the target, without changing the generator architecture or loss. At a 10\% target density, DFC brings the mean density of three base attacks within one percentage point of the target in a single run and improves the transfer attack success rate (ASR) of two of them on CNN and Transformer targets, including under per-image $\ell\_0$ budgets, while perturbing fewer pixels. Tracing GPG's training, we observe that as DFC relaxes the coefficient, the transfer ASR recovers with the density and overtakes the fixed-coefficient baseline with fewer pixels. For EGS-TSSA, which restricts perturbations to source-model feature-importance regions, DFC yields no consistent gain; we analyze how this restriction interacts with density feedback.
