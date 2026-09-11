---
interest: medium
link: https://arxiv.org/abs/2609.10608
next_step: skim
priority: low
slack_ts: '1789100107.017389'
source: cs.CR - Cryptography and Security
status: unread
title: 'Adaptive Diffusion Freezing: Privacy-preserving Diffusion Models Against Membership
  Inference Attacks'
---
# Adaptive Diffusion Freezing: Privacy-preserving Diffusion Models Against Membership Inference Attacks
> 原文: [https://arxiv.org/abs/2609.10608](https://arxiv.org/abs/2609.10608)

arXiv:2609.10608v1 Announce Type: new
Abstract: Diffusion models have achieved remarkable success in generative tasks across various areas, however their training process raises significant privacy concerns, particularly under membership inference attacks (MIAs). Prior studies on privacy-preserving of diffusion models fail to balance privacy, utility, and efficiency. To address this gap, we propose a novel framework of privacy-preserving diffusion models, Adaptive Diffusion Freezing (ADF), which can defend against MIAs with better trade-off. By leveraging cross-timestep adaptive freezing training, ADF explicitly control the participation of different data subsets across diffusion timesteps via a mask matrix, which reduces the over-memorization and leads to more uniform model behaviors between member and nonmember samples. To construct a freezing mask matrix that effectively reduce membership leakage without unnecessarily harming generation quality, we introduce a pretraining-based risk-aware freezing policy to estimate MIA risk based on memorization tendency, and suppress the contribution of the subset-timestep pairs with higher risk. Evaluations on multiple datasets demonstrate that ADF provides effective defense performance as well as state-of-the-art privacy-utility-efficiency trade-off performance compared to various baselines.
