---
interest: medium
link: https://arxiv.org/abs/2610.26987
next_step: skim
priority: medium
slack_ts: '1792556417.420949'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Dynamic Dual-Feedback Conformal Inference for Time Series Forecasting
---
# Dynamic Dual-Feedback Conformal Inference for Time Series Forecasting
> 原文: [https://arxiv.org/abs/2610.26987](https://arxiv.org/abs/2610.26987)

arXiv:2610.26987v1 Announce Type: new
Abstract: Quantifying uncertainty in time series forecasting is particularly demanding because sequential data exhibit temporal dependence and are prone to distributional changes. Conformal inference has emerged as a powerful uncertainty quantification approach through the construction of prediction sets. Recent advances have introduced online conformal methods that adaptively adjust prediction thresholds through feedback mechanisms. However, the existing feedback mechanism typically relies solely on miscoverage indicators (actual feedback), whether the true label falls within the interval at each time step, while overlooking the empirical prediction threshold (estimated feedback) that is derived from the oracle conformal method. In this paper, we propose Dynamic Dual-feedback Conformal Inference (DDCI), which incorporates a dual-feedback mechanism consisting of actual feedback and estimated feedback. The former drives the primary adjustment of the intervals based on true observations, while the latter dampens excessive expansions or contractions by leveraging empirical thresholds from conformal inference during updates. By balancing these two signals, DDCI achieves more stable and narrower prediction intervals in sequential settings while maintaining near-nominal coverage in practice.
