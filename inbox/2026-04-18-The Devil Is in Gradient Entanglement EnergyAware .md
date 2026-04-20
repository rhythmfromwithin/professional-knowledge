---
interest: medium
link: https://arxiv.org/abs/2604.14176
next_step: skim
priority: high
slack_ts: '1776656361.938719'
source: cs.LG - Machine Learning
status: unread
title: 'The Devil Is in Gradient Entanglement: Energy-Aware Gradient Coordinator for
  Robust Generalized Category Discovery'
---
# The Devil Is in Gradient Entanglement: Energy-Aware Gradient Coordinator for Robust Generalized Category Discovery
> 原文: [https://arxiv.org/abs/2604.14176](https://arxiv.org/abs/2604.14176)

arXiv:2604.14176v1 Announce Type: new
Abstract: Generalized Category Discovery (GCD) leverages labeled data to categorize unlabeled samples from known or unknown classes. Most previous methods jointly optimize supervised and unsupervised objectives and achieve promising results. However, inherent optimization interference still limits their ability to improve further. Through quantitative analysis, we identify a key issue, i.e., gradient entanglement, which 1) distorts supervised gradients and weakens discrimination among known classes, and 2) induces representation-subspace overlap between known and novel classes, reducing the separability of novel categories. To address this issue, we propose the Energy-Aware Gradient Coordinator (EAGC), a plug-and-play gradient-level module that explicitly regulates the optimization process. EAGC comprises two components: Anchor-based Gradient Alignment (AGA) and Energy-aware Elastic Projection (EEP). AGA introduces a reference model to anchor the gradient directions of labeled samples, preserving the discriminative structure of known classes against the interference of unlabeled gradients. EEP softly projects unlabeled gradients onto the complement of the known-class subspace and derives an energy-based coefficient to adaptively scale the projection for each unlabeled sample according to its degree of alignment with the known subspace, thereby reducing subspace overlap without suppressing unlabeled samples that likely belong to known classes. Experiments show that EAGC consistently boosts existing methods and establishes new state-of-the-art results. Code is available at https://haiyangzheng.github.io/EAGC.
