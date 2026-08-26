---
title: "Rapid Earthquake-to-Tsunami Waveform Generation via Large-Scale Multi-GPU FFT Convolution Applied to the Cascadia Subduction Zone"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.21763
priority: medium
status: unread
interest: medium
next_step: skim
---
# Rapid Earthquake-to-Tsunami Waveform Generation via Large-Scale Multi-GPU FFT Convolution Applied to the Cascadia Subduction Zone
> 原文: [https://arxiv.org/abs/2608.21763](https://arxiv.org/abs/2608.21763)

arXiv:2608.21763v1 Announce Type: new
Abstract: Data-driven methods for earthquake and tsunami early warning rely on large ensembles of rupture scenarios and their resulting waveforms, but generating such datasets with repeated high-fidelity seismic and tsunami simulations is prohibitively expensive. We exploit the linear time-invariant structure of both dynamics to precompute elastic Green's functions and acoustic-gravity adjoint responses, reducing the source-to-waveform map to two consecutive convolution operators. We evaluate these convolutions with a distributed, FFT-accelerated GPU pipeline that partitions the large seafloor grid across GPUs and directly generates the final observation waveforms. We demonstrate the scalability of this pipeline for the Cascadia Subduction Zone with 963 subfaults, 2,416,530 seafloor grid points, 64 observation locations, and 256 timesteps, requiring 9.45 TiB of aggregate GPU memory. On 64 GB200 GPUs within one NVL72 domain, the pipeline generates waveforms in 24 ms per rupture once the response operators are resident, enabling large rupture ensembles to be evaluated within minutes.
