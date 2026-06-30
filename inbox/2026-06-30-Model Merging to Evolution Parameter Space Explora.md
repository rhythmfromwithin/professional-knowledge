---
interest: medium
link: https://arxiv.org/abs/2606.28373
next_step: skim
priority: low
slack_ts: '1782792824.290359'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Model Merging to Evolution: Parameter Space Exploration for Expert Models'
---
# Model Merging to Evolution: Parameter Space Exploration for Expert Models
> 原文: [https://arxiv.org/abs/2606.28373](https://arxiv.org/abs/2606.28373)

arXiv:2606.28373v1 Announce Type: new
Abstract: Model merging integrates the capabilities of multiple expert models to create strong models for multiple tasks without additional training, thereby reducing computational resource requirements. However, existing methods operate within the convex combination space of expert models, failing to explore high-performance regions outside this space. This paper proposes the MERGEvolve framework, which unifies model merging and evolution within an evolution strategy by treating the merged model as the initialization for evolutionary exploration of the parameter space. During the merging phase, expert models act as deterministic sources to build a strong initial point. The evolution phase then explores the parameter space using random noise. Theoretical analysis shows that MERGEvolve explores regions outside the convex combination space. Extensive experiments on single-task and multi-task benchmarks demonstrate that MERGEvolve consistently achieves performance competitive with advanced model merging baselines. Ablation studies confirm that a high-quality initial point is critical for efficient exploration of the parameter space.
