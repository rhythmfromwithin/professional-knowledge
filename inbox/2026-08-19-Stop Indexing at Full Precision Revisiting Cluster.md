---
interest: medium
link: https://arxiv.org/abs/2608.14648
next_step: skim
priority: low
slack_ts: '1787276735.287589'
source: cs.DB - Databases
status: unread
title: 'Stop Indexing at Full Precision: Revisiting Clustering for Vector Embeddings'
---
# Stop Indexing at Full Precision: Revisiting Clustering for Vector Embeddings
> 原文: [https://arxiv.org/abs/2608.14648](https://arxiv.org/abs/2608.14648)

arXiv:2608.14648v1 Announce Type: new
Abstract: In this study, we revisit three widely used techniques in vector search and utilize them to optimize vector embedding indexing through clustering: dimensionality reduction, quantization, and dimension pruning. We propose an indexing pipeline in which these techniques are applied before clustering, and we focus on how they affect storage footprint, clustering time, and the quality of the resulting centroids for vector search tasks. Our results reveal that using full-precision vectors for clustering is excessive, as even 1-bit codes can achieve near-optimal clustering quality (within 1% of ideal) while reducing storage requirements by 60x and delivering attractive performance gains (Figure 1). We open-source our implementations at https://github.com/cwida/SuperKMeans.
