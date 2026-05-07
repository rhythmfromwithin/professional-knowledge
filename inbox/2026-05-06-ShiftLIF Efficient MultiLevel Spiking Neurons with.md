---
interest: medium
link: https://arxiv.org/abs/2605.01866
next_step: skim
priority: low
slack_ts: '1778125806.652439'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization'
---
# ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization
> 原文: [https://arxiv.org/abs/2605.01866](https://arxiv.org/abs/2605.01866)

arXiv:2605.01866v1 Announce Type: new
Abstract: Spiking neural networks (SNNs) are promising for edge sensing due to their event-driven computation and temporal filtering capability. However, standard leaky integrate-and-fire (LIF) neurons communicate only through binary spikes, which severely limit representational capacity. Existing multi-level spiking neurons improve information transmission, but often rely on uniform quantization that mismatches membrane-potential distributions or introduces costly synaptic multiplications. In this paper, we propose ShiftLIF, a multi-level spiking neuron that maps membrane potentials to a logarithmically spaced power-of-two spike set. This design provides finer representation in the small-amplitude regime, where membrane potentials are densely concentrated, while enabling multiplier-free synaptic computation through bit-shift and accumulation operations. As a result, ShiftLIF improves spike-level expressiveness without sacrificing the hardware-friendly nature of standard SNN computation. We evaluate ShiftLIF on 10 datasets spanning wireless, acoustic, motion, and visual sensing tasks. Results show that ShiftLIF consistently matches or exceeds the accuracy of existing multi-level spiking neurons while maintaining synaptic energy consumption close to standard binary LIF. These results indicate that ShiftLIF provides a favorable accuracy-efficiency trade-off for cross-modal edge sensing.
