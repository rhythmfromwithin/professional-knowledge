---
interest: medium
link: https://arxiv.org/abs/2605.14464
next_step: skim
priority: low
slack_ts: '1778990764.803799'
source: cs.DB - Databases
status: unread
title: 'From Schema to Signal: Retrieval-Augmented Modeling for Relational Data Analytics'
---
# From Schema to Signal: Retrieval-Augmented Modeling for Relational Data Analytics
> 原文: [https://arxiv.org/abs/2605.14464](https://arxiv.org/abs/2605.14464)

arXiv:2605.14464v1 Announce Type: new
Abstract: Relational data stored in RDBMS is foundational to many real-world applications across domains such as e-commerce, finance, and sociality. While deep neural networks (DNNs) have achieved strong performance on tabular data with a single table, extending these models to relational databases is challenging due to the normalized multi-table structure and complex inter-table relationships. Existing approaches often rely strictly on schema-defined graphs, which overlook implicit semantic signals embedded in tuple attributes and suffer from rigid connectivity.
In this work, we propose Retrieval-Augmented Modeling (RAM), a novel framework that combines graph structure with attribute semantics for relational data analytics. RAM treats tuple attributes as tokens and uses random walks to construct contextual documents, enabling the use of information retrieval techniques to estimate semantic relevance between tuples. Building on these documents, we introduce two retrieval-based augmentations: ATRA, which leverages intra-table relevance for contrastive learning, and ETRA, which links semantically related tuples across tables to enhance graph connectivity. Then, we propose a layer-wise model architecture tailored for relational data, which involves attribute embedding, feature integration, and graph aggregation layers to enable expressive and flexible representation learning. Extensive experiments on five real-world relational databases demonstrate that RAM consistently outperforms existing baselines in diverse prediction tasks, establishing a state-of-the-art for relational data analytics.
