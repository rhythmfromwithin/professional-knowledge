---
interest: medium
link: https://arxiv.org/abs/2604.22072
next_step: skim
priority: medium
slack_ts: '1777434584.851149'
source: cs.DC - Distributed Computing
status: unread
title: 'Shard the Gradient, Scale the Model: Serverless Federated Aggregation via
  Gradient Partitioning'
---
# Shard the Gradient, Scale the Model: Serverless Federated Aggregation via Gradient Partitioning
> 原文: [https://arxiv.org/abs/2604.22072](https://arxiv.org/abs/2604.22072)

arXiv:2604.22072v1 Announce Type: new
Abstract: Federated learning (FL) aggregation on serverless platforms faces a hard scalability ceiling: existing architectures (lambda-FL, LIFL) partition clients across aggregators, but every aggregator must hold the complete model gradient in memory. When gradients exceed the per-function memory limit (e.g., 10 GB on AWS Lambda), aggregation becomes infeasible regardless of tree depth or branching factor. We propose GradsSharding, which instead partitions the gradient tensor into M shards, each averaged independently by a serverless function that receives contributions from all clients. Because FedAvg averaging is element-wise, this produces bit-identical results to tree-based approaches, so model accuracy is invariant by construction. Per-function memory is bounded at O(|{\theta}|/M), independent of client count, enabling aggregation of arbitrarily large models. We evaluate GradsSharding against lambda-FL and LIFL through HPC experiments and real AWS Lambda deployments across model sizes from 43 MB to 5 GB. Results show a cost crossover at approximately 500 MB gradient size, 2.7x cost reduction at VGG-16 scale, and that GradsSharding is the only architecture that remains deployable beyond the serverless memory ceiling.
