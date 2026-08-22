---
title: "Clustering and Token Denoising for Faster and More Robust VLMs"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.19285
priority: medium
status: unread
interest: medium
next_step: skim
---
# Clustering and Token Denoising for Faster and More Robust VLMs
> 原文: [https://arxiv.org/abs/2608.19285](https://arxiv.org/abs/2608.19285)

arXiv:2608.19285v1 Announce Type: new
Abstract: Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLaVA showing impressive results. However, the computational burden of processing up to 576 or 729 visual tokens makes edge deployment challenging. While various token pruning techniques require retraining, some are training-free and thus can easily adapt to architecture changes. We introduce ClustRS, a two-part, training-free algorithm for robust token pruning. Its first component is an attention-weighted, clustering algorithm that selects representative tokens from each semantic cluster. The second component, Residual Shrinkage, is a one-pass denoising step on the selected tokens. These training-free lightweight steps make LLaVA ready for real-world data, improving robustness to a wide range of image-noise types and intensities. Experimental results on the ScienceQA-IMG and MM-VET benchmarks show our method outperforms attention- and diversity-based methods by up to 20\% under extreme noise and token conditions (reducing tokens by 97\%, down to 16 tokens) on LLaVA 1.5 7b and achieves exceptional results on LLaVA-OneVision, where we match baseline performance with fewer than one-third of their tokens under mild noise conditions. Our study demonstrates a simple yet powerful alternative to both score-only and diversity-only pruning rules, paving the way for compute-efficient and noise-resilient VLM deployment.
