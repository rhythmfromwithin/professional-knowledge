---
title: "EgoHand: Monocular 3D Hand Reconstruction from Egocentric Video"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.30293
priority: medium
status: unread
interest: medium
next_step: skim
---
# EgoHand: Monocular 3D Hand Reconstruction from Egocentric Video
> 原文: [https://arxiv.org/abs/2610.30293](https://arxiv.org/abs/2610.30293)

arXiv:2610.30293v1 Announce Type: new
Abstract: We introduce EgoHand, a monocular 3D hand reconstruction model that achieves state-of-the-art performance on egocentric video. Central to our approach is the curation of a high-quality training corpus of 14 million images, combining synthetic data, in-the-wild video, and multi-camera motion capture to balance scene diversity and supervision quality. The model adopts SOMA-Hand as its parametric representation and processes 2D hand crops with a transformer encoder, incorporating camera cues and an auxiliary 2D branch to improve geometric consistency and image alignment. Zero-shot evaluations on HOT3D, ARCTIC, and H2O demonstrate strong out-of-domain generalization, with lower joint-position, root-translation, and acceleration errors than competing baselines at an inference latency of approximately 9.69 ms. A blinded user preference study further shows that participants favor EgoHand's reconstructed hand poses over those from Apple EgoDex and Ropedia Xperience-10M. We release the EgoHand model and source code under the OpenMDW license, allowing free commercial use of the model.
