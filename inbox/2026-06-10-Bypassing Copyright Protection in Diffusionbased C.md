---
interest: medium
link: https://arxiv.org/abs/2606.09909
next_step: skim
priority: low
slack_ts: '1781065401.179069'
source: cs.CR - Cryptography and Security
status: unread
title: Bypassing Copyright Protection in Diffusion-based Customization via Two-Stage
  Latent Feature Optimization
---
# Bypassing Copyright Protection in Diffusion-based Customization via Two-Stage Latent Feature Optimization
> 原文: [https://arxiv.org/abs/2606.09909](https://arxiv.org/abs/2606.09909)

arXiv:2606.09909v1 Announce Type: new
Abstract: With the growing concerns over copyright infringement in diffusion-based customization, adversarial attacks have emerged as a prominent defense strategy to prevent malicious content forgery in personalized image generation. However, current defenses typically introduce persistent perturbations in the latent space of Latent Diffusion Models (LDMs), which remain susceptible to adaptive bypasses by adversaries. In this paper, we introduce Two-Stage Latent Feature Optimization (TS-LFO), an efficient and effective copyright-stealing attack against protected diffusion-based customization. We begin by observing that existing defenses primarily disrupt the mapping between input images and their latent representations, thereby degrading the model's ability to produce personalized outputs. To counteract this, TS-LFO restores the broken mapping through a two-stage optimization process. In the Latent Denoising Stage, we enhance semantic consistency between latent codes and input images by jointly minimizing a Latent-Image Alignment Loss and a Latent Diffusion Loss with timestep-dependent weights, effectively suppressing the high-frequency noise introduced by defenses. In the Latent Reconstruction Stage, we recover low-frequency semantic information using pixel-level constraints to refine the latent features. Extensive experiments show that TS-LFO consistently bypasses state-of-the-art (SOTA) copyright defenses and outperforms SOTA copyright attacks such as DiffPure, GrIDPure and IMPRESS across diverse settings.
