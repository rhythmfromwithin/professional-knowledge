---
title: "Thinking with Spatial Code for Physical-World Video Reasoning"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.05591
priority: medium
status: unread
interest: medium
next_step: skim
---
# Thinking with Spatial Code for Physical-World Video Reasoning
> 原文: [https://arxiv.org/abs/2603.05591](https://arxiv.org/abs/2603.05591)

arXiv:2603.05591v1 Announce Type: new
Abstract: We introduce Thinking with Spatial Code, a framework that transforms RGB video into explicit, temporally coherent 3D representations for physical-world visual question answering. We highlight the empirical finding that our proposed spatial encoder can parse videos into structured spatial code with explicit 3D oriented bounding boxes and semantic labels, enabling large language models (LLMs) to reason directly over explicit spatial variables. Specifically, we propose the spatial encoder that encodes image and geometric features by unifying 6D object parsing and tracking backbones with geometric prediction, and we further finetuning LLMs with reinforcement learning using a spatial rubric reward that encourages perspective-aware, geometrically grounded inference. As a result, our model outperforms proprietary vision-language models on VSI-Bench, setting a new state-of-the-art. Code is available at https://github.com/Beckschen/spatialcode.
