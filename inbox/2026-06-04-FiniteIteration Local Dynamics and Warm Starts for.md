---
title: "Finite-Iteration Local Dynamics and Warm Starts for Alternating Power Iteration in Spiked Tensor PCA"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2606.04065
priority: medium
status: unread
interest: medium
next_step: skim
---
# Finite-Iteration Local Dynamics and Warm Starts for Alternating Power Iteration in Spiked Tensor PCA
> 原文: [https://arxiv.org/abs/2606.04065](https://arxiv.org/abs/2606.04065)

arXiv:2606.04065v1 Announce Type: new
Abstract: We study simultaneous alternating power iteration for fixed-order asymmetric rank-one spiked tensor models. Our main contribution is a finite-iteration local theory that is independent of any particular initialization. Once the iterates enter a sufficiently small neighborhood of the planted rank-one direction, their error decomposes into a geometrically decaying transient and an intrinsic noise floor caused by fixed orthogonal noise contractions at the planted point. The deterministic finite-sample conditions are stated explicitly, but under a coarse fixed-order multilinear noise event they reduce to a conservative high-signal regime for fixed or slowly expanding local radii.
We then separate the warm-start mechanism from any specific spectral construction. A generic one-sweep principle shows that, if a sign-compatible initializer has correlation \(\gamma\_N\), first-sweep noise level \(a\_N\), and \(a\_N/(\gamma\_N^{d-1}\omega\_{N,d})\to0\), then one can choose an expanding radius \(r\_N=o(\omega\_{N,d})\) for which the first sweep enters the local basin. After entry, the local affine contraction yields convergence to the unique informative local fixed point in that basin. For centered-Gram initialization, we verify the required correlation and same-sample first-sweep noise bound under i.i.d. finite-fourth-moment noise by a signal-preserving noise-only leave-one comparison and an averaged leave-one slice-contraction estimate, which we call a pressed-back estimate. The leave-one comparison keeps the spike fixed and averages over the deleted coordinate, so planted coordinates enter through \(\ell\_2\)-weighted sums rather than worst-case incoherence bounds.
