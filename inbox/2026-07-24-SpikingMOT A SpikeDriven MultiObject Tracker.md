---
title: "SpikingMOT: A Spike-Driven Multi-Object Tracker"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.19875
priority: low
status: unread
interest: medium
next_step: skim
---
# SpikingMOT: A Spike-Driven Multi-Object Tracker
> 原文: [https://arxiv.org/abs/2607.19875](https://arxiv.org/abs/2607.19875)

arXiv:2607.19875v1 Announce Type: new
Abstract: Multi-object tracking (MOT) plays a fundamental role in visual perception, where accurate trajectory prediction is essential for reliable target association under complex motion patterns. Recent trackers have improved motion modeling with densely activated artificial neural networks, yet they largely overlook whether such dense responses are necessary for trajectory prediction. In this paper, we formulate activation sparsity preference (ASP) by tackling two key questions: 1. How can we identify a model architecture that appropriately and formally explains ASP, and 2. How can we translate this explanation into competitive tracking performance. Theoretical analysis shows that sparse gating is no worse than state-independent dropout under the same activation rate. Based on this insight, SpikingMOT is proposed as a spike-driven tracker that adaptively models sparse trajectory dynamics with spiking neural networks (SNNs). Specifically, SpikingMOT decomposes each trajectory state into pseudo-trajectory bases and uses the current prediction error to calibrate the posterior for next-frame prediction. With this brain-inspired loop, SpikingMOT achieves state-of-the-art performance in extensive experiments, 74.9 HOTA on SportsMOT and 56.5 HOTA on DanceTrack, while reducing the parameters and energy by 72% and 86.7%, respectively. These results bring SNNs into MOT, opening a promising direction for efficient tracking.
