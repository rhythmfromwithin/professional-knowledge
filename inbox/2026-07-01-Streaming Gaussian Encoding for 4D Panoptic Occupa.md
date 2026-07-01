---
interest: medium
link: https://arxiv.org/abs/2606.30754
next_step: skim
priority: medium
slack_ts: '1782880938.568459'
source: cs.CV - Computer Vision
status: unread
title: Streaming Gaussian Encoding for 4D Panoptic Occupancy Tracking
---
# Streaming Gaussian Encoding for 4D Panoptic Occupancy Tracking
> 原文: [https://arxiv.org/abs/2606.30754](https://arxiv.org/abs/2606.30754)

arXiv:2606.30754v1 Announce Type: new
Abstract: Camera-based 4D panoptic occupancy tracking (4D-POT) is a promising paradigm for holistic scene understanding from multi-view imagery, enabling joint reasoning about geometry, semantics, and object identities across time. Recent mask-based pipelines achieve strong performance by propagating instance queries across frames. However, their underlying volumetric representations are typically recomputed at each timestep, limiting geometric temporal consistency, particularly under occlusion and for static scene elements. To address this limitation, we propose a streaming Gaussian encoder that maintains a persistent volumetric scene representation for 4D-POT. Our method models the scene as a fixed-size set of latent Gaussian queries that are propagated via ego-motion compensation and refreshed under a confidence-guided budget constraint. Crucially, we shape Gaussian opacities through depth-based supervision to serve as proxy for visibility, enabling confidence to accumulate as a temporally aggregated measure of persistent scene support. Together with a warmup-based multi-frame training strategy, this yields representation-level temporal coherence beyond decoder-only tracking. Extensive experiments on Occ3D-extended nuScenes and Waymo establish a new state-of-the-art for camera-based 4D-POT, improving tracking consistency with negligible computational overhead while remaining fully compatible with existing mask-based pipelines. We provide code and models at https://sge.cs.uni-freiburg.de.
