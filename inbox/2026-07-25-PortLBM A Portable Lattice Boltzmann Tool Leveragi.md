---
title: "PortLBM: A Portable Lattice Boltzmann Tool Leveraging SYCL on AMD, NVIDIA, and Intel GPUs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.20650
priority: medium
status: unread
interest: medium
next_step: skim
---
# PortLBM: A Portable Lattice Boltzmann Tool Leveraging SYCL on AMD, NVIDIA, and Intel GPUs
> 原文: [https://arxiv.org/abs/2607.20650](https://arxiv.org/abs/2607.20650)

arXiv:2607.20650v1 Announce Type: new
Abstract: The lattice Boltzmann method (LBM) is a well-established approach for simulating fluid flows at the mesoscopic scale. With the stagnation of Moore's law, high-performance computing has shifted toward GPU accelerators, necessitating programming models that ensure both portability and efficiency across diverse hardware platforms.
We present PortLBM, an extensible portable LBM framework built on SYCL that integrates cross-platform GPU support with interactive real-time visualization. PortLBM supports diverse simulation scenarios ranging from K\'arm\'an vortex streets and wing flows to porous media, and is designed for easy extension with new algorithms and backends. As part of a performance portability study, we evaluate PortLBM on contemporary GPU architectures from NVIDIA, AMD, and Intel, examining the impact of three data layouts (stream, bundle, and collision) and four algorithmic variants on simulation throughput.
Our results show that no single configuration achieves optimal performance across all GPU vendors, confirming the need for system-specific tuning. The stream layout maximizes bandwidth and performs best on the contemporary NVIDIA and Intel GPUs, while the bundle layout improves cache efficiency and excels on the AMD GPU. Two-lattice schemes achieve higher throughput while one-lattice schemes are preferable under memory constraints. Our work underscores the necessity for adaptable, portable LBM software in increasingly heterogeneous computing environments.
