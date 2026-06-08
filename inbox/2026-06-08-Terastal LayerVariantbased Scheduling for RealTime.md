---
title: "Terastal: Layer-Variant-based Scheduling for Real-Time Multi-DNN Workloads on Heterogeneous Accelerators"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.06818
priority: medium
status: unread
interest: medium
next_step: skim
---
# Terastal: Layer-Variant-based Scheduling for Real-Time Multi-DNN Workloads on Heterogeneous Accelerators
> 原文: [https://arxiv.org/abs/2606.06818](https://arxiv.org/abs/2606.06818)

arXiv:2606.06818v1 Announce Type: new
Abstract: Heterogeneous DNN accelerators improve soft real-time multi-DNN execution by mapping each layer to its preferred accelerator to reduce latency. However, under skewed workloads, large layer-latency differences across accelerators limit scheduling flexibility and increase deadline misses. To address this challenge, we introduce layer variants, customized layer implementations that reduce latency gaps on non-preferred accelerators. We then present Terastal, a soft real-time framework for layer-variant design and scheduling on heterogeneous DNN accelerators. Terastal combines offline heterogeneity-aware virtual budget assignment and layer-variant design, and online scheduling to jointly optimize accelerator mapping and variant selection under timing and accuracy constraints. Experimental results show that Terastal reduces deadline miss rate per model by 40.58%, 30.53%, and 36.27% compared with FCFS, EDF, and DREAM, respectively, while incurring only 2.24% average normalized accuracy loss across models with variants.
