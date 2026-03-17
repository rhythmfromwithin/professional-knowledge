---
interest: medium
link: https://arxiv.org/abs/2603.06650
next_step: skim
priority: medium
slack_ts: '1773715514.969509'
source: cs.CV - Computer Vision
status: unread
title: Margin-Consistent Deep Subtyping of Invasive Lung Adenocarcinoma via Perturbation
  Fidelity in Whole-Slide Image Analysis
---
# Margin-Consistent Deep Subtyping of Invasive Lung Adenocarcinoma via Perturbation Fidelity in Whole-Slide Image Analysis
> 原文: [https://arxiv.org/abs/2603.06650](https://arxiv.org/abs/2603.06650)

arXiv:2603.06650v1 Announce Type: new
Abstract: Whole-slide image classification for invasive lung adenocarcinoma subtyping remains vulnerable to real-world imaging perturbations that undermine model reliability at the decision boundary. We propose a margin consistency framework evaluated on 203,226 patches from 143 whole-slide images spanning five adenocarcinoma subtypes in the BMIRDS-LUAD dataset. By combining attention-weighted patch aggregation with margin-aware training, our approach achieves robust feature-logit space alignment measured by Kendall correlations of 0.88 during training and 0.64 during validation. Contrastive regularization, while effective at improving class separation, tends to over-cluster features and suppress fine-grained morphological variation; to counteract this, we introduce Perturbation Fidelity (PF) scoring, which imposes structured perturbations through Bayesian-optimized parameters. Vision Transformer-Large achieves 95.20 +/- 4.65% accuracy, representing a 40% error reduction from the 92.00 +/- 5.36% baseline, while ResNet101 with an attention mechanism reaches 95.89 +/- 5.37% from 91.73 +/- 9.23%, a 50% error reduction. All five subtypes exceed an area under the receiver operating characteristic curve (AUC) of 0.99. On the WSSS4LUAD external benchmark, ResNet50 with an attention mechanism attains 80.1% accuracy, demonstrating cross-institutional generalizability despite approximately 15-20% domain-shift-related degradation and identifying opportunities for future adaptation research.
