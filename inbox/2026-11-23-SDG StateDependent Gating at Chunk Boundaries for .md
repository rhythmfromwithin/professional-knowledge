---
title: "SDG: State-Dependent Gating at Chunk Boundaries for Linear Attention"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.26637
priority: medium
status: unread
interest: medium
next_step: skim
---
# SDG: State-Dependent Gating at Chunk Boundaries for Linear Attention
> 原文: [https://arxiv.org/abs/2611.26637](https://arxiv.org/abs/2611.26637)

arXiv:2611.26637v1 Announce Type: new
Abstract: Recent gated linear attention models use state-independent gates, computed from token representations without directly reading the recurrent memory. This design supports efficient chunkwise computation: sequences are divided into chunks of consecutive tokens, with parallel computation within each chunk. However, the same token representation produces the same gate, even when the layer stores different information. We introduce State-Dependent Gating (SDG), which computes element-wise gates from the change in memory over a chunk and applies them at the chunk boundary. This provides state feedback for forgetting while preserving parallel computation within each chunk. We develop fused kernels for Gated DeltaNet, Kimi Delta Attention, Gated DeltaNet-2, and Mamba-3. Our theoretical analysis quantifies the potential reconstruction benefits of state-dependent, element-wise gating under a signal--noise model. We also show that boundary decay is an element-wise ridge proximal step when the gate is held fixed. Empirical evaluation of 1.3B linear attention and hybrid models trained on 100B tokens shows improvements across language modeling, commonsense reasoning, synthetic and real-world retrieval, and long-context understanding. These results demonstrate that SDG is an effective approach to enhancing existing linear attention models.
