---
title: "Exemplar: Classical Priors Complement Frozen Features for Few-Shot Microscopy Segmentation at Native Resolution"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.03080
priority: medium
status: unread
interest: medium
next_step: skim
---
# Exemplar: Classical Priors Complement Frozen Features for Few-Shot Microscopy Segmentation at Native Resolution
> 原文: [https://arxiv.org/abs/2609.03080](https://arxiv.org/abs/2609.03080)

arXiv:2609.03080v1 Announce Type: new
Abstract: Segmenting a new biomedical dataset usually means a domain-specific model trained on substantial annotation, or a foundation model steered at inference time. We present Exemplar, a few-shot segmenter that fuses a frozen DINOv3 backbone with a fixed bank of classical native-resolution filter responses in one lightweight head, fitted from the support masks alone. In the few-mask, native-resolution regime, classical priors and frozen self-supervised features are complementary: fused in one head, a single fixed configuration spans eleven biomedical imaging datasets. Under the same head, the classical bank alone reaches 0.693 on the eleven-dataset panel, scored by foreground intersection-over-union or centreline Dice, and the frozen features alone 0.672; the bank leads on seven of the eleven and the features on the rest, and fused they reach 0.782. Against five forward-pass few-shot methods, Exemplar leads in 54 of 55 method-dataset comparisons, 52 of them significant after Holm correction. From a single annotated mask it reaches 0.703 on the same panel, against 0.682 for a from-scratch nnU-Net trained on that same mask. At eight masks nnU-Net overtakes it on the panel mean, chiefly on centreline agreement, but takes 16-77x longer to fit.
