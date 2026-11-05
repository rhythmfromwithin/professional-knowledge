---
interest: medium
link: https://arxiv.org/abs/2611.03875
next_step: skim
priority: medium
slack_ts: '1793859286.614259'
source: cs.DC - Distributed Computing
status: unread
title: 'INSIGHT-HPC: An Interpretable System Intelligence for Global HPC Telemetry'
---
# INSIGHT-HPC: An Interpretable System Intelligence for Global HPC Telemetry
> 原文: [https://arxiv.org/abs/2611.03875](https://arxiv.org/abs/2611.03875)

arXiv:2611.03875v1 Announce Type: new
Abstract: Modern high-performance computing (HPC) clusters integrate multi-generation CPUs and GPUs, which generate rich, high-dimensional telemetry streams from out-of-band baseboard management controllers (BMC), job schedulers, and facility power distribution units. Detecting anomalies within this telemetry is critical to prevent energy waste and costly node failures. Existing approaches often rely primarily on statistical deviations and require stronger labels than actual production environments can provide. In addition, these detectors have a limited operational context for interpreting alerts. We present INSIGHT-HPC, a multi-plane anomaly-detection architecture that combines statistical, workload-aware, and physics-guided evidence into operator-interpretable episodes. INSIGHT-HPC integrates heterogeneous, large-scale telemetry streams and transforms noisy minute-resolution observations into de-duplicated fault episodes with operator-facing explanations. This design allows the system to distinguish workload-explained behavior from genuine infrastructure anomalies while producing interpretable alert summaries for operators. On production HPC telemetry with weak operational labels and controlled HPC-relevant fault injections, INSIGHT-HPC achieves a stronger precision-recall balance than all evaluated baselines. The system achieves a precision of 0.913, a recall of 0.817, an F1 score of 0.862, and an AUROC of 0.896. These results demonstrate the value of combining workload context, physical consistency, and explainable episode-level fusion.
