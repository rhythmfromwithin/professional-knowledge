---
title: "VoxelDiffusionCut: Non-destructive Internal-part Extraction via Iterative Cutting and Structure Estimation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.00116
priority: medium
status: unread
interest: medium
next_step: skim
---
# VoxelDiffusionCut: Non-destructive Internal-part Extraction via Iterative Cutting and Structure Estimation
> 原文: [https://arxiv.org/abs/2603.00116](https://arxiv.org/abs/2603.00116)

arXiv:2603.00116v1 Announce Type: new
Abstract: Non-destructive extraction of the target internal part, such as batteries and motors, by cutting surrounding structures is crucial at recycling and disposal sites. However, the diversity of products and the lack of information on disassembly procedures make it challenging to decide where to cut. This study explores a method for non-destructive extraction of a target internal part that iteratively estimates the internal structure from observed cutting surfaces and formulates cutting plans based on the estimation results. A key requirement is to estimate the probability of the target part's presence from partial observations. However, learning conditional generative models for this task is challenging: The high dimensionality of 3D shape representations makes learning difficult, and conventional models (e.g., conditional variational autoencoders) often fail to capture multi-modal predictive uncertainty due to mode collapse, resulting in overconfident predictions. To address these issues, we propose VoxelDiffusionCut, which iteratively estimates the internal structure represented as voxels using a diffusion model and plans cuts for non-destructive extraction of the target internal part based on the estimation results. Voxel representation allows the model to predict only attributes at fixed grid positions, i.e., types of constituent parts, making learning more tractable. The diffusion model completes the voxel representation conditioned on observed cutting surfaces, capturing uncertainty in unobserved regions to avoid erroneous cuts. Experimental results in simulation suggest that the proposed method can estimate internal structures from observed cutting surfaces and enable non-destructive extraction of the target internal part by leveraging the estimated uncertainty.
