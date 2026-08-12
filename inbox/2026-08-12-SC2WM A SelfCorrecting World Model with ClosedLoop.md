---
title: "SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.07548
priority: medium
status: unread
interest: medium
next_step: skim
---
# SC$^{2}$-WM: A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments
> 原文: [https://arxiv.org/abs/2608.07548](https://arxiv.org/abs/2608.07548)

arXiv:2608.07548v1 Announce Type: new
Abstract: Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires agents to make fine-grained navigation decisions under partial observability. However, most existing methods rely on open-loop execution, lacking mechanisms to detect and correct internal state drift during inference. We propose SC$^{2}$-WM, a self-correcting world model framework that introduces internal feedback for closed-loop decision making in VLN-CE. Our method derives feedback from world-model foresight to perform state-level plan refinement before action execution. To handle challenging scenarios, we further introduce conditional world-aware adaptation, which enables model-level correction by selectively updating the world model at test time when feedback indicates model capacity insufficiency. Experiments on standard VLN-CE benchmarks demonstrate improved navigation robustness and generalization. Our code is available at https://github.com/sunrise-ikun/SC2\_WM.
