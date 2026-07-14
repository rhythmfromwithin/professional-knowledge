---
interest: medium
link: https://arxiv.org/abs/2607.08973
next_step: skim
priority: medium
slack_ts: '1783998920.149869'
source: cs.DC - Distributed Computing
status: unread
title: 'SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference'
---
# SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference
> 原文: [https://arxiv.org/abs/2607.08973](https://arxiv.org/abs/2607.08973)

arXiv:2607.08973v1 Announce Type: new
Abstract: The rise of reasoning models and agentic systems has made LLM token-generation latency a key bottleneck. Unlike chatbots, whose latency gains saturate at human reading speed, these systems generate intermediate reasoning tokens not consumed by humans. Thus, per-token latency directly determines end-to-end response time. Low-latency inference uses minimal batching, making token generation bandwidth-bound. Tensor Parallelism addresses this by sharding model weights across GPUs and loading them in parallel. However, scaling to more GPUs introduces All-Reduce overheads that grow with GPU count. Removing All-Reduce improves token throughput by 43% for Llama-3.1-8B on 8 H200 GPUs.
We propose Synchronization-Free All-Reduce (SiFAR), which reduces synchronization overhead during low-latency inference. Existing oneshot and twoshot algorithms incur overheads from barriers before and after communication. First, we find that the bottom barrier in oneshot enforces a WAW dependency and eliminate it by co-designing communication and model execution to enable dual buffering. However, oneshot scales poorly with GPU count. Twoshot performs better at higher TP degrees but incurs an unavoidable bottom barrier. To overcome this, we leverage in-switch reduction in modern switches. We propose redundant pull, where each GPU reduces the full All-Reduce payload at the switch. This improves oneshot scalability while retaining its no-bottom-barrier advantage. Finally, to reduce top-barrier overhead, we observe that each decode step issues multiple All-Reduce operations, keeping GPUs tightly synchronized after the first. We therefore propose speculative reduction, which initiates data transfer before the top barrier and ensures correctness via lightweight validation. SiFAR reduces All-Reduce latency by up to 52% and improves end-to-end throughput by 18.6% for Llama-3.1-8B and 13.1% for Qwen3.5-397B-17B at TP=8.
