---
title: "HERO: Histology Encoder for Robust Representation in Oncology"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.35943
priority: medium
status: unread
interest: medium
next_step: skim
---
# HERO: Histology Encoder for Robust Representation in Oncology
> 原文: [https://arxiv.org/abs/2609.35943](https://arxiv.org/abs/2609.35943)

arXiv:2609.35943v1 Announce Type: new
Abstract: Foundation models trained on large pathology image corpora now provide strong, transferable representations for computational pathology. Over the past few years a series of such models has been released, each trained on more slides than the last; on standard classification and segmentation benchmarks, the leading models are now separated by small margins. In clinical use, however, the foundation model is applied to images from hospitals, scanners, and staining protocols outside its training data. Encoders generally embed these acquisition factors alongside biological information, which may introduce downstream errors and hinder safe clinical adoption. A pathology foundation model should therefore be robust to acquisition shift without giving up representation quality, yet robustness is seldom the axis along which models are compared. In this report, we introduce HERO (Histology Encoder for Robust Representation in Oncology), a ViT-G/14 pathology foundation model trained with the DINO and iBOT objectives and refined with high-resolution Gram anchoring on a morphology-balanced corpus of 500 million tiles from approximately 575,000 clinical whole-slide images. Across the evaluated public benchmarks, HERO shows the strongest robustness to center, scanner, and stain variation among the compared state-of-the-art foundation models, performs comparably on tile-level classification, segmentation, and gene-expression prediction, ranks first on average across 39 evaluated slide-level clinical tasks, and, under an equal-weighted framework-level analysis, has the best average rank across the six benchmark frameworks.
