---
interest: medium
link: https://arxiv.org/abs/2603.12361
next_step: skim
priority: medium
slack_ts: '1773715546.573929'
source: cs.RO - Robotics
status: unread
title: 'GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning'
---
# GNN-DIP: Neural Corridor Selection for Decomposition-Based Motion Planning
> 原文: [https://arxiv.org/abs/2603.12361](https://arxiv.org/abs/2603.12361)

arXiv:2603.12361v1 Announce Type: new
Abstract: Motion planning through narrow passages remains a core challenge: sampling-based planners rarely place samples inside these narrow but critical regions, and even when samples land inside a passage, the straight-line connections between them run close to obstacle boundaries and are frequently rejected by collision checking. Decomposition-based planners resolve both issues by partitioning free space into convex cells -- every passage is captured exactly as a cell boundary, and any path within a cell is collision-free by construction. However, the number of candidate corridors through the cell graph grows combinatorially with environment complexity, creating a bottleneck in corridor selection. We present GNN-DIP, a framework that addresses this by integrating a Graph Neural Network (GNN) with a two-phase Decomposition-Informed Planner (DIP). The GNN predicts portal scores on the cell adjacency graph to bias corridor search toward near-optimal regions while preserving completeness. In 2D, Constrained Delaunay Triangulation (CDT) with the Funnel algorithm yields exact shortest paths within corridors; in 3D, Slab convex decomposition with portal-face sampling provides near-optimal path evaluation. Benchmarks on 2D narrow-passage scenarios, 3D bottleneck environments with up to 246 obstacles, and dynamic 2D settings show that GNN-DIP achieves 99--100% success rates with 2--280 times speedup over sampling-based baselines.
