---
title: "BlockMGARD: Accelerating Adaptive Scientific Data Reduction with Region-of-Interest Error Control on GPUs"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.00205
priority: medium
status: unread
interest: medium
next_step: skim
---
# BlockMGARD: Accelerating Adaptive Scientific Data Reduction with Region-of-Interest Error Control on GPUs
> 原文: [https://arxiv.org/abs/2609.00205](https://arxiv.org/abs/2609.00205)

arXiv:2609.00205v1 Announce Type: new
Abstract: The growing scale of scientific data makes lossy compression essential for reducing data volume under controllable error. Transformation-based compressors using multilevel decomposition, such as MGARD, achieve strong compression ratios but map poorly to GPU architectures. We propose BlockMGARD, an adaptive, Region-of-Interest (ROI)-supported GPU lossy compressor, with four contributions: (1) an In-cache Block decomposition leveraging GPU on-chip memory and constant lookup tables to accelerate decomposition; (2) a hybrid hierarchy combining In-cache Block and global decomposition to balance speed and compression ratio; (3) an end-to-end pipeline with fine-grained ROI error control for feature preservation; and (4) an evaluation against state-of-the-art methods on five real-world datasets. Compared to MGARD-X, BlockMGARD achieves up to 4.2x and 9.1x higher compression and decompression throughput, and up to 8.63x higher compression ratio than uniform-tolerance baselines under ROI-aware error control. Across four GPUs, BlockMGARD achieves near-ideal linear scaling and up to 1.58x I/O cost reduction over MGARD-X.
