---
interest: medium
link: https://arxiv.org/abs/2609.27189
next_step: skim
priority: medium
slack_ts: '1790310826.664979'
source: cs.DC - Distributed Computing
status: unread
title: 'ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning'
---
# ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning
> 原文: [https://arxiv.org/abs/2609.27189](https://arxiv.org/abs/2609.27189)

arXiv:2609.27189v1 Announce Type: new
Abstract: Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored. Unlike first-order training, ZO progress can be represented by lightweight seed-and-scalar step logs, yet naive log-only recovery still incurs replay cost that grows with training progress, and shortcut replay does not preserve the executed floating-point trajectory. We present ZOCheck, a fault-tolerant ZO training system that exploits this replayable structure through a CPU shadow process that continuously replays logged updates, materializes consistent recovery images off the GPU critical path, and persists them asynchronously. ZOCheck therefore combines non-blocking checkpointing during training with fast recovery from a near-current state. We also develop a cost model for choosing the snapshot policy under realistic failure rates. Experiments show that ZOCheck reduces checkpoint overhead by up to 219.7x and recovery latency by 1.55x on average compared with asynchronous full-state checkpointing, translating into up to 21.3x lower end-to-end wasted time across the evaluated failure rates, while preserving exact recovery behavior.
