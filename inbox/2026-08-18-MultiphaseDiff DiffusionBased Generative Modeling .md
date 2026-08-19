---
interest: medium
link: https://arxiv.org/abs/2608.13669
next_step: skim
priority: medium
slack_ts: '1787103720.820019'
source: cs.CV - Computer Vision
status: unread
title: 'Multiphase-Diff: Diffusion-Based Generative Modeling for High-Contrast Multiphase
  Physical Systems with Sharp Interfaces'
---
# Multiphase-Diff: Diffusion-Based Generative Modeling for High-Contrast Multiphase Physical Systems with Sharp Interfaces
> 原文: [https://arxiv.org/abs/2608.13669](https://arxiv.org/abs/2608.13669)

arXiv:2608.13669v1 Announce Type: new
Abstract: Physics-constrained diffusion for high-contrast, sharp-interface multiphase fields faces three coupled difficulties. At coefficient jumps, expanded pointwise strong-form PDE residuals contain singular gradient terms that can penalize physical interfaces. Under extreme contrast, low-magnitude phases may fall below the diffusion noise floor and be erased, misscaled, or generated with negative coefficients, while a global likelihood scale allows high-magnitude phases to dominate supervision. We therefore propose Multiphase-Diff, which makes three corresponding contributions: (i) a conservative flux residual that avoids differentiating discontinuous coefficients and enforces discrete conservation; (ii) an analytic bijective representation that maps low-amplitude signals to order-one latent scales and guarantees coefficient positivity through exponential decoding; and (iii) a Jacobi-preconditioned likelihood that normalizes local residual scales for balanced supervision. Experiments on three complementary multiphase benchmarks demonstrate the superiority of Multiphase-Diff over seven baselines in both physical and distributional fidelity and its robustness across phase contrasts and compositions, establishing its effectiveness for scientific sample generation in this challenging regime.
