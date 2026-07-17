---
interest: medium
link: https://arxiv.org/abs/2607.09753
next_step: skim
priority: medium
slack_ts: '1784258629.810699'
source: cs.CV - Computer Vision
status: unread
title: Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis
---
# Unified Backbone Refinement for Diffusion Models via Internal-Latent Analysis
> 原文: [https://arxiv.org/abs/2607.09753](https://arxiv.org/abs/2607.09753)

arXiv:2607.09753v1 Announce Type: new
Abstract: Diffusion models have achieved remarkable success across diverse domains, with performance closely related to the denoising backbones that parameterize the score function. In this paper, we present a systematic, phase-aware analysis of diffusion components and show that abrupt, early-stage fluctuations in deep latents are strongly associated with artifacts. Guided by these findings, we introduce DUNE (Diffusion Unified Network refiNEr), a training-free refinement framework that detects abrupt deviations in deep low-noise internal latents using a shared EMA-based criterion, and applies backbone-specific suppression to the detector-selected entries. Although derived from U-Net, the same detect-suppress principle extends naturally to Transformer-based diffusion models by acting on the latents of deep self-attention blocks. Extensive experiments across multiple backbones indicate that DUNE improves fidelity while reducing hallucinations, offering new insight into where and when diffusion backbones should be controlled.
