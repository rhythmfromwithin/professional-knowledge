---
title: "Uncertainty Gates the Gradient: Adaptive Updates for Generalized Few-Shot 3D Segmentation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.26909
priority: medium
status: unread
interest: medium
next_step: skim
---
# Uncertainty Gates the Gradient: Adaptive Updates for Generalized Few-Shot 3D Segmentation
> 原文: [https://arxiv.org/abs/2610.26909](https://arxiv.org/abs/2610.26909)

arXiv:2610.26909v1 Announce Type: new
Abstract: In generalized few-shot 3D point cloud segmentation, support annotations are often compromised by sparsity and occlusion. Blindly adapting to such low quality samples risks learning spurious geometric patterns rather than robust novel concepts. Although 3D Vision-Language Models have been introduced to sup plement supervision, the potential of uncertainty to actively govern adaptation dynamics remains underexplored. Existing signal-level methods like loss reweight ing fail to prevent unreliable episodes from steering the optimization trajectory. To address this, we propose Uncertainty-Gated Adaptive (UGA), to the best of our knowledge the first framework that elevates uncertainty to update-level gating for generalized few-shot 3D point cloud segmentation. The core mod ule, Uncertainty-Gated Update (UG-Update), estimates episodic reliability via intra-class dispersion over merged support and pseudo-labeled novel supervision, and selectively gates residual gradient updates. This encourages the model to learn novel semantics from reliable episodes while attenuating updates during unreliable ones. Complementing this, we introduce an Uncertainty-Based Pseudo Label Filter (UB-Filter) to enforce learning from high-confidence dense signals. On ScanNet200 and ScanNet++ (1-/5-shot), UGA sets new state of the art with an average +3.08 HM IoU over the strongest prior baseline.
