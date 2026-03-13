---
interest: medium
link: https://arxiv.org/abs/2603.08809
next_step: skim
priority: medium
slack_ts: '1773369876.569579'
source: cs.CV - Computer Vision
status: unread
title: 'Where, What, Why: Toward Explainable 3D-GS Watermarking'
---
# Where, What, Why: Toward Explainable 3D-GS Watermarking
> 原文: [https://arxiv.org/abs/2603.08809](https://arxiv.org/abs/2603.08809)

arXiv:2603.08809v1 Announce Type: new
Abstract: As 3D Gaussian Splatting becomes the de facto representation for interactive 3D assets, robust yet imperceptible watermarking is critical. We present a representation-native framework that separates where to write from how to preserve quality. A Trio-Experts module operates directly on Gaussian primitives to derive priors for carrier selection, while a Safety and Budget Aware Gate (SBAG) allocates Gaussians to watermark carriers, optimized for bit resilience under perturbation and bitrate budgets, and to visual compensators that are insulated from watermark loss. To maintain fidelity, we introduce a channel-wise group mask that controls gradient propagation for carriers and compensators, thereby limiting Gaussian parameter updates, repairing local artifacts, and preserving high-frequency details without increasing runtime. Our design yields view-consistent watermark persistence and strong robustness against common image distortions such as compression and noise, while achieving a favorable robustness-quality trade-off compared with prior methods. In addition, decoupled finetuning provides per-Gaussian attributions that reveal where the message is carried and why those carriers are selected, enabling auditable explainability. Compared with state-of-the-art methods, our approach achieves a PSNR improvement of +0.83 dB and a bit-accuracy gain of +1.24%.
