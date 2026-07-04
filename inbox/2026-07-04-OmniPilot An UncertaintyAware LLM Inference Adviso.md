---
interest: medium
link: https://arxiv.org/abs/2607.01579
next_step: skim
priority: medium
slack_ts: '1783136973.440959'
source: cs.DC - Distributed Computing
status: unread
title: 'OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU
  Clusters'
---
# OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters
> 原文: [https://arxiv.org/abs/2607.01579](https://arxiv.org/abs/2607.01579)

arXiv:2607.01579v1 Announce Type: new
Abstract: Serving large language models (LLMs) on a shared, heterogeneous GPU cluster requires users and operators to select the GPU type, tensor-parallel degree, and precision before committing valuable node-hours. Making these choices is challenging because effective throughput, launch-success rates, and cluster demand and utilization continuously fluctuate. Furthermore, static configuration recipes miss critical interactions: quantization effects depend heavily on the model family, key-value cache pressure creates size-by-precision trade-offs, and failure rates vary by more than twofold across different tensor-parallel degrees. Additionally, cluster resources are frequently constrained by unpredictable hardware failures. To address these challenges, we present \textbf{OmniPilot}, a launch advisor that predicts serving costs for feasible configurations and abstains when requests fall outside its measured support envelope. OmniPilot pairs a conformally calibrated quantile cost model (spanning eight serving targets) with an out-of-distribution (OOD) abstention layer. It ranks configurations using an economic utility metric calibrated to an operator's revealed preferences. In evaluations across 460 benchmark runs on A100, H100, and H200 hardware across four precisions, OmniPilot predicts aggregate throughput with a 6.2\% mean absolute percentage error (MAPE) and a log-space $R^2=0.92$. The advisor achieves 95\% top-1 accuracy with a mean utility regret of just 0.003. When tested on an OOD holdout of unsupported cells, prediction error climbs to 24-46\% and conformal intervals cover 0 of 5 points; however, the abstention layer successfully flags all five as low-confidence. Over time, these OOD scenarios will be integrated into the training dataset to continuously expand the advisor's support envelope.
