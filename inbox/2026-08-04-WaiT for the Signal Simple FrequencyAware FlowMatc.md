---
interest: medium
link: https://arxiv.org/abs/2607.28760
next_step: skim
priority: medium
slack_ts: '1786072098.366449'
source: cs.CV - Computer Vision
status: unread
title: 'WaiT for the Signal: Simple Frequency-Aware Flow-Matching'
---
# WaiT for the Signal: Simple Frequency-Aware Flow-Matching
> 原文: [https://arxiv.org/abs/2607.28760](https://arxiv.org/abs/2607.28760)

arXiv:2607.28760v1 Announce Type: new
Abstract: As image generation models scale to ever higher resolutions, global coherence, local detail, and texture fidelity become critical axes for generation quality. However, standard flow matching treats all spatial frequencies uniformly, ignoring the natural frequency hierarchy where high-frequency bands become indistinguishable from pure noise far earlier than coarse structures. We introduce WaiT, a Wavelet-aware image Transformer that decomposes generation into coarse and fine bands via lossless wavelets. True to its name, the high-frequency bands wait for the signal: staying pure noise until coarse structure has emerged, then joining the flow for joint refinement. Since standard FID discards fine-grained detail through aggressive downsampling, we introduce a more stringent three-axis evaluation protocol to assess quality at native resolution. On ImageNet 512x512, WaiT achieves a pixel-space FID of 1.43 and is Pareto-optimal across all three axes, reducing sampling compute by up to 50%. With our largest 2B model, we set a new state-of-the-art FID of 1.3 for pixel-space models on ImageNet 512 resolution. Our formulation outperforms even the strongest latent-space models on texture fidelity, and scales seamlessly to high-resolution OpenImages and to video generation, achieving a state-of-the-art FVD of 0.84 on Kinetics-600 with no algorithmic modifications.
