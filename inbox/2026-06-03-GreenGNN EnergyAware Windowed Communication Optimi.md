---
interest: medium
link: https://arxiv.org/abs/2606.02916
next_step: skim
priority: medium
slack_ts: '1780462702.822929'
source: cs.DC - Distributed Computing
status: unread
title: 'GreenGNN: Energy-Aware Windowed Communication Optimization for Distributed
  GNN Training'
---
# GreenGNN: Energy-Aware Windowed Communication Optimization for Distributed GNN Training
> 原文: [https://arxiv.org/abs/2606.02916](https://arxiv.org/abs/2606.02916)

arXiv:2606.02916v1 Announce Type: new
Abstract: Large-scale graph neural network (GNN) training often requires distributed clusters because graph structure and feature tensors no longer fit in a single node's memory. In sampling-based training, each mini-batch expands into a receptive field that spans partitions and triggers thousands of remote feature fetches per epoch. This wastes energy for two main reasons: each small RPC pays a fixed initiation and protocol cost, and GPUs continue drawing substantial baseline power while waiting for remote features. We present GreenGNN, an energy-aware distributed GNN training system that reduces communication energy by exploiting the bursty, short-lived temporal locality of neighbor sampling. GreenGNN groups training into windows of W consecutive mini-batches, stages each window's hot features in a local cache, and merges remote requests from each partition owner into a small number of bulk transfers. This amortizes RPC overhead across many features while preserving an on-demand path for cache misses. Because window size controls the trade-off between communication amortization and hot-set staleness, GreenGNN selects W offline using a discrete-event simulator that replays a deterministic one-epoch access trace with a hybrid energy model. We implement GreenGNN on DGL and evaluate it on a 4-node GPU cluster with benchmark datasets. Across datasets and batch sizes, GreenGNN reduces total system energy by 27--43% relative to baseline while improving end-to-end throughput by up to 3.9x. GPU energy drops by 36--71%, driven by fewer RPC initiations and lower GPU stall time.
