---
interest: medium
link: https://arxiv.org/abs/2605.00462
next_step: skim
priority: medium
slack_ts: '1777952323.327429'
source: cs.DC - Distributed Computing
status: unread
title: Adaptation of AI-accelerated CFD Simulations to the IPU platform
---
# Adaptation of AI-accelerated CFD Simulations to the IPU platform
> 原文: [https://arxiv.org/abs/2605.00462](https://arxiv.org/abs/2605.00462)

arXiv:2605.00462v1 Announce Type: new
Abstract: Intelligence Processing Units (IPU) have proven useful for many AI applications. In this paper, we evaluate them within the emerging field of \emph{AI for simulation}, where traditional numerical simulations are supported by artificial intelligence approaches. We focus specifically on a program for training machine learning models supporting a \emph{computational fluid dynamics} application. We use custom TensorFlow provided by the Poplar SDK to adapt the program for the IPU-POD16 platform and investigate its ease of use and performance scalability. Training a model on data from OpenFOAM simulations allows us to get accurate simulation state predictions in test time. We show how to utilize the \emph{popdist} library to overcome a performance bottleneck in feeding training data to the IPU on the host side, achieving up to 34\% speedup. Due to communication overheads, using data parallelism to utilize two IPUs instead of one does not improve the throughput. However, once the intra-IPU costs have been paid, the hardware capabilities for inter-IPU communication allow for good scalability. Increasing the number of IPUs from 2 to 16 improves the throughput from 560.8 to 2805.8 samples/s.
