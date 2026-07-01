---
interest: medium
link: https://arxiv.org/abs/2606.30647
next_step: skim
priority: medium
slack_ts: '1782880929.046329'
source: cs.CV - Computer Vision
status: unread
title: Cross-Modal Hierarchical Fusion for from Multi-Sensor Ground Observation
---
# Cross-Modal Hierarchical Fusion for from Multi-Sensor Ground Observation
> 原文: [https://arxiv.org/abs/2606.30647](https://arxiv.org/abs/2606.30647)

arXiv:2606.30647v1 Announce Type: new
Abstract: Dense volumetric reconstruction of cloud microphysical fields from sparse ground-based instruments remains an open problem, largely because the available measurements are heterogeneous in both modality and spatial coverage. We present AtmoFuseNet, a framework that fuses multi-view sky camera imagery with millimeter-wave cloud radar and ceilometer observations to produce 4D (three spatial dimensions plus time) estimates of cloud state and wind. The method operates in three stages: a cross-modal hierarchical aggregation module that combines image feature pyramids with instrument-derived vertical profiles through layer-wise cross-attention; a conditional variational refinement module that maps the resulting volume to physically consistent microphysical fields under differentiable radar and image forward models; and a correlation-based motion estimator that recovers per-voxel 3D wind vectors from consecutive volumetric reconstructions. On collocated observations from a semi-arid site, AtmoFuseNet reaches 0.026 g m^-3 liquid water content MAE and 1.18 m s^-1 wind speed MAE, improving over existing retrieval baselines. Ablation experiments isolate the contribution of each module.
