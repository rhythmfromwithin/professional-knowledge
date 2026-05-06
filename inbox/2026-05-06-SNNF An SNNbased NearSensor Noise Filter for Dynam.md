---
title: "SNNF: An SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.01937
priority: low
status: unread
interest: medium
next_step: skim
---
# SNNF: An SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors
> 原文: [https://arxiv.org/abs/2605.01937](https://arxiv.org/abs/2605.01937)

arXiv:2605.01937v1 Announce Type: new
Abstract: Dynamic Vision Sensors (DVS) exhibit exceptional dynamic range and low power consumption, making them ideal for edge applications in the Internet of Video Things (IoVT). However, their output is often degraded by spurious Background Activity (BA) noise, leading to unnecessary computational overhead. This paper proposes SNNF, a near-sensor BA noise filter that integrates a compact Event-Based Binary Image (EBBI) representation, a parallel memory architecture, and a single-layer Spiking Neural Network (SNN) classifier. Trained on representative DVS data, the SNN distinguishes signal events from noise with an AUC of 0.89 on standard datasets. The binary-array-based EBBI eliminates timestamp dependency, significantly reducing memory footprint. Moreover, the SNN's spike-based computation replaces power-hungry multipliers with simple accumulation logic and minimizes inter-neuron data width, resulting in an extremely hardware-efficient design. FPGA implementation results show that SNNF reduces memory and logic resources to approximately 11% and 40%, respectively of state-of-the-art filters, while achieving a throughput of 29 Mega events per second (Meps). In a 65 nm CMOS ASIC implementation, SNNF achieves 44.4 Meps with an area and power consumption of only ~13% and <5% of the corresponding ANN-based designs. These results demonstrate that SNNF provides an excellent balance between filtering accuracy and hardware efficiency, making it highly suitable for resource-constrained, near-sensor deployment.
