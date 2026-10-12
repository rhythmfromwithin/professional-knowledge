---
title: "Execution-Feasible Dispatch of LLM Pre-training Loads for Renewable-Dominant AI Data Centers"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.13047
priority: medium
status: unread
interest: medium
next_step: skim
---
# Execution-Feasible Dispatch of LLM Pre-training Loads for Renewable-Dominant AI Data Centers
> 原文: [https://arxiv.org/abs/2610.13047](https://arxiv.org/abs/2610.13047)

arXiv:2610.13047v1 Announce Type: new
Abstract: AI data centers (AIDCs) are emerging as large power-system loads, making their operational flexibility increasingly valuable. Existing studies often treat AIDC demand as continuously adjustable or generically delay-tolerant, which overstating the flexibility of large language model (LLM) pretraining. This paper proposes an execution-feasible dispatch framework for LLM pre-training in renewable-dominant AIDCs. LLM descriptors are first converted into checkpoint-domain daily workloads, then mapped to feasible 3D-parallel GPU modes with explicit throughput, GPU-capacity, memory, and IT-power limits. The resulting checkpoint- and mode-constrained load states are embedded into a day-ahead power dispatch model. Case studies on a 2048 GPUs AIDC with two LLaMA pretraining tasks show that checkpoint-aware 3D dispatch reduces operating cost by 20.02% and renewable curtailment from 1.077 to 0.014 MWh relative to fixed continuous training. Related results also show that checkpoint records alone do not create load flexibility,practical grid-interactive flexibility arises from checkpoint waiting combined with execution-feasible 3D-mode compensation.
