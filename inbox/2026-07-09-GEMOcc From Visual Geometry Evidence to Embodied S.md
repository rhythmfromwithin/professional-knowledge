---
title: "GEM-Occ: From Visual Geometry Evidence to Embodied Semantic Occupancy Memory"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.05543
priority: medium
status: unread
interest: medium
next_step: skim
---
# GEM-Occ: From Visual Geometry Evidence to Embodied Semantic Occupancy Memory
> 原文: [https://arxiv.org/abs/2607.05543](https://arxiv.org/abs/2607.05543)

arXiv:2607.05543v1 Announce Type: new
Abstract: Semantic occupancy provides a structured spatial memory for embodied indoor agents by jointly representing occupied regions, observed free space, unknown areas, and object semantics. However, existing indoor occupancy benchmarks and methods mainly focus on single-view prediction or room-level online perception, leaving long-horizon semantic mapping across connected indoor spaces underexplored. We introduce HIOcc, a hierarchical indoor occupancy benchmark that unifies ScanNet, ScanNet++, and Matterport3D under a common sparse semantic occupancy format while preserving their native observation geometries, including perspective RGB-D frames and pano-centric observation groups. HIOcc supports three complementary evaluation regimes: local semantic occupancy prediction, room-level online occupancy mapping, and building-level mapping across connected panoramic environments. We further propose GEM-Occ, a Gaussian Evidence Memory framework for semantic occupancy mapping. Rather than using pointmaps as persistent map states, GEM-Occ treats local visual geometry predictions as transient evidence, converts them into semantic Gaussian occupancy evidence and free-space ray evidence, and fuses them into a persistent hierarchical memory through visibility- and uncertainty-aware causal updates. The memory is organized into local caches, room-level submaps, and a building-level graph, and can be queried at any time through Gaussian-to-occupancy splatting. Experiments on HIOcc show that GEM-Occ improves local occupancy prediction, online map stability, free-space reasoning, revisit consistency, and building-level scalability over prior indoor occupancy and Gaussian-based mapping baselines.
