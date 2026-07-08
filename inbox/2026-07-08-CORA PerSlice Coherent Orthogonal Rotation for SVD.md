---
interest: medium
link: https://arxiv.org/abs/2607.02576
next_step: skim
priority: medium
slack_ts: '1783481432.107839'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'CORA: Per-Slice Coherent Orthogonal Rotation for SVD-based Low-Rank Adaptation'
---
# CORA: Per-Slice Coherent Orthogonal Rotation for SVD-based Low-Rank Adaptation
> 原文: [https://arxiv.org/abs/2607.02576](https://arxiv.org/abs/2607.02576)

arXiv:2607.02576v1 Announce Type: new
Abstract: Parameter-Efficient Fine-Tuning (PEFT) commonly adapts pretrained weights through low-rank updates, and recent methods further exploit the singular value decomposition (SVD) of the base weight for initialization or subspace selection. However, these methods do not explicitly preserve the coupled geometry between the pretrained left and right singular bases. Motivated by recent minimum-perturbation theory, which shows that stable finetuning follows a coherent SVD rotation in which a single orthogonal $Q$ acts on both the left singular basis $U\_0$ and the right singular basis $V\_0$, we prove a per-slice analogue: each row slice of $W\_0$ can be adapted by a shared orthogonal rotation $Q\_i$ on its left basis $U\_i$ and right basis $V\_i$ together with a diagonal spectrum shift. We implement this form as CORA (Coherent Orthogonal Rotation Adaptation), which applies per-slice orthogonal rotations and a per-layer diagonal scale to the rank-$r$ SVD truncation of $W\_0$. CORA uses $\tfrac{1}{2}m(r{-}1)$ trainable parameters per linear layer, about $4{\times}$ fewer than LoRA at the same rank. CORA outperforms LoRA, DoRA, PiSSA, and MiLoRA on commonsense reasoning and code generation while using about $8{\times}$ fewer parameters.
