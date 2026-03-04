---
title: "StaTS: Spectral Trajectory Schedule Learning for Adaptive Time Series Forecasting with Frequency Guided Denoiser"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.00037
priority: high
status: unread
---
# StaTS: Spectral Trajectory Schedule Learning for Adaptive Time Series Forecasting with Frequency Guided Denoiser
> 原文: [https://arxiv.org/abs/2603.00037](https://arxiv.org/abs/2603.00037)

arXiv:2603.00037v1 Announce Type: new
Abstract: Diffusion models have been used for probabilistic time series forecasting and show strong potential. However, fixed noise schedules often produce intermediate states that are hard to invert and a terminal state that deviates from the near noise assumption. Meanwhile, prior methods rely on time domain conditioning and seldom model schedule induced spectral degradation, which limits structure recovery across noise levels. We propose StaTS, a diffusion model for probabilistic time series forecasting that learns the noise schedule and the denoiser through alternating updates. StaTS includes Spectral Trajectory Scheduler (STS) that learns a data adaptive noise schedule with spectral regularization to improve structural preservation and stepwise invertibility, and Frequency Guided Denoiser (FGD) that estimates schedule induced spectral distortion and uses it to modulate denoising strength for heterogeneous restoration across diffusion steps and variables. A two stage training procedure stabilizes the coupling between schedule learning and denoiser optimization. Experiments on multiple real world benchmarks show consistent gains, while maintaining strong performance with fewer sampling steps. Our code is available at https://github.com/zjt-gpu/StaTS/.
