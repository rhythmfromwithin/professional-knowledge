---
interest: medium
link: https://arxiv.org/abs/2610.31765
next_step: skim
priority: medium
slack_ts: '1793164453.044629'
source: cs.CV - Computer Vision
status: unread
title: 'SyncVid: World-Equivariant Diffusion for Synchronized Video Generation'
---
# SyncVid: World-Equivariant Diffusion for Synchronized Video Generation
> 原文: [https://arxiv.org/abs/2610.31765](https://arxiv.org/abs/2610.31765)

arXiv:2610.31765v1 Announce Type: new
Abstract: Generating multiple videos of a dynamic scene from a single reference video requires synthesizing both observed and unobserved content consistently across viewpoints. Existing camera-control methods for video diffusion typically rely on architectural mechanisms, including camera embeddings, cross-view attention, and geometric conditioning. Although effective for static scene content, these approaches often struggle with the fine-grained, dynamic geometry that must remain coherent across views and over time. We synchronize the diffusion process itself by sampling the Gaussian noise prior in a canonical 3D space derived from the source video and rasterizing it into target cameras, rather than sampling independently in each 2D image plane. Our method, SyncVid, lifts a monocular video into a canonical 4D representation, associates noise with scene geometry and unseen space, and rasterizes the resulting structured noise into arbitrary views. Because rendering can introduce local correlations, we further propose a cross-view-consistent whitening procedure that decorrelates neighboring pixels while preserving correspondence across views. The structured noise serves as the diffusion prior for a LoRA-adapted pretrained video diffusion model, requiring no architectural modifications. By enforcing spatiotemporal and cross-view coherence at the source of stochasticity, SyncVid generates synchronized videos and improves both perceptual quality and cross-view consistency in our experiments. Project page: https://qualcomm-ai-research.github.io/SyncVid-Webpage.
