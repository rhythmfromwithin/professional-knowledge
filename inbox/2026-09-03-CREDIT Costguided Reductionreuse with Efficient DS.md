---
interest: medium
link: https://arxiv.org/abs/2609.01864
next_step: skim
priority: medium
slack_ts: '1788408238.538719'
source: cs.DC - Distributed Computing
status: unread
title: 'CREDIT: Cost-guided Reduction-reuse with Efficient DSMEM Inter-CTA Tiling'
---
# CREDIT: Cost-guided Reduction-reuse with Efficient DSMEM Inter-CTA Tiling
> 原文: [https://arxiv.org/abs/2609.01864](https://arxiv.org/abs/2609.01864)

arXiv:2609.01864v1 Announce Type: new
Abstract: NVIDIA distributed shared memory (DSMEM) enables direct shared-memory access within a thread block cluster. However, cluster synchronization, remote access, and resource costs make it difficult to determine when DSMEM improves performance. To fill this gap, we propose CREDIT, a cost-guided framework that identifies DSMEM-profitable workload patterns, predicts their profitability range, and delivers consistent speedups across diverse workloads. CREDIT combines three innovations: (1) a profiling-driven characterization that identifies workload patterns likely to benefit from DSMEM; (2) a transformation that applies DSMEM to reduction-reuse workloads; (3) a cost model based on profiling data, to determine its profitability range. Evaluations on diverse workloads show CREDIT achieves 91.7% prediction accuracy on profitability. CREDIT beats torch.compile, Triton, and optimized non-DSMEM CUDA baselines on all six workloads, with geometric-mean speedups of 1.466x on RTX 5090 and 1.318x on H100. CREDIT's source code is publicly available at https://github.com/zhengxiongli08/CREDIT.
