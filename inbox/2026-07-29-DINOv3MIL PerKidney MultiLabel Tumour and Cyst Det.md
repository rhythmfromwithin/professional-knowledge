---
interest: medium
link: https://arxiv.org/abs/2607.22687
next_step: skim
priority: medium
slack_ts: '1785468989.778309'
source: cs.CV - Computer Vision
status: unread
title: 'DINOv3-MIL: Per-Kidney Multi-Label Tumour and Cyst Detection from Foundation-Model
  Patch Tokens on KiTS23'
---
# DINOv3-MIL: Per-Kidney Multi-Label Tumour and Cyst Detection from Foundation-Model Patch Tokens on KiTS23
> 原文: [https://arxiv.org/abs/2607.22687](https://arxiv.org/abs/2607.22687)

arXiv:2607.22687v2 Announce Type: new
Abstract: Foundation vision models trained on natural images transfer to medical tasks without domain pre-training, but volumetric classification requires aggregating tens of thousands of patch tokens per study, and the aggregator constrains how the resulting model can be interpreted. We compare three aggregators on identical frozen DINOv3 ViT-H/16+ features for renal tumour/cyst detection on KiTS23 (966 kidneys; n=97 test): a CLS-token linear probe, gated attention multiple instance learning (MIL) over 55,296 patch tokens, and a prototype head following ProtoViT. Attention MIL achieves the highest AUROC for tumour (0.74, 95% CI 0.64-0.83) and cyst (0.80, 0.70-0.88), with attention enriched 7.5-9.8x over chance within annotated lesions. The prototype head does not transfer to cyst detection (AUROC 0.51), exposing an interpretability-performance trade-off at this token scale.
