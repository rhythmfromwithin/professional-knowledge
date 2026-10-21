---
interest: medium
link: https://arxiv.org/abs/2610.24038
next_step: skim
priority: medium
slack_ts: '1792556404.257199'
source: cs.DC - Distributed Computing
status: unread
title: 'Merge Hulls Without Copying Vertices: GPU Isotonic Regression'
---
# Merge Hulls Without Copying Vertices: GPU Isotonic Regression
> 原文: [https://arxiv.org/abs/2610.24038](https://arxiv.org/abs/2610.24038)

arXiv:2610.24038v1 Announce Type: new
Abstract: Isotonic regression finds the monotone sequence closest to the data in weighted least squares. It is used to calibrate probabilities and inside differentiable ranking. Its standard algorithm, pool adjacent violators, is sequential within a sequence, and torchsort, the exact GPU solver of differentiable sorting libraries, runs it with one thread per sequence, which is slow on long ones. The fit is the slope sequence of the lower convex hull of cumulative sums, and hulls of sorted points can be merged in parallel. Merging partial hulls level by level, however, copies the surviving vertices at every level, which moves $\Theta(n \log n)$ data when most points survive. We store each chunk's hull once and represent a merged hull as a list of segments of these chunk hulls, at most one per chunk; a merge then updates the list. We prove the representation correct, bound the work and depth of the merge phase, and measure a CUDA implementation on four NVIDIA GPUs against a control that copies the surviving vertices with the whole GPU at every level. On dense hulls the merge phase is 17 to 276 times faster with segment lists and the whole operator 3.9 to 19 times; on noisy data, where few vertices survive, the difference is small. In a differentiable soft rank, replacing torchsort's isotonic solver makes forward and backward 2.3 to 230 times faster on a T4, and the training step of a compact model with a Spearman loss 1.6 to 9 times.
