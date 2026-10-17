---
interest: medium
link: https://arxiv.org/abs/2610.21264
next_step: skim
priority: low
slack_ts: '1792209645.905109'
source: cs.DB - Databases
status: unread
title: 'AdaBool: Sparse Boolean Matrix Processing with Adaptive Data Representation'
---
# AdaBool: Sparse Boolean Matrix Processing with Adaptive Data Representation
> 原文: [https://arxiv.org/abs/2610.21264](https://arxiv.org/abs/2610.21264)

arXiv:2610.21264v1 Announce Type: new
Abstract: Many data processing tasks revolve around determining whether logical relationships exist between two sets of entities, a pattern that can be naturally modeled as Sparse Boolean Matrix Multiplication (SpBMM). Under Boolean semantics, matrix representations no longer need to store numerical values and instead focus on encoding the positions of non-zero elements, making it highly amenable to data compression for substantially lower memory access overhead. The key challenge, however, is that the most effective compression depends heavily on sparsity distribution: different methods perform best at different sparsity levels, while real-world matrices often contain sharply varying sparsity across regions. Consequently, forcing the entire matrix into any fixed, monolithic representation leaves considerable optimization opportunities untapped.
We present AdaBool, a SpBMM framework designed to reconcile this tension through an adaptive data representation. AdaBool partitions matrices into fine-grained element blocks and represents each block with the encoding best matched to its local sparsity. On top of this adaptive encoding, AdaBool introduces a heterogeneous GPU execution model that groups blocks by encoding type and maps them to matching processing paths, enabling efficient execution and scheduling across GPU resources. We implement AdaBool end to end with low-level system optimizations, evaluate it on both production and public workloads, and show that it outperforms representative baselines by over an order of magnitude.
