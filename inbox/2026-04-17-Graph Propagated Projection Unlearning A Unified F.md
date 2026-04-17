---
title: "Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.13127
priority: medium
status: unread
interest: medium
next_step: skim
---
# Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models
> 原文: [https://arxiv.org/abs/2604.13127](https://arxiv.org/abs/2604.13127)

arXiv:2604.13127v1 Announce Type: new
Abstract: The need to selectively and efficiently erase learned information from deep neural networks is becoming increasingly important for privacy, regulatory compliance, and adaptive system design. We introduce Graph-Propagated Projection Unlearning (GPPU), a unified and scalable algorithm for class-level unlearning that operates across both vision and audio models. GPPU employs graph-based propagation to identify class-specific directions in the feature space and projects representations onto the orthogonal subspace, followed by targeted fine-tuning, to ensure that target class information is effectively and irreversibly removed. Through comprehensive evaluations on six vision datasets and two large-scale audio benchmarks spanning a variety of architectures including CNNs, Vision Transformers, and Audio Transformers, we demonstrate that GPPU achieves highly efficient unlearning, realizing 10-20x speedups over prior methodologies while preserving model utility on retained classes. Our framework provides a principled and modality-agnostic approach to machine unlearning, evaluated at a scale that has received limited attention in prior work, contributing toward more efficient and responsible deep learning.
