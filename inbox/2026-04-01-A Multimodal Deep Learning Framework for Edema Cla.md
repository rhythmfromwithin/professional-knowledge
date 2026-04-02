---
interest: medium
link: https://arxiv.org/abs/2603.26726
next_step: skim
priority: medium
slack_ts: '1775098518.491339'
source: cs.CV - Computer Vision
status: unread
title: A Multimodal Deep Learning Framework for Edema Classification Using HCT and
  Clinical Data
---
# A Multimodal Deep Learning Framework for Edema Classification Using HCT and Clinical Data
> 原文: [https://arxiv.org/abs/2603.26726](https://arxiv.org/abs/2603.26726)

arXiv:2603.26726v1 Announce Type: new
Abstract: We propose AttentionMixer, a unified deep learning framework for multimodal detection of brain edema that combines structural head CT (HCT) with routine clinical metadata. While HCT provides rich spatial information, clinical variables such as age, laboratory values, and scan timing capture complementary context that might be ignored or naively concatenated. AttentionMixer is designed to fuse these heterogeneous sources in a principled and efficient manner. HCT volumes are first encoded using a self-supervised Vision Transformer Autoencoder (ViT-AE++), without requiring large labeled datasets. Clinical metadata are mapped into the same feature space and used as keys and values in a cross-attention module, where HCT-derived feature vector serves as queries. This cross-attention fusion allows the network to dynamically modulate imaging features based on patient-specific context and provides an interpretable mechanism for multimodal integration. A lightweight MLP-Mixer then refines the fused representation before final classification, enabling global dependency modeling with substantially reduced parameter overhead. Missing or incomplete metadata are handled via a learnable embedding, promoting robustness to real-world clinical data quality. We evaluate AttentionMixer on a curated brain HCT cohort with expert edema annotations using five-fold cross-validation. Compared with strong HCT-only, metadata-only, and prior multimodal baselines, AttentionMixer achieves superior performance (accuracy 87.32%, precision 92.10%, F1-score 85.37%, AUC 94.14%). Ablation studies confirm the benefit of both cross-attention and MLP-Mixer refinement, and permutation-based metadata importance analysis highlights clinically meaningful variables driving predictions. These results demonstrate that structured, interpretable multimodal fusion can substantially improve edema detection in clinical practice.
