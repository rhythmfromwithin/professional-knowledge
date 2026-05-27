---
interest: medium
link: https://arxiv.org/abs/2605.22864
next_step: skim
priority: high
slack_ts: '1779856025.241919'
source: cs.LG - Machine Learning
status: unread
title: Reading Calibrated Uncertainty from Language Model Trajectories
---
# Reading Calibrated Uncertainty from Language Model Trajectories
> 原文: [https://arxiv.org/abs/2605.22864](https://arxiv.org/abs/2605.22864)

arXiv:2605.22864v1 Announce Type: new
Abstract: The maximum softmax probability (MSP) represents a default approach when evaluating uncertainty quantification for language model generation with structured output. Although cheap, it is often miscalibrated. Methods that probe the model's internal activations feed raw hidden states into opaque classifiers, reading activations as static snapshots and leaving implicit the layer-wise trajectory by which a representation is formed. Yet, similar endpoints can arise from very different paths, and how evidence accumulates, reinforces, or reverses across depth might reveal uncertainty that final probabilities obscure. We extract eleven scale-invariant geometric features, tracing the cumulative path of per-layer MLP updates, and feed them to a sparse linear probe. The probe outperforms MSP under selective abstention, with gains scaling with baseline miscalibration up to 21 AURC points. Because every feature has a closed-form geometric meaning, the probe's coefficients trace how and where along depth errors take shape -- which layers commit prematurely, which contradict the running state, where trajectories drift away from their endpoint.
