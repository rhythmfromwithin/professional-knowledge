---
title: "PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.16984
priority: medium
status: unread
interest: medium
next_step: skim
---
# PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation
> 原文: [https://arxiv.org/abs/2608.16984](https://arxiv.org/abs/2608.16984)

arXiv:2608.16984v1 Announce Type: new
Abstract: Recent monocular depth estimators achieve strong zero-shot generalization, yet often struggle to preserve fine-grained structures and object boundaries. We attribute this limitation to the prevalent combination of large-patch ViT encoders and convolutional decoders, as coarse tokenization can weaken pixel-level cues that upsampling cannot fully recover. To address this issue, we propose PXDepth, a discriminative monocular depth model that separates global context modeling from pixel-level depth prediction. Specifically, a large-patch ViT captures global scene context, while a pixel-space predictor composed of Context-Modulated Pixel Transformer blocks maintains high-resolution spatial representations throughout depth estimation. This design preserves fine structures and sharp boundaries without sacrificing global depth consistency. Across diverse zero-shot benchmarks, PXDepth combines faithful local geometry with competitive global depth accuracy while remaining efficient at inference. Our code and model are available at https://yuanzhy29.github.io/PXDepth-Page/.
