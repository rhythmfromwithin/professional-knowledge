---
interest: medium
link: https://arxiv.org/abs/2606.25009
next_step: skim
priority: medium
slack_ts: '1782360765.602909'
source: cs.CV - Computer Vision
status: unread
title: Noise-Aware Boundary-Enhanced Generative Learning for Ultrasound Speckle Reduction
---
# Noise-Aware Boundary-Enhanced Generative Learning for Ultrasound Speckle Reduction
> 原文: [https://arxiv.org/abs/2606.25009](https://arxiv.org/abs/2606.25009)

arXiv:2606.25009v1 Announce Type: new
Abstract: Ultrasound is a non-invasive, real-time, and cost-effective imaging technique widely used in clinical diagnosis. However, its diagnostic efficacy is often compromised by inherent speckle noise that degrades image quality and obscures underlying anatomical structures. Existing speckle reduction methods tend to over-smooth tissue boundaries and generalize poorly to heterogeneous noise levels. To address these limitations, we propose a Noise-Aware Boundary-Enhanced Generative Learning (NBGL) framework for ultrasound speckle reduction, which simultaneously preserves annotated anatomical boundaries and adapts to varying noise levels. The NBGL framework consists of a speckle reduction branch and a boundary enhancement branch. The former leverages generative learning to suppress speckle noise, while the latter learns boundary-sensitive representations to preserve target anatomical structures. Furthermore, a noise-aware interaction weight generation (NIWG) module estimates the speckle noise level via 3D Laplacian filtering and a median absolute deviation estimator, and translates it into an adaptive interaction weight. This weight is incorporated into a weighted feature-wise linear modulation (wFiLM) module to adaptively modulate cross-branch feature coupling, thereby improving robustness to varying noise levels. Extensive evaluations on 141 3D transvaginal ultrasound volumes demonstrate that NBGL consistently outperforms state-of-the-art methods in speckle reduction and structural preservation across six noise levels, while maintaining consistency with annotated anatomical boundaries.
