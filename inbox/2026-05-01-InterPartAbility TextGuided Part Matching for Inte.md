---
interest: medium
link: https://arxiv.org/abs/2604.27122
next_step: skim
priority: medium
slack_ts: '1777692910.983159'
source: cs.CV - Computer Vision
status: unread
title: 'InterPartAbility: Text-Guided Part Matching for Interpretable Person Re-Identification'
---
# InterPartAbility: Text-Guided Part Matching for Interpretable Person Re-Identification
> 原文: [https://arxiv.org/abs/2604.27122](https://arxiv.org/abs/2604.27122)

arXiv:2604.27122v1 Announce Type: new
Abstract: Text-to-image person re-identification (TI-ReID) relies on natural-language text description to retrieve top matching individuals from a large gallery of images. While recent large vision-language models (VLMs) achieve strong retrieval performance, their decisions remain largely uninterpretable. Existing interpretability approaches in TI-ReID rely solely on slot-attention to highlight attended regions, but fail to reliably bind visual regions to semantically meaningful concepts, limiting explanations to qualitative visualizations over a restricted vocabulary. This paper introduces InterPartAbility, an interpretable TI-ReID method that performs explicit part-wise matching and enables phrase-region grounding. A new open-vocabulary, lightweight supervision, patch-phrase interaction module (PPIM) is proposed to train a standard TI-ReID model with concept-level guidance. Concept-based part phrases provide evidence that encourages the model to attend to corresponding image regions. InterPartAbility further constrains CLIP ViT self-attention to produce spatially concentrated patch activations aligned with each part-level phrase, yielding grounded explanation maps. A quantitative interpretability protocol for TI-ReID is introduced by adapting perturbation-based evaluation metrics, including counterfactual region masking that measures retrieval degradation when top-ranked explanatory regions are removed. Empirical results\footnote{Our code is included in the supplementary materials and will be made public.} on challenging benchmarks like CUHK-PEDES and ICFG-PEDES show that InterPartAbility achieves state-of-the-art (SOTA) interpretability performance under these metrics, while sustaining competitive retrieval accuracy.
