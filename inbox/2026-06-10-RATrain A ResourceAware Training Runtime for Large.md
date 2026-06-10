---
interest: medium
link: https://arxiv.org/abs/2606.10415
next_step: skim
priority: medium
slack_ts: '1781065411.323719'
source: cs.DC - Distributed Computing
status: unread
title: 'RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained
  Heterogeneous Supercomputing Platforms'
---
# RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms
> 原文: [https://arxiv.org/abs/2606.10415](https://arxiv.org/abs/2606.10415)

arXiv:2606.10415v1 Announce Type: new
Abstract: Production heterogeneous supercomputing platforms are increasingly used to host large language model (LLM) training workloads. However, existing GPU-oriented training runtimes typically rely on high-bandwidth device memory, fast interconnects, and mature collective communication libraries, making them difficult to directly adapt to MT-3000, a platform with an explicit memory hierarchy, limited usable DDR capacity, and constrained inter-cluster communication. This paper presents RATrain, a resource-aware training runtime for dense LLMs on bandwidth-constrained heterogeneous supercomputing platforms. RATrain formulates standard non-interleaved 1F1B training as a training-state lifecycle scheduling problem, and schedules gradient synchronization, parameter update, parameter-view prefetching, and activation recovery at layer-level and stage-local granularity. RATrain further combines an MT-3000-aware execution backend for efficient and predictable FP16 GEMM, Attention Backward, and explicit data movement with a resource-aware planner that selects feasible training configurations under the 20GB usable-DDR constraint per compute cluster. We implement RATrain on a real MT-3000 platform and evaluate it using LLaMA-2-7B, Baichuan2-13B, Qwen2.5-32B, and LLaMA-2-70B configurations. Results show that RATrain achieves up to 1.35$\times$ end-to-end speedup over MT-3000-adapted GPU-style training strategies. For LLaMA-2-7B, RATrain scales to 1024 compute clusters, reaches 112,790.55 tokens/s, and achieves 97.0\% scaling efficiency. A further 1.028B-token correctness run shows that RATrain preserves the loss trajectory of a semantically equivalent Baseline-1F1B run, with a maximum relative loss deviation of 0.081\%.
