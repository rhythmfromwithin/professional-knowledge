---
title: "Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.14182
priority: medium
status: unread
interest: medium
next_step: skim
---
# Semantic Audio-driven Understanding for Dynamic Humanoid Whole Body Control
> 原文: [https://arxiv.org/abs/2607.14182](https://arxiv.org/abs/2607.14182)

arXiv:2607.14182v1 Announce Type: new
Abstract: Recent advances in humanoid robotics and reinforcement learning have enabled the acquisition of highly expressive whole-body motion policies. However, most robotic performances remain based on pre-scripted sequences or externally triggered behaviors, limiting autonomy and responsiveness to dynamic environments. In this work, we introduce a novel multi-modal orchestration framework for semantic audio-driven humanoid control, enabling robots to autonomously select and execute appropriate motion skills in real time. The system processes continuous audio streams and routes them into music or speech branches. Music input is handled via audio fingerprinting and semantic embeddings to retrieve track identity and temporal alignment, allowing dynamic mapping between musical segments and motion policies. Speech input is grounded into a discrete library of imitation-learned skills, enabling direct human-robot interaction. Both modalities share a unified interface that schedules skill execution over a reinforcement learning control pipeline. We validate the approach in simulation and on a Unitree G1 humanoid, showing robust sim-to-real transfer and consistent audio-conditioned policy selection. Supplementary materials are available at the following site: https://lab-rococo-sapienza.github.io/semantic-WBC/
