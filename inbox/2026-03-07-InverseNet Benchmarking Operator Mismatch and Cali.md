---
title: "InverseNet: Benchmarking Operator Mismatch and Calibration Across Compressive Imaging Modalities"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.04538
priority: medium
status: unread
---
# InverseNet: Benchmarking Operator Mismatch and Calibration Across Compressive Imaging Modalities
> 原文: [https://arxiv.org/abs/2603.04538](https://arxiv.org/abs/2603.04538)

arXiv:2603.04538v1 Announce Type: new
Abstract: State-of-the-art EfficientSCI loses 20.58 dB when its assumed forward operator deviates from physical reality in just eight parameters, yet no existing benchmark quantifies operator mismatch, the default condition in deployed compressive imaging systems. We introduce InverseNet, the first cross-modality benchmark for operator mismatch, spanning CASSI, CACTI, and single-pixel cameras. Evaluating 12 methods under a four-scenario protocol (ideal, mismatched, oracle-corrected, blind calibration) across 27 simulated scenes and 9 real hardware captures, we find: (1) deep learning methods lose 10-21 dB under mismatch, eliminating their advantage over classical baselines; (2) performance and robustness are inversely correlated across modalities (Spearman r\_s = -0.71, p < 0.01); (3) mask-oblivious architectures recover 0% of mismatch losses regardless of calibration quality, while operator-conditioned methods recover 41-90%; (4) blind grid-search calibration recovers 85-100% of the oracle bound without ground truth. Real hardware experiments confirm that simulation trends transfer to physical data. Code will be released upon acceptance.
