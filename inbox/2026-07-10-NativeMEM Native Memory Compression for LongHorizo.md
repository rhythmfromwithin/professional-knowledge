---
interest: medium
link: https://arxiv.org/abs/2607.06678
next_step: skim
priority: medium
slack_ts: '1783740349.193269'
source: cs.RO - Robotics
status: unread
title: 'NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation'
---
# NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation
> 原文: [https://arxiv.org/abs/2607.06678](https://arxiv.org/abs/2607.06678)

arXiv:2607.06678v1 Announce Type: new
Abstract: How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA's own vision encoder to compress each historical frame from each camera view into a single token. Appended to the input sequence, these memory tokens enable the pretrained VLA to attend over long-term history with negligible latency overhead, requiring neither an external planner nor a freshly initialized memory module. To align the memory tokens with the pretrained policy, we first develop a generic memory tokenizer under the supervision of a frozen VLA on memory-demanding data, and then unfreeze the VLA for task-specific fine-tuning. NativeMEM consistently outperforms prior methods, boosting success rates from 32.4% to 84.0% in simulation and up to 98.7% on real robots, while maintaining low inference latency and GPU memory usage. Notably, NativeMEM exhibits high data efficiency by achieving competitive results with prior arts using only 20% of the training data.
