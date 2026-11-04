---
title: "EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.03899
priority: medium
status: unread
interest: medium
next_step: skim
---
# EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and RL
> 原文: [https://arxiv.org/abs/2611.03899](https://arxiv.org/abs/2611.03899)

arXiv:2611.03899v1 Announce Type: new
Abstract: Low-rank adapters (LoRA) let one base model serve many fine-tuned variants: multi-tenant engines keep a single copy of the base and batch the requests of many tenants, each with its own adapter. As base models move to 8-bit (FP8) and 4-bit formats, their general matrix multiplications (GEMMs) become cheaper, but the adapters do not: engines run them as separate small GPU kernels beside the GEMM, whose latency takes a growing share of every decoding step. An adapter projects its input down to a low rank and back up, and our key observation is that the GEMM needs the down-projection only in its epilogue, the final stage in which it writes its output. EpiLoRA, a plugin for the vLLM engine, therefore launches the down-projection first and the low-precision GEMM as a dependent kernel that streams its weights meanwhile and adds every tenant's up-projection in its epilogue. On NVIDIA Hopper GPUs, EpiLoRA decodes for a single adapter with up to 24% lower time per token than vLLM's fastest configuration, and faster than SGLang and TensorRT-LLM; with many tenants, its adapter kernels deliver more throughput than vLLM's on most GPU-model pairs we tested. The same low-precision base also trains: a LoRA reinforcement-learning trainer that computes on the engine's FP8 weights needs no 16-bit copy, so a 27B model trains on one 48 GB GPU, and an engine that then keeps activations in 16 bits removes most of the remaining mismatch between the model generating training data and the one trained.
