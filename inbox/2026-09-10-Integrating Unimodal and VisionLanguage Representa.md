---
interest: medium
link: https://arxiv.org/abs/2609.09185
next_step: skim
priority: medium
slack_ts: '1789013738.442449'
source: cs.CV - Computer Vision
status: unread
title: Integrating Unimodal and Vision-Language Representations in Latent Space for
  Multi-Label Chest X-Ray Classification
---
# Integrating Unimodal and Vision-Language Representations in Latent Space for Multi-Label Chest X-Ray Classification
> 原文: [https://arxiv.org/abs/2609.09185](https://arxiv.org/abs/2609.09185)

arXiv:2609.09185v1 Announce Type: new
Abstract: Multi-label chest X-ray classification has attracted considerable attention in recent years, with the effective use of visual representations and clinical semantic knowledge playing an important role. This study proposes a framework that combines unimodal representations from RAD-DINO with vision--language representations from BioViL-T for the classification of 14 labels in the MIMIC-CXR-JPG dataset. The RAD-DINO and BioViL-T embeddings and their combined representation are refined separately in latent space before being normalized and fused across the three branches. In addition to improving classification performance, the study aims to clarify the role of each embedding source and the degree to which they complement one another.
Experiments show that RAD-DINO outperforms BioViL-T when used independently, whereas early fusion further improves the results, indicating that the two embedding sources contain complementary information. The best-performing model achieves a mean AUROC of 0.840 and an mAP of 0.467. Ablation analysis shows that hybrid fusion provides consistent and statistically significant improvements over early fusion when each embedding source is refined in latent space, suggesting that fusion effectiveness depends on the quality of the representation supplied by each branch. However, the study has only been evaluated internally on MIMIC-CXR-JPG; its generalizability to data from other healthcare institutions therefore remains to be validated. The source code is available at: https://anonymous.4open.science/r/mimic-report-C210/.
