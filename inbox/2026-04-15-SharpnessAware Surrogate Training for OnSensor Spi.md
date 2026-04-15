---
title: "Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2604.09696
priority: low
status: unread
interest: medium
next_step: skim
---
# Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2604.09696](https://arxiv.org/abs/2604.09696)

arXiv:2604.09696v1 Announce Type: new
Abstract: Spiking neural networks (SNNs) are a natural computational model for on-sensor and near-sensor vision, where event driven processors must operate under strict power budgets with hard binary spikes. However, models trained with surrogate gradients often degrade sharply when the smooth surrogate nonlinearity is replaced by a hard threshold at deployment; a surrogate-to-hard transfer gap that directly limits on-sensor accuracy. We study Sharpness-Aware Surrogate Training (SAST), which applies Sharpness-Aware Minimization (SAM) to a surrogate-forward SNN so that the training objective is smooth and the gradient is exact, and position it as one gap-reduction strategy under the tested settings rather than the only viable mechanism. Under explicit contraction assumptions we provide state-stability, input-Lipschitz, and smoothness bounds, together with a corresponding nonconvex convergence result. On two event-camera benchmarks, swap-only hard-spike accuracy improves from 65.7\% to 94.7\% on N-MNIST and from 31.8\% to 63.3\% on DVS Gesture. Under a hardware-aware inference simulation (INT8/INT4 weight quantization, fixed-point membrane potentials, discrete leak factors), SAST remains strong: on N-MNIST, hard-spike accuracy improves from 47.6\% to 96.9\% (INT8) and from 43.2\% to 81.0\% (INT4), while on DVS Gesture it improves from 25.3\% to 47.6\% (INT8) and from 26.0\% to 43.8\% (INT4). SynOps also decrease under the same hardware-aware setting, including 1734k$\rightarrow$1315k (N-MNIST, INT8) and 86221k$\rightarrow$4323k (DVS Gesture, INT8). These results suggest that SAST is a promising component in a broader toolbox for on-sensor spiking inference under the tested settings.
