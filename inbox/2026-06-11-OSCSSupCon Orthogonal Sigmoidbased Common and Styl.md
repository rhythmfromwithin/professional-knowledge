---
interest: medium
link: https://arxiv.org/abs/2606.11233
next_step: skim
priority: medium
slack_ts: '1781153120.507039'
source: cs.CV - Computer Vision
status: unread
title: 'OSCS-SupCon: Orthogonal Sigmoid-based Common and Style Supervised Contrastive
  Learning for Robust Feature Disentanglement'
---
# OSCS-SupCon: Orthogonal Sigmoid-based Common and Style Supervised Contrastive Learning for Robust Feature Disentanglement
> 原文: [https://arxiv.org/abs/2606.11233](https://arxiv.org/abs/2606.11233)

arXiv:2606.11233v1 Announce Type: new
Abstract: Supervised Contrastive Learning (SupCon) has achieved strong performance by explicitly modeling pairwise relationships among samples. However, existing SupCon-based methods suffer from two key limitations: negative-sample dilution induced by the standard InfoNCE loss, and feature-space entanglement caused by the lack of explicit constraints separating category-relevant (common) and category-irrelevant (style) features. These limitations reduce feature discriminability and generalization ability. To address these issues, we propose OSCS-SupCon (Orthogonal Sigmoid-based Common and Style Supervised Contrastive Learning), a unified framework that combines a sigmoid-based pairwise contrastive objective with explicit orthogonality constraints. Specifically, we introduce a sigmoid-based contrastive loss with two learnable parameters, temperature and bias, which adaptively modulate pairwise decision boundaries and alleviate negative-sample dilution. Furthermore, we enforce orthogonality between common and style feature subspaces via a linear projection with ReLU nonlinearity, thereby reducing feature overlap and improving disentanglement of style-irrelevant representations. Extensive experiments on six benchmark datasets demonstrate that OSCS-SupCon consistently outperforms state-of-the-art supervised contrastive learning methods across multiple backbone architectures. In particular, on the fine-grained CUB200-2011 dataset with a ResNet-18 backbone, the proposed method achieves a 3.4% improvement in classification accuracy over CS-SupCon, highlighting its robustness and generalization capability. Ablation studies further confirm the effectiveness of each component.
