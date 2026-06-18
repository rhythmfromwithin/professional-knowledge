---
interest: medium
link: https://arxiv.org/abs/2606.18463
next_step: skim
priority: medium
slack_ts: '1781759643.560529'
source: cs.DC - Distributed Computing
status: unread
title: Mixed-Precision Communication-Avoiding SGD for Generalized Linear Models on
  GPUs
---
# Mixed-Precision Communication-Avoiding SGD for Generalized Linear Models on GPUs
> 原文: [https://arxiv.org/abs/2606.18463](https://arxiv.org/abs/2606.18463)

arXiv:2606.18463v1 Announce Type: new
Abstract: Distributed stochastic gradient descent (SGD) is limited by communication rather than computation, since each iteration requires an AllReduce across processes. Communication-avoiding SGD (CA-SGD) amortizes communication over $s$ iterations by replacing $s$ consecutive AllReduces with a single AllReduce of an $sb\times sb$ Gram matrix, trading more computation and bandwidth for fewer synchronization points. Modern GPUs with matrix hardware and reduced-precision formats offset this by accelerating the Gram GEMM and shrinking BF16 traffic. We study mixed-precision CA-SGD for generalized linear models on NVIDIA GPUs. Our finite-precision analysis decomposes the local rounding error of one CA-SGD outer iteration into nine independent precision choices, depending on the hardware only through its low-precision unit roundoffs, so the resulting recipes transfer in principle across GPU generations. The recipe stores the input matrix and margin vector in low precision, computes the Gram matrix from low-precision inputs with high-precision accumulation, communicates it in high precision, and performs the inner recurrence and weight updates in high precision. On NERSC Perlmutter A100 GPUs, mixed-precision CA-SGD matches FP32 SGD loss within $0.5\%$ on logistic, linear, and Poisson problems and reaches $5.1$--$6.8\times$ speedup over FP32 SGD on epsilon, SUSY, HIGGS, synth, and Poisson-synth. Our software is available at https://doi.org/10.5281/zenodo.20448273
