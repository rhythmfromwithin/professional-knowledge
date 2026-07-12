---
interest: medium
link: https://arxiv.org/abs/2607.08215
next_step: skim
priority: medium
slack_ts: '1783827431.902869'
source: cs.DC - Distributed Computing
status: unread
title: 'On the Limitations of Non-GPU AI Accelerators for Large-Model Inference: A
  Field Study of MoE and Multimodal Serving on Huawei Ascend'
---
# On the Limitations of Non-GPU AI Accelerators for Large-Model Inference: A Field Study of MoE and Multimodal Serving on Huawei Ascend
> 原文: [https://arxiv.org/abs/2607.08215](https://arxiv.org/abs/2607.08215)

arXiv:2607.08215v1 Announce Type: new
Abstract: Non-GPU AI accelerators are increasingly adopted as alternatives to general-purpose GPUs for large-model inference, but the real engineering cost of migrating demanding workloads beyond CUDA remains poorly documented. We present a field study of deploying two large inference workloads on a 16-device Huawei Ascend 910 system using CANN and vLLM-Ascend: an LLM-as-a-judge safety and alignment evaluation pipeline based on a W8A8 MoE judge model, DeepSeek-V4-Flash, and a multimodal medical vision--language benchmark based on DeepSeek-V4-Flash-Vision for MMMU and MMMU-Pro. Making these workloads reliable required twelve source-level patches to the vendor inference plugin, disabling several high-throughput features to preserve numerical correctness, and adding operational safeguards for recurring device-level failures. We summarize the main platform limitations in eight categories: incomplete operator and feature support, fragile parallelism, numerical faults in low-level kernels, immature graph compilation, unstable advanced features, limited scalability, weak observability, and ecosystem fragmentation. For each category, we report the symptoms, evidence, and likely causes. We also quantify the integration effort, concurrency behavior, and benchmark quality to show that both workloads were served correctly. Our study provides a reproducible reference for teams evaluating or operating non-GPU accelerators for large-model inference.
