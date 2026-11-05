---
interest: medium
link: https://arxiv.org/abs/2611.04138
next_step: skim
priority: medium
slack_ts: '1793859289.334859'
source: cs.DC - Distributed Computing
status: unread
title: 'PhotonZip: Lifecycle-Aware Compression for HDF5-Based Synchrotron Workflows'
---
# PhotonZip: Lifecycle-Aware Compression for HDF5-Based Synchrotron Workflows
> 原文: [https://arxiv.org/abs/2611.04138](https://arxiv.org/abs/2611.04138)

arXiv:2611.04138v1 Announce Type: new
Abstract: Synchrotron detectors generate data at rates that challenge storage and I/O systems. Compression can reduce data movement, but codec-only measurements do not capture the end-to-end behavior of HDF5 workflows. We present PhotonZip, a lifecycle-aware compression framework that tests candidate modes through a common HDF5 path and selects among eligible measured configurations according to either compression ratio or round-trip throughput. Its modular filters preserve standard HDF5 access when the required plugin is available. Across four beamline-derived datasets, PhotonZip reaches lossless compression ratios up to 1.629$\times$ and HDF5 write throughput up to 3.40GB/s write and 7.75GB/s read. The throughput-oriented configuration achieves 1.529$\times$ lossless data reduction while improving HDF5 write and read throughput by 21.2\% and 15.0\%, respectively. Lossy preview modes provide up to 16$\times$ data reduction and reduce preview latency by up to 8.35~s in the evaluated file-per-rank HDF5 configuration.
