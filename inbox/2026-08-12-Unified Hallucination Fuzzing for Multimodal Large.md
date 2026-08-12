---
title: "Unified Hallucination Fuzzing for Multimodal Large Language Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.07525
priority: high
status: unread
interest: medium
next_step: skim
---
# Unified Hallucination Fuzzing for Multimodal Large Language Models
> 原文: [https://arxiv.org/abs/2608.07525](https://arxiv.org/abs/2608.07525)

arXiv:2608.07525v1 Announce Type: new
Abstract: Hallucination remains a persistent challenge for Multimodal Large Language Models (MLLMs), severely limiting their reliability in high-stakes applications. Existing evaluations, predominantly based on static benchmarks, suffer from narrow taxonomical coverage and rapid performance saturation, failing to reflect model robustness in evolving real-world scenarios. To bridge this gap, we present a systematic evaluation framework integrating a comprehensive benchmark with self-evolving stress testing. First, we introduce UniHall, a fine-grained dataset grounded in a unified taxonomy spanning Object, Instruction, and Knowledge dimensions. Second, to address benchmark saturation, we propose Self-Adaptive Multimodal Fuzzing (SAMF), a self-adaptive framework that employs evolutionary mutation strategies to explore the boundaries of model hallucinations. Crucially, to ensure reliable assessment of dynamic inputs, SAMF incorporates a structured metric suite driven by an ensemble of multi-modal oracles. Our extensive experiments reveal that state-of-the-art MLLMs exhibit significant performance degradation under fuzzing compared to conventional settings, exposing a dissociation between reasoning capabilities and factual grounding. Furthermore, we identify a helpfulness-hallucination trade-off, where reinforcement learning alignment inadvertently exacerbates sycophancy in instruction-following tasks. The framework, code and benchmark are available at https://github.com/LanceZPF/EvalHall.
