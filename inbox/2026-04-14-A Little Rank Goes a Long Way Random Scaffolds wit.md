---
interest: medium
link: https://arxiv.org/abs/2604.08749
next_step: skim
priority: low
slack_ts: '1776137316.296169'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All
  You Need'
---
# A Little Rank Goes a Long Way: Random Scaffolds with LoRA Adapters Are All You Need
> 原文: [https://arxiv.org/abs/2604.08749](https://arxiv.org/abs/2604.08749)

arXiv:2604.08749v2 Announce Type: cross
Abstract: How many of a neural network's parameters actually encode task-specific information? We investigate this question with LottaLoRA, a training paradigm in which every backbone weight is drawn at random and frozen; only low-rank LoRA adapters are trained. Across nine benchmarks spanning diverse architecture families from single-layer classifiers to 900M parameter Transformers low-rank adapters over frozen random backbones recover 96-100% of fully trained performance while training only 0.5-40% of the parameters. The task-specific signal therefore occupies a subspace orders of magnitude smaller than the full parameter count suggests. Three mechanistic findings underpin this result:(1) the frozen backbone is actively exploited when static the learned scaling~$\beta$ remains strictly positive across all architectures but when the scaffold is destabilized, the optimizer silences it and the LoRA factors absorb all task information; (2) the frozen backbone is preferable but interchangeable any random initialization works equally well, provided it remains fixed throughout training; and (3) the minimum LoRA rank at which performance saturates estimates the intrinsic dimensionality of the task, reminiscent of the number of components retained in Principal Component Analysis (PCA). The construction is formally analogous to Reservoir Computing unfolded along the depth axis of a feedforward network. Because the backbone is determined by a random seed alone, models can be distributed as adapters plus seed a footprint that grows with task complexity, not model size, so that storage and memory savings compound as architectures scale.
