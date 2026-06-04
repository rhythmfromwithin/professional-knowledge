---
interest: medium
link: https://arxiv.org/abs/2606.04061
next_step: skim
priority: medium
slack_ts: '1780548674.785339'
source: cs.CV - Computer Vision
status: unread
title: 'Intra-Modal Neighbors Never Lie: Rectifying Inter-Modal Noisy Correspondence
  via Graph-Based Intra-Modal Reasoning'
---
# Intra-Modal Neighbors Never Lie: Rectifying Inter-Modal Noisy Correspondence via Graph-Based Intra-Modal Reasoning
> 原文: [https://arxiv.org/abs/2606.04061](https://arxiv.org/abs/2606.04061)

arXiv:2606.04061v1 Announce Type: new
Abstract: Large-scale web-harvested datasets have fueled the progress of cross-modal retrieval but inevitably suffer from noisy correspondence, which severely degrades model generalization. Existing methods primarily address this by filtering out noise or seeking a substitute label, yet they predominantly remain bound by a "Discrete Selection" paradigm. We argue that relying on a single discrete proxy induces Single-Point Fragility and Discretization Error. To overcome these limitations, we propose a novel framework, Intra-modal Neighbor-aware Noise Rectification (IN2R), which shifts the paradigm from searching for a substitute to synthesizing a reliable supervision target. Leveraging the intrinsic geometric stability of intra-modal data, IN2R employs a Graph Refiner to perform relational reasoning over neighbors retrieved from a dynamic Cross-Model Memory. Instead of propagating discrete labels, our method synthesizes a continuous, soft prototype that reflects the consensus of the local semantic neighborhood, effectively rectifying inter-modal misalignment. Extensive experiments on Flickr30K, MS-COCO, and CC152K demonstrate that IN2R significantly outperforms state-of-the-art methods. Our code and pre-trained models are publicly available at https://github.com/liuyyy111/IN2R.
