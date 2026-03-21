---
title: "GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.18210
priority: medium
status: unread
interest: medium
next_step: skim
---
# GoalVLM: VLM-driven Object Goal Navigation for Multi-Agent System
> 原文: [https://arxiv.org/abs/2603.18210](https://arxiv.org/abs/2603.18210)

arXiv:2603.18210v1 Announce Type: new
Abstract: Object-goal navigation has traditionally been limited to ground robots with closed-set object vocabularies. Existing multi-agent approaches depend on precomputed probabilistic graphs tied to fixed category sets, precluding generalization to novel goals at test time.
We present GoalVLM, a cooperative multi-agent framework for zero-shot, open-vocabulary object navigation. GoalVLM integrates a Vision-Language Model (VLM) directly into the decision loop, SAM3 for text-prompted detection and segmentation, and SpaceOM for spatial reasoning, enabling agents to interpret free-form language goals and score frontiers via zero-shot semantic priors without retraining. Each agent builds a BEV semantic map from depth-projected voxel splatting, while a Goal Projector back-projects detections through calibrated depth into the map for reliable goal localization. A constraint-guided reasoning layer evaluates frontiers through a structured prompt chain (scene captioning, room-type classification, perception gating, multi-frontier ranking), injecting commonsense priors into exploration.
We evaluate GoalVLM on GOAT-Bench val\_unseen (360 multi-subtask episodes, 1032 sequential object-goal subtasks, HM3D scenes), where each episode requires navigating to a chain of 5-7 open-vocabulary targets. GoalVLM with N=2 agents achieves 55.8% subtask SR and 18.3% SPL, competitive with state-of-the-art methods while requiring no task-specific training. Ablation studies confirm the contributions of VLM-guided frontier reasoning and depth-projected goal localization.
