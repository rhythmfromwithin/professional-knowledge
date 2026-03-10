---
title: "CamDirector: Towards Long-Term Coherent Video Trajectory Editing"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.02256
priority: medium
status: unread
interest: medium
next_step: skim
---
# CamDirector: Towards Long-Term Coherent Video Trajectory Editing
> 原文: [https://arxiv.org/abs/2603.02256](https://arxiv.org/abs/2603.02256)

arXiv:2603.02256v1 Announce Type: new
Abstract: Video (camera) trajectory editing aims to synthesize new videos that follow user-defined camera paths while preserving scene content and plausibly inpainting previously unseen regions, upgrading amateur footage into professionally styled videos. Existing VTE methods struggle with precise camera control and long-range consistency because they either inject target poses through a limited-capacity embedding or rely on single-frame warping with only implicit cross-frame aggregation in video diffusion models. To address these issues, we introduce a new VTE framework that 1) explicitly aggregates information across the entire source video via a hybrid warping scheme. Specifically, static regions are progressively fused into a world cache then rendered to target camera poses, while dynamic regions are directly warped; their fusion yields globally consistent coarse frames that guide refinement. 2) processes video segments jointly with their history via a history-guided autoregressive diffusion model, while the world cache is incrementally updated to reinforce already inpainted content, enabling long-term temporal coherence. Finally, we present iPhone-PTZ, a new VTE benchmark with diverse camera motions and large trajectory variations, and achieve state-of-the-art performance with fewer parameters.
