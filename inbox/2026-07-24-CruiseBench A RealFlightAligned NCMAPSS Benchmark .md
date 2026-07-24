---
title: "CruiseBench: A Real-Flight-Aligned N-CMAPSS Benchmark for Engine RUL Prediction"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.19380
priority: high
status: unread
interest: medium
next_step: skim
---
# CruiseBench: A Real-Flight-Aligned N-CMAPSS Benchmark for Engine RUL Prediction
> 原文: [https://arxiv.org/abs/2607.19380](https://arxiv.org/abs/2607.19380)

arXiv:2607.19380v1 Announce Type: new
Abstract: Remaining useful life (RUL) prediction estimates how long an engine can continue safe operation and is central to maintenance planning. N-CMAPSS extends C-MAPSS by simulating run-to-failure aero-engine trajectories using recorded real-flight profiles and retaining complete within-flight time series rather than cycle-level snapshots. However, this added realism reduces evaluation control because full-flight records increase data volume and entangle degradation cues with operating-regime variation, complicating preprocessing choices and direct comparisons of RUL modeling performance. To mitigate this issue, this paper proposes CruiseBench, a cruise-stage RUL benchmark derived from N-CMAPSS. It introduces CPM-N-CMAPSS (Cruising-Period Mask for N-CMAPSS), a mask artifact that stores cycle-local cruising intervals identified by the common-altitude method for the nine accessible subdatasets. CruiseBench applies a fixed protocol to the masked rows, using scenario descriptors and measured sensors as inputs while excluding virtual sensors, health parameters, and auxiliary metadata from the feature tensor, preserving native-resolution windows, and applying dataset-wise RUL caps. Experiments with LSTM, GRU, TCN, and TSMixer provide baseline results for this setting. Under CruiseBench-eta5-W256-S10, TSMixer obtains the lowest average RMSE, $3.4\pm1.71$, and Saxena score, $(2.50\pm2.99)\times 10^{4}$. Ablation studies show that flight-stage selection, temporal downscaling method, and RUL-cap threshold affect reported results. With its fixed cruise-stage protocol, CruiseBench provides a reproducible sub-benchmark for controlled RUL model comparison and CPM-N-CMAPSS provides a stage-specific data foundation for future transfer-learning and domain-adaptation studies.
