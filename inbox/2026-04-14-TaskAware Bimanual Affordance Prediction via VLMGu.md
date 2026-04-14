---
title: "Task-Aware Bimanual Affordance Prediction via VLM-Guided Semantic-Geometric Reasoning"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.08726
priority: medium
status: unread
interest: medium
next_step: skim
---
# Task-Aware Bimanual Affordance Prediction via VLM-Guided Semantic-Geometric Reasoning
> 原文: [https://arxiv.org/abs/2604.08726](https://arxiv.org/abs/2604.08726)

arXiv:2604.08726v1 Announce Type: new
Abstract: Bimanual manipulation requires reasoning about where to interact with an object and which arm should perform each action, a joint affordance localization and arm allocation problem that geometry-only planners cannot resolve without semantic understanding of task intent. Existing approaches either treat affordance prediction as coarse part segmentation or rely on geometric heuristics for arm assignment, failing to jointly reason about task-relevant contact regions and arm allocation. We reframe bimanual manipulation as a joint affordance localization and arm allocation problem and propose a hierarchical framework for task-aware bimanual affordance prediction that leverages a Vision-Language Model (VLM) to generalize across object categories and task descriptions without requiring category-specific training. Our approach fuses multi-view RGB-D observations into a consistent 3D scene representation and generates global 6-DoF grasp candidates, which are then spatially and semantically filtered by querying the VLM for task-relevant affordance regions on each object, as well as for arm allocation to the individual objects, thereby ensuring geometric validity while respecting task semantics. We evaluate our method on a dual-arm platform across nine real-world manipulation tasks spanning four categories: parallel manipulation, coordinated stabilization, tool use, and human handover. Our approach achieves consistently higher task success rates than geometric and semantic baselines for task-oriented grasping, demonstrating that explicit semantic reasoning over affordances and arm allocation helps enable reliable bimanual manipulation in unstructured environments.
