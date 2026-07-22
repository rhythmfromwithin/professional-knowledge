---
interest: medium
link: https://arxiv.org/abs/2607.15413
next_step: skim
priority: medium
slack_ts: '1784690752.857429'
source: cs.DC - Distributed Computing
status: unread
title: 'FSZ: Breaking the Prediction-Throughput Trade-off in GPU Lossy Compression'
---
# FSZ: Breaking the Prediction-Throughput Trade-off in GPU Lossy Compression
> 原文: [https://arxiv.org/abs/2607.15413](https://arxiv.org/abs/2607.15413)

arXiv:2607.15413v1 Announce Type: new
Abstract: Existing fast GPU error-bounded lossy compressors have achieved high throughput through pure-GPU single-kernel designs, but their compression ratios remain limited because they typically apply a fixed first-order predictor on independent blocks. We propose FSZ, a GPU error-bounded lossy compressor that redesigns the prediction stage with three mutually reinforcing algorithmic innovations to achieve both higher compression ratios and higher throughput within a single CUDA kernel: (1) cross-block prediction state carries Lorenzo prediction state across block boundaries within 256-element tiles, eliminating 7 out of 8 boundary residuals that inflate encoding rates; (2) per-tile adaptive multi-order prediction and centering adaptively selects the best compression strategy per tile from first-order, second-order, and centering variants; and (3) a single-pass four-way evaluation exploits a mathematical property of finite differences to evaluate all variants from a single data read, enabling richer prediction within the same bandwidth budget as a fixed predictor. Experiments on NVIDIA GH200 GPU with 8 real-world application datasets show that FSZ outperforms cuSZp-P by up to 10.95x and the state-of-the-art cuSZp-O by up to 2.92x in compression ratio. Notably, these gains come with no throughput penalty: FSZ simultaneously achieves the highest average throughput (676 GB/s compression, 785 GB/s decompression) among all evaluated compressors.
