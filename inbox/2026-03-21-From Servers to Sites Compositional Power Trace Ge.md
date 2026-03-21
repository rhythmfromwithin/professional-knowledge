---
title: "From Servers to Sites: Compositional Power Trace Generation of LLM Inference for Infrastructure Planning"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.18383
priority: medium
status: unread
interest: medium
next_step: skim
---
# From Servers to Sites: Compositional Power Trace Generation of LLM Inference for Infrastructure Planning
> 原文: [https://arxiv.org/abs/2603.18383](https://arxiv.org/abs/2603.18383)

arXiv:2603.18383v1 Announce Type: new
Abstract: Datacenter operators and electrical utilities rely on power traces at different spatiotemporal scales. Operators use fine-grained traces for provisioning, facility management, and scheduling, while utilities use site-level load profiles for capacity and interconnection planning. Existing datacenter power models do not capture LLM inference workloads, in which GPUs shift rapidly among compute-intensive prefill, lower-power decode, and idle states, and facility demand depends on how these states evolve and synchronize across many devices. We show that LLM inference power can be represented compositionally through two components: workload-driven transitions among operating states and configuration-specific power distributions within those states. Building on this observation, we develop a trace-generation framework that learns from measured traces and synthesizes power profiles for new traffic conditions and serving configurations. These traces aggregate from GPU servers to rack-, row-, and facility-scale load profiles at the temporal granularity required by the study.
Across multiple LLMs, tensor-parallel settings, and GPU generations, our framework achieves median absolute energy error below 5% for most configurations while preserving temporal autocorrelation structure. The resulting traces support downstream analyses including oversubscription, power modulation, and utility-facing load characterization, enabling infrastructure evaluations that flat nameplate assumptions and static trace replay cannot support.
