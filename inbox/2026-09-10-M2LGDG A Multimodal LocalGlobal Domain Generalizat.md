---
interest: medium
link: https://arxiv.org/abs/2609.09186
next_step: skim
priority: medium
slack_ts: '1789013739.417099'
source: cs.CV - Computer Vision
status: unread
title: 'M2LG-DG: A Multi-modal Local-Global Domain Generalization Framework for Cross-site
  Major Depressive Disorder Classification'
---
# M2LG-DG: A Multi-modal Local-Global Domain Generalization Framework for Cross-site Major Depressive Disorder Classification
> 原文: [https://arxiv.org/abs/2609.09186](https://arxiv.org/abs/2609.09186)

arXiv:2609.09186v1 Announce Type: new
Abstract: Classification models based on resting-state functional magnetic resonance imaging (rs-fMRI) often show lower performance at imaging sites not included during model development, which can limit their use in clinical settings. Domain generalization (DG) addresses this issue by learning representations from source sites that remain effective for unseen target sites. However, existing DG approaches for psychiatric disorder classification commonly rely on a single imaging modality and may not fully account for site-specific acquisition effects on the learned representation space. Subjects scanned at the same site share scanner hardware, acquisition settings, and preprocessing characteristics, which can cause representations to reflect acquisition conditions rather than diagnostic information. In this work, we present M2LG-DG, a source-only multimodal local-global framework for cross-site major depressive disorder (MDD) classification. The framework employs a dual-stream rs-fMRI encoder, where the global pathway models inter-regional dependencies through self-attention and the local pathway performs graph-constrained aggregation over functional connectivity-derived brain graphs. Imaging and non-imaging representations are decomposed into shared and private components and integrated through bidirectional cross-attention with a learned modality gate. A cross-site supervised contrastive objective forms positive pairs from same-class subjects acquired at different source sites, encouraging the fused representation to preserve diagnostic information across acquisition domains. On four held-out REST-meta-MDD sites, M2LG-DG achieves an AUC of 69.48% and exceeds the closest comparison method by 2.18 percentage points. Experiments on the Autism Brain Imaging Data Exchange (ABIDE) dataset further support its applicability to other psychiatric neuroimaging classification tasks.
