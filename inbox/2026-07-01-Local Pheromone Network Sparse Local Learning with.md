---
interest: medium
link: https://arxiv.org/abs/2606.30669
next_step: skim
priority: low
slack_ts: '1782880935.136689'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Local Pheromone Network: Sparse Local Learning with Multi-Scale Synaptic Trails,
  Consolidation, and Replay'
---
# Local Pheromone Network: Sparse Local Learning with Multi-Scale Synaptic Trails, Consolidation, and Replay
> 原文: [https://arxiv.org/abs/2606.30669](https://arxiv.org/abs/2606.30669)

arXiv:2606.30669v1 Announce Type: new
Abstract: Backpropagation-trained dense neural networks are powerful function approximators, but they couple learning across many parameters and can overwrite previous associations when tasks conflict. This paper describes Local Pheromone Network, a small research prototype for sparse, local, manually updated neural networks. In Local Pheromone Network, each output unit reads only a fixed local neighborhood of input units subject to geometric distance and molecular-tag compatibility. Each synapse stores a weight, a short-term pheromone trace, a long-term pheromone trace, and an optional consolidation state. Training does not call automatic differentiation. Instead, every layer performs a pheromone-weighted Hebbian-style update on a budgeted subset of local synapses selected from local error and co-activity. The update budget adapts online: it shrinks when loss improves and expands toward recently active neighborhoods when loss worsens. Optional mechanisms add structural plasticity, local replay, output masks for partitioned learning, and a target-free local contrastive step. We present the implementation, learning rule, and preliminary experiments on synthetic regression, partitioned memory, conflicting memory, consolidated conflict, structural plasticity, replay, and a synthetic long-context hybrid memory task. The prototype learns local linear rules, preserves partitioned memories through tags and masks, reduces forgetting under consolidation, and uses replay under conflict.
