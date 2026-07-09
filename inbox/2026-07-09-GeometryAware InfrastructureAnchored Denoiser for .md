---
title: "Geometry-Aware Infrastructure-Anchored Denoiser for UWB Sensing and Work-Zone Reconstruction"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.05449
priority: high
status: unread
interest: medium
next_step: skim
---
# Geometry-Aware Infrastructure-Anchored Denoiser for UWB Sensing and Work-Zone Reconstruction
> 原文: [https://arxiv.org/abs/2607.05449](https://arxiv.org/abs/2607.05449)

arXiv:2607.05449v1 Announce Type: new
Abstract: Accurate work-zone geometry perception is critical for intelligent transportation systems, and ultra-wideband sensing offers a low-cost approach for infrastructure-aided reconstruction. However, outdoor UWB ranging is often degraded by non-line-of-sight propagation, burst noise, and long-tail errors, which can distort downstream spatial reconstruction. We present GAIA, a geometry-aware, infrastructure-anchored learning framework that couples temporal range modeling with latent anchor-layout estimation and deterministic distance projection. GAIA preserves range denoising as the supervised task while orienting the learned distances toward boundary-consistent reconstruction. We evaluate GAIA on a real-world outdoor UWB dataset with synchronized UWB, GNSS, and IMU measurements, and further test robustness using a real-data-calibrated stress-test simulator. GAIA achieves the lowest overall range MSE and highest polygon IoU among evaluated filtering-based and learning-based baselines, reducing MSE by 18.4% and improving polygon IoU by 15.5% over PoseMLP. These results show that geometry-aware range denoising provides an effective path toward spatially coherent work-zone reconstruction.
