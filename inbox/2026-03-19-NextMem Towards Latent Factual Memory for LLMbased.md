---
interest: medium
link: https://arxiv.org/abs/2603.15634
next_step: skim
priority: high
slack_ts: '1773888852.500579'
source: cs.AI - Artificial Intelligence
status: unread
title: 'NextMem: Towards Latent Factual Memory for LLM-based Agents'
---
# NextMem: Towards Latent Factual Memory for LLM-based Agents
> 原文: [https://arxiv.org/abs/2603.15634](https://arxiv.org/abs/2603.15634)

arXiv:2603.15634v1 Announce Type: new
Abstract: Memory is critical for LLM-based agents to preserve past observations for future decision-making, where factual memory serves as its foundational part. However, existing approaches to constructing factual memory face several limitations. Textual methods impose heavy context and indexing burdens, while parametric methods suffer from catastrophic forgetting and high costs. To address these challenges, we introduce NextMem, a latent factual memory framework that utilizes an autoregressive autoencoder to efficiently construct latent memory while ensuring accurate reconstruction. For better optimization, we propose a two-stage training process, including autoregressive reconstruction alignment and progressive latent substitution. We also incorporate quantization to reduce storage overhead. Extensive experiments demonstrate that NextMem achieves superior performance, and excels in retrieval, robustness, and extensibility properties. We release our code and model checkpoints at https://github.com/nuster1128/NextMem.
