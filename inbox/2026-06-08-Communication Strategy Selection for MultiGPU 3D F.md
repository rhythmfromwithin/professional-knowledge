---
interest: medium
link: https://arxiv.org/abs/2606.06910
next_step: skim
priority: medium
slack_ts: '1780894163.309889'
source: cs.DC - Distributed Computing
status: unread
title: Communication Strategy Selection for Multi-GPU 3D FDTD with Convolutional Perfectly
  Matched Boundary Layers
---
# Communication Strategy Selection for Multi-GPU 3D FDTD with Convolutional Perfectly Matched Boundary Layers
> 原文: [https://arxiv.org/abs/2606.06910](https://arxiv.org/abs/2606.06910)

arXiv:2606.06910v1 Announce Type: new
Abstract: In this paper we describe a communication-strategy study for multi-GPU three-dimensional finite-difference time-domain computation with convolutional perfectly matched layer boundary conditions using CUDA. The metrics used to determine the most effective implementation include runtime, throughput in millions of output points per second, strong-scaling efficiency, CPML overhead, host-staged versus direct GPU-to-GPU exchange speedup, and enlarged-ghost speedup. On a single NVIDIA Quadro RTX 6000 GPU, the CPML implementation sustains 2,889--3,290 million output points per second with less than 1\% boundary-layer overhead, providing the single-GPU baseline for the multi-GPU study. The results show that direct GPU-to-GPU peer exchange is the dominant optimization with a 2.46--2.76$\times$ speedup over host-staged exchange, while enlarged ghost regions give only modest benefits because the reduced communication frequency is partly offset by redundant computation and additional memory traffic. On NVIDIA Quadro RTX 8000 GPUs, the implementation gives up to a 1.51$\times$ speedup on two GPUs for the tested strong-scaling cases, while four GPUs enable larger grids that approach or exceed single-GPU memory capacity.
