---
title: "CineMesh4D: Personalized 4D Whole Heart Reconstruction from Sparse Cine MRI"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.13994
priority: medium
status: unread
interest: medium
next_step: skim
---
# CineMesh4D: Personalized 4D Whole Heart Reconstruction from Sparse Cine MRI
> 原文: [https://arxiv.org/abs/2605.13994](https://arxiv.org/abs/2605.13994)

arXiv:2605.13994v1 Announce Type: new
Abstract: Accurate 3D+t whole-heart mesh reconstruction from cine MRI is a clinically crucial yet technically challenging task. The difficulty of this task arises from two coupled factors: inherently sparse sampling of 3D cardiac anatomy by 2D image slices and the tight coupling between cardiac shape and motion. Current cardiac image-to-mesh approaches typically reconstruct only a subset of cardiac chambers or a single phase of the cardiac cycle. In this work, we propose CineMesh4D, a novel end-to-end 4D (3D+t) pipeline that directly reconstructs patient-specific whole-heart mesh from multi-view 2D cine MRI via cross-domain mapping. Specifically, we introduce a differentiable rendering loss that enables supervision of 3D+t whole-heart mesh from multi-view sparse contours of cine MRI. Furthermore, we develop a dual-context temporal block that fuses global and local cardiac temporal information to capture high-dimensional sequential patterns. In quantitative and qualitative evaluations, CineMesh4D outperforms existing approaches in terms of reconstruction quality and motion consistency, providing a practical pathway for personalized real-time cardiac assessment. The code will be publicly released once the manuscript is accepted.
