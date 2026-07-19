---
interest: medium
link: https://arxiv.org/abs/2607.14394
next_step: skim
priority: medium
slack_ts: '1784432006.207699'
source: cs.DC - Distributed Computing
status: unread
title: 'DRIFT: Direct Reduced Fourier Transforms for Distributed Spectral Neural Operators'
---
# DRIFT: Direct Reduced Fourier Transforms for Distributed Spectral Neural Operators
> 原文: [https://arxiv.org/abs/2607.14394](https://arxiv.org/abs/2607.14394)

arXiv:2607.14394v1 Announce Type: new
Abstract: Fourier Neural Operators (FNOs) learn solution operators for partial differential equations and offer orders of magnitude speedup over traditional numerical solvers at inference time, which makes them attractive surrogates for high-resolution computational physics. Scaling FNOs to high-resolution spatial grids requires distributing the data across GPUs, but the distributed FFT at the core of each spectral layer requires multiple dense all-to-all collectives that communicate the full spatial tensor, only for most coefficients to be discarded immediately. We introduce the Distributed Truncated Spectral Transform (DTST), which reverses this order. Each GPU computes only a small subset of frequency modes used by the spectral convolution locally via a partial DFT, and two collectives combine the results with a payload that depends only on this mode count, not the spatial resolution. DTST produces spectral coefficients identical to the standard distributed FFT with truncation, while providing both spatial data parallelism and spectral weight model parallelism. We present DRIFT, a GPU implementation of DTST for distributed Fourier Neural Operators, using separable per-dimension basis matrices and efficient GPU-to-GPU communication. On a 3D+time FNO across 4--32 GPUs, on up to 8 nodes (4 GPUs/node), DRIFT achieves a forward-pass speedup of 38--64$\times$ and a 37$\times$ training speedup over the distributed FNO baseline, reducing communication time from 97\% to under 6\% of the forward-pass time, with growing speedups at higher resolution.
