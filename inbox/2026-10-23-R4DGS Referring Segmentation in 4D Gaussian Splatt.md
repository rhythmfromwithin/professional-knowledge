---
title: "R4DGS: Referring Segmentation in 4D Gaussian Splatting"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.30326
priority: medium
status: unread
interest: medium
next_step: skim
---
# R4DGS: Referring Segmentation in 4D Gaussian Splatting
> 原文: [https://arxiv.org/abs/2610.30326](https://arxiv.org/abs/2610.30326)

arXiv:2610.30326v1 Announce Type: new
Abstract: Dynamic representations based on 4D Gaussian Splatting (4DGS) have shown strong capabilities in reconstruction and rendering, yet current methods remain limited in supporting complex natural-language referring in dynamic scenes. Existing 4D Gaussian methods are primarily designed for rendering-oriented dynamic modeling, while current semantic extensions often rely on scene-specific semantic optimization or are evaluated on relatively simple query settings. In this paper, we study Referring 4D Gaussian Splatting (R4DGS), a task for grounding temporally varying, multi-target or reasoning-intensive, and zero-target or distractor expressions in dynamic 4D scenes. To support this task, we introduce R4D-Bench-QA, a benchmark with structured query annotations. We further present ReferGaussian, a unified framework built upon 4DGS that converts low-level dynamic Gaussians into persistent, language-addressable entities for training-free referring inference. ReferGaussian organizes mask-supported Gaussian entities in an EntityBank, uses Multimodal Large Language Models (MLLMs) to decompose complex queries into trackable object phrases and structured referring constraints, and performs constraint-aware grounding without scene-specific semantic optimization. Experiments on R4D-Bench-QA and the 4D LangSplat protocol demonstrate improved temporal target selection and competitive spatiotemporal grounding without scene-specific semantic training. Project resources are available at https://chenbangpu.github.io/R4DGS/.
