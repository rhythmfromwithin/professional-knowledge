---
title: "GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.22882
priority: medium
status: unread
interest: medium
next_step: skim
---
# GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation
> 原文: [https://arxiv.org/abs/2605.22882](https://arxiv.org/abs/2605.22882)

arXiv:2605.22882v1 Announce Type: new
Abstract: Video world models can generate realistic futures from a single instruction, but they often fail to preserve consistent point-level motion over time. As a result, the generated videos appear plausible, yet lack the physical grounding required for reliable action execution, such as robot manipulation. We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision, distilled from a pretrained geometry foundation model, into the video generative backbone during training. This supervision enables the model to jointly capture appearance and geometric structure while retaining a single-stream architecture with no additional inference cost. We further introduce an inverse dynamics module that converts correspondence-consistent video rollouts into executable robot trajectories, enabling direct deployment in both real-world and simulated manipulation. GEM-4D achieves state-of-the-art performance on both video prediction and geometric consistency across simulation and realistic scenarios and improves real-world manipulation success from 61% to 81%. Additional results are available at the project page: https://anonymous-submission-20.github.io/gem.github.io/.
