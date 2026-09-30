---
interest: medium
link: https://arxiv.org/abs/2609.31654
next_step: skim
priority: medium
slack_ts: '1790745136.174149'
source: cs.CV - Computer Vision
status: unread
title: Temporal-Attention Head Specialization During Video Diffusion Training
---
# Temporal-Attention Head Specialization During Video Diffusion Training
> 原文: [https://arxiv.org/abs/2609.31654](https://arxiv.org/abs/2609.31654)

arXiv:2609.31654v1 Announce Type: new
Abstract: Video diffusion transformers depend on temporal attention to coordinate information across frames, yet nearly everything known about this mechanism comes from analyzing trained models, so when and where temporal-attention structure forms during training remains poorly characterized. Population averages can also hide it, since a few specializing heads and a diffusing majority cancel in the mean. We therefore conduct a checkpoint-resolved census of every temporal-attention head across nine Open-Sora STDiT training runs spanning three model scales (306M to 1.03B parameters), scoring each head with an entropy-normalized measure of cross-frame attention concentration (CFAC) under a preregistered change-point and effect-size selection rule. The census reveals the sparse picture that averages obscure. Aggregate CFAC is flat or decreasing in every run, while a small minority of heads, roughly 4--13% in full-grid runs, develops pronounced concentration. Across seeds, the reproducible signal is positional but block-level. Selected heads repeatedly arise in the first temporal block, whereas individual head coordinates do not reproduce once block membership is accounted for. Among the analyzed 760M selected heads, attention maps converge to a small repertoire of local frame-routing motifs, self-frame diagonals and adjacent-frame bands, even when the responsible coordinates differ across runs. Correlation and ablation analyses do not establish a causal link to generated video quality, and we bound our claims accordingly. Beyond this STDiT family, the study contributes a transferable methodology. Checkpoint-resolved, per-head analysis under fixed selection rules can expose sparse temporal organization in other factorized video diffusion transformers and, with adapted routing metrics, in joint spatio-temporal architectures.
