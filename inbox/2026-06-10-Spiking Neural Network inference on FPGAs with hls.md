---
title: "Spiking Neural Network inference on FPGAs with hls4ml"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2606.10008
priority: low
status: unread
interest: medium
next_step: skim
---
# Spiking Neural Network inference on FPGAs with hls4ml
> 原文: [https://arxiv.org/abs/2606.10008](https://arxiv.org/abs/2606.10008)

arXiv:2606.10008v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) provide a naturally temporal machine-learning framework. Their neurons maintain an internal state and propagate information through discrete spikes, enabling low-latency temporal inference. Although SNNs are often associated with asynchronous neuromorphic processors, many scientific real-time inference systems rely on conventional synchronous field-programmable gate arrays (FPGAs) and high-level synthesis (HLS) workflows. In this paper we present an extension of hls4ml that enables clock-driven deployment of SNNs trained in pytorch onto FPGA firmware. We demonstrate the workflow using a dense quantised SNN trained on the Heidelberg Spiking Digits dataset where it achieves inference latencies of approximately $34\mu$s. We validate the generated design through software reference comparisons, HLS C simulation, HLS synthesis, export, and Vivado synthesis reports. This work opens up the hls4ml toolkit to neuromorphic computing, allowing streamlined optimisation, synthesis, and deployment of SNN models for real-time inference.
