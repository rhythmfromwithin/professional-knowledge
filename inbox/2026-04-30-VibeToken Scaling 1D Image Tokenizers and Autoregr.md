---
title: "VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.24885
priority: medium
status: unread
interest: medium
next_step: skim
---
# VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations
> 原文: [https://arxiv.org/abs/2604.24885](https://arxiv.org/abs/2604.24885)

arXiv:2604.24885v1 Announce Type: new
Abstract: We introduce an efficient, resolution-agnostic autoregressive (AR) image synthesis approach that generalizes to arbitrary resolutions and aspect ratios, narrowing the gap to diffusion models at scale. At its core is VibeToken, a novel resolution-agnostic 1D Transformer-based image tokenizer that encodes images into a dynamic, user-controllable sequence of 32-256 tokens, achieving a state-of-the-art efficiency and performance trade-off. Building on VibeToken, we present VibeToken-Gen, a class-conditioned AR generator with out-of-the-box support for arbitrary resolutions while requiring significantly fewer compute resources. Notably, VibeToken-Gen synthesizes 1024x1024 images using only 64 tokens and achieves 3.94 gFID; by comparison, a diffusion-based state-of-the-art alternative requires 1,024 tokens and attains 5.87 gFID. In contrast to fixed-resolution AR models such as LlamaGen -- whose inference FLOPs grow quadratically with resolution (11T FLOPs at 1024x1024) -- VibeToken-Gen maintains a constant 179G FLOPs (63.4x efficient) independent of resolution. We hope VibeToken can help unlock the wide adoption of AR visual generative models in production use cases.
