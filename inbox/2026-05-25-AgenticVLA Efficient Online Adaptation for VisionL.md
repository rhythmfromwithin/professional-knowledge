---
title: "Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.22896
priority: medium
status: unread
interest: medium
next_step: skim
---
# Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2605.22896](https://arxiv.org/abs/2605.22896)

arXiv:2605.22896v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) models have emerged as a promising paradigm for robotic manipulation by leveraging pre-trained vision-language representations. However, current VLA training methods suffer from two critical limitations: poor generalization to novel environments and low training efficiency requiring extensive demonstrations. We introduce Agentic-VLA, an agentic training framework that enables VLAs to efficiently adapt online through three key innovations: (1) Adaptive Reward Synthesis, which dynamically generates and adjusts reward functions based on the VLA's current capabilities and task complexity, decomposing complex tasks into learnable sub-goals for curriculum learning; (2) Language-Guided Exploration, where a critic model provides structured guidance for systematic exploration rather than random sampling; and (3) Experience Memory,which stores and retrieves task-relevant policy weights for warm-starting adaptation to similar tasks. We evaluate Agentic-VLA on the LIBERO benchmark, achieving substantial improvements: +12.3% on long-horizon tasks, +28.5% in 1-shot learning, and enabling cross-task transfer from 0% to 31.2% without task-specific demonstrations. Our framework also demonstrates 2.4x faster convergence compared to existing online adaptation methods. Beyond LIBERO, Agentic-VLA retains its advantage on the dual-arm RoboTwin 2.0 benchmark, including under its randomized Hard setting. These results establish Agentic-VLA as a significant step toward truly adaptive VLA systems capable of continuous learning in deployment.
