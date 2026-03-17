---
interest: medium
link: https://arxiv.org/abs/2603.12739
next_step: skim
priority: low
slack_ts: '1773715549.565509'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks
---
# SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2603.12739](https://arxiv.org/abs/2603.12739)

arXiv:2603.12739v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) have emerged as a biologically inspired alternative to conventional deep networks, offering event-driven and energy-efficient computation. However, their throughput remains constrained by the serial update of neuron membrane states. While many hardware accelerators and Compute-in-Memory (CIM) architectures efficiently parallelize the synaptic operation (W x I) achieving O(1) complexity for matrix-vector multiplication, the subsequent state update step still requires O(N) time to refresh all neuron membrane potentials. This mismatch makes state update the dominant latency and energy bottleneck in SNN inference. To address this challenge, we propose an SRAM-based CIM for SNN with Linear Decay Leaky Integrate-and-Fire (LD-LIF) Neuron that co-optimizes algorithm and hardware. At the algorithmic level, we replace the conventional exponential membrane decay with a linear decay approximation, converting costly multiplications into simple additions while accuracy drops only around 1%. At the architectural level, we introduce an in-memory parallel update scheme that performs in-place decay directly within the SRAM array, eliminating the need for global sequential updates. Evaluated on benchmark SNN workloads, the proposed method achieves a 1.1 x to 16.7 x reduction of SOP energy consumption, while providing 15.9 x to 69 x more energy efficiency, with negligible accuracy loss relative to original decay models. This work highlights that beyond accelerating the (W x I) computation, optimizing state-update dynamics within CIM architectures is essential for scalable, low-power, and real-time neuromorphic processing.
