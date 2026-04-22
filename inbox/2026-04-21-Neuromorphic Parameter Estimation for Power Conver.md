---
interest: medium
link: https://arxiv.org/abs/2604.15714
next_step: skim
priority: low
slack_ts: '1776828590.726999'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using
  Spiking Neural Networks
---
# Neuromorphic Parameter Estimation for Power Converter Health Monitoring Using Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2604.15714](https://arxiv.org/abs/2604.15714)

arXiv:2604.15714v1 Announce Type: new
Abstract: Always-on converter health monitoring demands sub-mW edge inference, a regime inaccessible to GPU-based physics-informed neural networks. This work separates spiking temporal processing from physics enforcement: a three-layer leaky integrate-and-fire SNN estimates passive component parameters while a differentiable ODE solver provides physics-consistent training by decoupling the ODE physics loss from the unrolled spiking loop. On an EMI-corrupted synchronous buck converter benchmark, the SNN reduces lumped resistance error from $25.8\%$ to $10.2\%$ versus a feedforward baseline, within the $\pm 10\%$ manufacturing tolerance of passive components, at a projected ${\sim}270\times$ energy reduction on neuromorphic hardware. Persistent membrane states further enable degradation tracking and event-driven fault detection via a $+5.5$ percentage-point spike-rate jump at abrupt faults. With $93\%$ spike sparsity, the architecture is suited for always-on deployment on Intel Loihi 2 or BrainChip Akida.
