---
interest: medium
link: https://arxiv.org/abs/2608.25466
next_step: skim
priority: low
slack_ts: '1787914964.805939'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Homo-RAG: Homology-Guided Retrieval-Augmented Generation for Cross-Species
  Gene Function Prediction'
---
# Homo-RAG: Homology-Guided Retrieval-Augmented Generation for Cross-Species Gene Function Prediction
> 原文: [https://arxiv.org/abs/2608.25466](https://arxiv.org/abs/2608.25466)

arXiv:2608.25466v1 Announce Type: new
Abstract: The functional annotation of genes in non-model organisms remains a significant challenge in computational biology, with 20-70% of sequenced genes lacking characterized functions. Traditional homology-based methods are often costly and strongly dependent on high sequence similarity. This study presents Homo-RAG, a framework for large language model-based gene function prediction that integrates homology-guided multi-hop retrieval with evidence-aware ranking. The framework exploits biological relationships between zebrafish and human orthologs to guide evidence acquisition from ZFIN, UniProt, and PubMed through hybrid dense and lexical retrieval. An Evidence Confidence Score (ECS) integrates semantic relevance, entity matching, orthology information, source reliability, and literature association signals to refine the ranking of retrieved evidence. Extensive evaluation across 150 queries and 7,200 retrieved documents shows that evidence weighting parameter of lambda=0.50 improves NDCG@10 to 0.9879 and MRR to 0.99, while retrieving relevant evidence for 99.33% of queries. Furthermore, 80% of the retrieved documents are query-exclusive, indicating that evidence quality complements rather than replaces retrieval relevance. These findings establish Homo-RAG as a practical and robust framework for reliable, evidence-grounded gene function prediction in understudied organisms. The study addresses important limitations of conventional annotation pipelines while identifying opportunities for future improvements in evidence features and attribution mechanisms.
