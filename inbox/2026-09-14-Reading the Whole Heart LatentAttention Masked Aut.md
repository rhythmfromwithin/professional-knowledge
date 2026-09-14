---
title: "Reading the Whole Heart: Latent-Attention Masked Autoencoders for Multimodal Cardiac Representation Learning"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2609.12035
priority: high
status: unread
interest: medium
next_step: skim
---
# Reading the Whole Heart: Latent-Attention Masked Autoencoders for Multimodal Cardiac Representation Learning
> 原文: [https://arxiv.org/abs/2609.12035](https://arxiv.org/abs/2609.12035)

arXiv:2609.12035v1 Announce Type: new
Abstract: Cardiovascular diagnosis rests on integrating complementary modalities, like ECG, echocardiography, chest radiographs, and clinical variables, each capturing distinct but correlated aspects of cardiac physiology. Yet most medical foundation models remain modality-specific, combining modalities only for finetuning or post-training. This discards the cross-modal evidence clinicians naturally integrate and ignores the structure within each modality. We introduce Latent-Attention Masked Autoencoders (LAMAE), a multimodal, structure-aware masked autoencoder that jointly learns patient-level representations during self-supervised pretraining. Rather than fusing modalities post hoc, LAMAE exchanges information directly in the latent space through a shared latent-attention module operating over a study-view-entity hierarchy, enabling aggregation of variable observations and graceful handling of missing modalities. Pretrained on over 1.2 million MIMIC-IV hospital stays, LAMAE outperforms modality-specific pretraining and strong contrastive and vision-language baselines across multimodal hospital-stay tasks, such as in-hospital mortality, ICD-10 and DRG coding, and length of stay, while remaining competitive on unimodal tasks. These gains persist even when only a single modality is available at test time, showing that modeling both intra- and inter-modal structure yields more robust, transferable representations.
