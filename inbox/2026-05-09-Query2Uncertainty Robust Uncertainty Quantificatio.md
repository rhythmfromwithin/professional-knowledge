---
title: "Query2Uncertainty: Robust Uncertainty Quantification and Calibration for 3D Object Detection under Distribution Shift"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.05328
priority: medium
status: unread
interest: medium
next_step: skim
---
# Query2Uncertainty: Robust Uncertainty Quantification and Calibration for 3D Object Detection under Distribution Shift
> 原文: [https://arxiv.org/abs/2605.05328](https://arxiv.org/abs/2605.05328)

arXiv:2605.05328v1 Announce Type: new
Abstract: Reliable uncertainty estimation for 3D object detection is critical for deploying safe autonomous systems, yet modern detectors remain poorly calibrated, especially under distribution shifts. Although post-hoc calibration methods address this issue and provide improved calibration for in-distribution tests, they fail to adapt in distribution-shifted scenarios. In this work, we address this issue and introduce a density-aware calibration method that couples post-hoc calibrators with the feature density of latent object queries from DETR-style 3D object detectors. These queries form a compact, location and class-aware feature, ideal for density estimation, allowing our approach to adjust model confidences in distribution-shift scenarios. By fitting a density estimator on these query features, our approach jointly recalibrates both classification and bounding box regression uncertainties. On both a multi-view camera and LiDAR-based detector, our approach consistently outperforms standard post-hoc methods in both in-distribution and distribution-shifted scenarios. Code available https://tillbeemelmanns.github.io/query2uncertainty/ .
