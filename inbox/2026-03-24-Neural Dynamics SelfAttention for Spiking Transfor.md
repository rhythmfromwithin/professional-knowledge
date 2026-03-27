---
interest: medium
link: https://arxiv.org/abs/2603.19290
next_step: skim
priority: low
slack_ts: '1774581533.853549'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Neural Dynamics Self-Attention for Spiking Transformers
---
# Neural Dynamics Self-Attention for Spiking Transformers
> 原文: [https://arxiv.org/abs/2603.19290](https://arxiv.org/abs/2603.19290)

arXiv:2603.19290v1 Announce Type: new
Abstract: Integrating Spiking Neural Networks (SNNs) with Transformer architectures offers a promising pathway to balance energy efficiency and performance, particularly for edge vision applications. However, existing Spiking Transformers face two critical challenges: (i) a substantial performance gap compared to their Artificial Neural Networks (ANNs) counterparts and (ii) high memory overhead during inference. Through theoretical analysis, we attribute both limitations to the Spiking Self-Attention (SSA) mechanism: the lack of locality bias and the need to store large attention matrices. Inspired by the localized receptive fields (LRF) and membrane-potential dynamics of biological visual neurons, we propose LRF-Dyn, which uses spiking neurons with localized receptive fields to compute attention while reducing memory requirements. Specifically, we introduce a LRF method into SSA to assign higher weights to neighboring regions, strengthening local modeling and improving performance. Building on this, we approximate the resulting attention computation via charge-fire-reset dynamics, eliminating explicit attention-matrix storage and reducing inference-time memory. Extensive experiments on visual tasks confirm that our method reduces memory overhead while delivering significant performance improvements. These results establish it as a key unit for achieving energy-efficient Spiking Transformers.
