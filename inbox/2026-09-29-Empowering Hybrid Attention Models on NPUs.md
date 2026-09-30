---
interest: medium
link: https://arxiv.org/abs/2609.32114
next_step: skim
priority: medium
slack_ts: '1790745128.337229'
source: cs.DC - Distributed Computing
status: unread
title: Empowering Hybrid Attention Models on NPUs
---
# Empowering Hybrid Attention Models on NPUs
> 原文: [https://arxiv.org/abs/2609.32114](https://arxiv.org/abs/2609.32114)

arXiv:2609.32114v1 Announce Type: new
Abstract: Hybrid attention models have emerged as a crucial architecture for Large Language Models (LLMs) (e.g., the Qwen3.5 and Kimi series). Their memory and computational efficiency make them highly attractive for on-device inference, forming a promising synergy with edge Neural Processing Units (NPUs). However, naive execution of these hybrid models on edge NPUs fails to deliver these benefits, often bottlenecking the prefill stage due to severe memory-system inefficiencies and architectural mismatches within the linear attention (LA) layers. We present HA-NPU, the first system to enable efficient hybrid attention LLM inference on edge NPUs without modifying the underlying algorithms. HA-NPU enhances execution efficiency by reorganizing the dataflow of the LA components across three levels: (1) At the core level, it partitions workloads by the head dimension and fuses dependent operators, eliminating cross-core global memory accesses; (2) At the operator level, it reorders execution to consume intermediate tensors immediately, drastically minimizing local-buffer pressure; (3) At the tensor level, it employs dataflow-aware layout planning to minimize transformation overhead between matrix and vector processing units. Compared to competitive baselines, HA-NPU achieves up to 35.95$\times$ LA kernel speedup and 36.14$\times$ energy reduction, delivering up to 2.03$\times$ faster end-to-end request latency. The source code will be made publicly available at https://github.com/yinyuanzhang/HA-NPU
