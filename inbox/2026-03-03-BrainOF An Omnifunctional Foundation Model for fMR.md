---
interest: medium
link: https://arxiv.org/abs/2602.23410
next_step: skim
priority: low
slack_ts: '1773196769.275069'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG'
---
# Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG
> 原文: [https://arxiv.org/abs/2602.23410](https://arxiv.org/abs/2602.23410)

arXiv:2602.23410v1 Announce Type: cross
Abstract: Brain foundation models have achieved remarkable advances across a wide range of neuroscience tasks. However, most existing models are limited to a single functional modality, restricting their ability to exploit complementary spatiotemporal dynamics and the collective data scale across imaging techniques. To address this limitation, we propose Brain-OF, the first omnifunctional brain foundation model jointly pretrained on fMRI, EEG and MEG, capable of handling both unimodal and multimodal inputs within a unified framework. To reconcile heterogeneous spatiotemporal resolutions, we introduce the Any-Resolution Neural Signal Sampler, which projects diverse brain signals into a shared semantic space.To further manage semantic shifts, the Brain-OF backbone integrates DINT attention with a Sparse Mixture of Experts, where shared experts capture modality-invariant representations and routed experts specialize in modality-specific semantics. Furthermore, we propose Masked Temporal-Frequency Modeling, a dual-domain pretraining objective that jointly reconstructs brain signals in both the time and frequency domains. Brain-OF is pretrained on a large-scale corpus comprising around 40 datasets and demonstrates superior performance across diverse downstream tasks, highlighting the benefits of joint multimodal integration and dual-domain pretraining.
