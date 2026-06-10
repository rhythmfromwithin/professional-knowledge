---
interest: medium
link: https://arxiv.org/abs/2606.09850
next_step: skim
priority: high
slack_ts: '1781065410.051189'
source: cs.LG - Machine Learning
status: unread
title: Mechanistic Analysis of Alignment Algorithms in Language Models
---
# Mechanistic Analysis of Alignment Algorithms in Language Models
> 原文: [https://arxiv.org/abs/2606.09850](https://arxiv.org/abs/2606.09850)

arXiv:2606.09850v1 Announce Type: new
Abstract: Post-training alignment algorithms are predominantly evaluated as black boxes, obscuring how they reshape language models' internal computations. We present a systematic mechanistic analysis of six preference-optimization methods: PPO, DPO, SimPO, ORPO, GRPO, and KTO across three open-weight model families. By integrating layer-wise linear probing, Sparse Autoencoders, and crosscoders, we localize preference representations and quantify alignment-induced geometric transformations in latent space. We find that preference signals consistently concentrate in early--mid or mid--late layers, but different objectives induce qualitatively distinct representational shifts. KTO and GRPO enhance linear separability through constructive feature sharing and sparse, high-salience recruitment. In contrast, DPO and ORPO degrade separability via non-constructive geometric rotation and feature attenuation, while PPO and SimPO largely preserve baseline geometry. These transformations exhibit architecture-dependent variability, demonstrating that behavioral alignment does not imply uniform internal restructuring. Our findings establish alignment as a heterogeneous intervention, motivate standardized feature-level auditing for safety and interpretability, and highlight the need for mechanism-aware optimization objectives.
