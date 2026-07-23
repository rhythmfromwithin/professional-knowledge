---
title: "Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.18631
priority: medium
status: unread
interest: medium
next_step: skim
---
# Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving
> 原文: [https://arxiv.org/abs/2607.18631](https://arxiv.org/abs/2607.18631)

arXiv:2607.18631v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) systems split a program's plan space in two: the space a cost model can rank, and the smaller space a real toolchain can actually build. Automatic optimizers rank the first and silently assume the two coincide -- so they can return a plan that is optimal on paper and impossible to emit. We present moefs, a realizability-aware full-space optimizer for MoE training and serving that makes deployment realizability a first-class search constraint. moefs closes a three-tier search over parallelism, schedule, and kernels; it emits both a Megatron training stack and an SGLang serving stack from a single plan; and it prices, rather than forbids, the realization overheads it measures. We evaluate across two hardware generations. On 2x RTX4090, the searched training plan edges the strongest hand-tuned baseline by +0.9% (and clears the 0.98x acceptance bar by +2.9%); on 8x H800, the searched serving plan matches the hand-tuned configuration at a 1.0304 throughput ratio. We hold failures to the same standard: on 8x H800 training, the searched plan is a computable, honest FAIL at 0.9338 of the best hand-tuned throughput, losing on a single schedule flag. All predictions are pre-registered in a frozen, artifact-hashed adjudication file before the H800 runs, and every outcome is reported as-is.
