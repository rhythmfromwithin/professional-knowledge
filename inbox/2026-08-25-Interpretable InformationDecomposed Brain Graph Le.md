---
interest: medium
link: https://arxiv.org/abs/2608.20380
next_step: skim
priority: low
slack_ts: '1787708792.041459'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Interpretable Information-Decomposed Brain Graph Learning for fMRI-based Disease
  Diagnosis
---
# Interpretable Information-Decomposed Brain Graph Learning for fMRI-based Disease Diagnosis
> 原文: [https://arxiv.org/abs/2608.20380](https://arxiv.org/abs/2608.20380)

arXiv:2608.20380v1 Announce Type: new
Abstract: Resting-state functional magnetic resonance imaging (rs-fMRI) has enabled non-invasive mapping of functional brain interactions for computer-aided diagnosis, yet most existing approaches reduce inter-regional relationships to correlation-based edge weights. Such representations capture co-fluctuation strength but obscure how information is shared across brain regions. Because brain disorders may disrupt not only connectivity strength but also the organization of redundancy, uniqueness and synergy, traditional functional connectivity may miss disease-relevant information structures. Here we introduce IID-GCN, an interpretable graph learning framework that decomposes rs-fMRI interactions into redundancy, uniqueness and synergy graphs using partial entropy decomposition. These information-specific graphs separately characterize shared, region-specific and jointly emergent components of brain activity. A multi-channel graph convolutional network then integrates the decomposed graphs through edge recalibration, cross-information interaction, ROI-attention readout and channel-attentive fusion. Across three datasets, IID-GCN consistently captures complementary diagnostic information beyond traditional functional connectivity. The learned information profiles reveal disorder-specific patterns of altered redundancy, uniqueness and synergy, suggesting that brain diseases reshape functional information organization rather than merely changing connection strength. These results establish information-decomposed brain graphs as an interpretable representation for rs-fMRI-based diagnosis. Our code is available at https://github.com/Zdy12/IID-GCN.
