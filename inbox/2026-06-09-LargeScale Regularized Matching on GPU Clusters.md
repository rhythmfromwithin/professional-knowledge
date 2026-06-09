---
interest: medium
link: https://arxiv.org/abs/2606.07777
next_step: skim
priority: medium
slack_ts: '1780978311.182969'
source: cs.DC - Distributed Computing
status: unread
title: Large-Scale Regularized Matching on GPU Clusters
---
# Large-Scale Regularized Matching on GPU Clusters
> 原文: [https://arxiv.org/abs/2606.07777](https://arxiv.org/abs/2606.07777)

arXiv:2606.07777v1 Announce Type: new
Abstract: Production decision systems such as ad allocation or content matching involve millions of users and thousands of items, reducing to large-scale linear programs with sparse block-diagonal structure across users. These LPs are solved repeatedly on recurring cadences over slowly evolving inputs. Three system gaps stand out. Scale: production instances routinely exceed the memory capacity of GPU solvers such as cuPDLP and D-PDLP under fixed hardware budgets. Temporal instability: solution variability across runs induces downstream churn and complicates SLAs, yet existing solvers provide no explicit control. Extensibility: CPU-based solvers such as DuaLip-Scala converge slowly and couple problem formulation to fixed schemas, making new constraint families difficult to express. We present a distributed multi-GPU LP solver built natively in PyTorch with systems-algorithm co-design for this structure. It adopts column-sharded parallelism with fused Triton kernels and batched operations to reduce per-iteration overhead. As users grow, only local computation increases, while communication is limited to a reduction of item-level dual variables, yielding near-linear scaling with GPU count at fixed item size. We also adopt ridge-regularized LPs to improve stability, a control absent from existing GPU solvers. A continuation schedule over the regularization parameter balances convergence speed and solution fidelity. Finally, we introduce an operator-centric programming model that replaces DuaLip-Scala's schema-bound interface with composable primitives, enabling new formulations without modifying the solve loop or distributed infrastructure. On synthetic workloads, our system achieves order-of-magnitude wall-clock speedup over DuaLip-Scala, near-linear multi-GPU scaling (3.86x on 4 GPUs), and scales beyond the reach of existing GPU solvers.
