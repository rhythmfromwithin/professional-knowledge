---
interest: medium
link: https://arxiv.org/abs/2607.00058
next_step: skim
priority: medium
slack_ts: '1783050935.816389'
source: cs.CV - Computer Vision
status: unread
title: Joint Medical Image Enhancement and Segmentation with Diffusion-based Symbiotic
  Information Interaction
---
# Joint Medical Image Enhancement and Segmentation with Diffusion-based Symbiotic Information Interaction
> 原文: [https://arxiv.org/abs/2607.00058](https://arxiv.org/abs/2607.00058)

arXiv:2607.00058v1 Announce Type: new
Abstract: Image quality is critical for accurate medical diagnosis. However, MRI, CT, and ultrasound images are often of low resolution and quality due to cost constraints, complicating the visualization of key anatomical structures and lesions. While such limitations are common in practice, traditional methods treat image enhancement as a separate preprocessing step, failing to fully leverage its potential synergy with image segmentation. To address this, we propose DiSIINet (Diffusion-based Symbiotic Information Interaction Network), which is built on the principle that enhancement and segmentation should mutually reinforce each other in a unified model. Based on Denoising Diffusion Implicit Models (DDIM), DiSIINet integrates an enhancement branch and a segmentation branch. These branches interact through a novel Symbiotic Information Interaction (SII) module, which facilitates dynamic, feature-level information exchange via cross-attention during the reverse diffusion process. This design enables both tasks to iteratively improve each other. The DDIM backbone ensures high-quality output and efficient inference through deterministic sampling. Experiments on multi-modal medical datasets (MRI, CT, ultrasound) show that DiSIINet achieves significant performance improvements compared to sequential or independent enhancement and segmentation approaches. The code is available at: https://github.com/Reconsider80/DiSIINet.
