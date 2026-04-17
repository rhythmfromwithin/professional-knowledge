---
title: "PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.13153
priority: medium
status: unread
interest: medium
next_step: skim
---
# PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction
> 原文: [https://arxiv.org/abs/2604.13153](https://arxiv.org/abs/2604.13153)

arXiv:2604.13153v1 Announce Type: new
Abstract: 3D Gaussian Splatting (3DGS) has recently enabled highly photorealistic 3D reconstruction from casually captured multi-view images. However, this accessibility raises a privacy concern: publicly available images or videos can be exploited to reconstruct detailed 3D models of scenes or objects without the owner's consent. We present PatchPoison, a lightweight dataset-poisoning method that prevents unauthorized 3D reconstruction. Unlike global perturbations, PatchPoison injects a small high-frequency adversarial patch, a structured checkerboard, into the periphery of each image in a multi-view dataset. The patch is designed to corrupt the feature-matching stage of Structure-from-Motion (SfM) pipelines such as COLMAP by introducing spurious correspondences that systematically misalign estimated camera poses. Consequently, downstream 3DGS optimization diverges from the correct scene geometry. On the NeRF-Synthetic benchmark, inserting a 12 X 12 pixel patch increases reconstruction error by 6.8x in LPIPS, while the poisoned images remain unobtrusive to human viewers. PatchPoison requires no pipeline modifications, offering a practical, "drop-in" preprocessing step for content creators to protect their multi-view data.
