---
title: "KSE-Web: An Analysis of Hybrid Retrieval and LLM-Assisted Query Expansion for Low-Resource Khmer Semantic Search"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.21365
priority: high
status: unread
interest: medium
next_step: skim
---
# KSE-Web: An Analysis of Hybrid Retrieval and LLM-Assisted Query Expansion for Low-Resource Khmer Semantic Search
> 原文: [https://arxiv.org/abs/2608.21365](https://arxiv.org/abs/2608.21365)

arXiv:2608.21365v1 Announce Type: new
Abstract: As a low-resource language, Khmer presents several retrieval challenges, including limited annotated data, ambiguous word boundaries, weak support in multilingual embedding models, and frequent mixed Khmer-English usage. This paper presents KSE-Web, an analysis of hybrid retrieval and LLM-assisted query expansion for Khmer semantic search. We construct the dataset from approximately 17K candidate Khmer titles and retain 3K cleaned full-text Khmer documents after filtering, normalization, deduplication, and document-length control. The dataset includes 300 manually reviewed user-style Khmer search queries and silver relevance labels with partial human verification. We evaluate character n-gram BM25, multilingual dense retrieval, hybrid BM25+dense retrieval, and LLM-assisted query expansion using Qwen2.5 models. Experimental results show that BM25 achieves the strongest overall performance, reaching 0.943 Recall and 0.876 nDCG. Hybrid BM25+dense retrieval performs comparably, achieving 0.929 Recall and 0.871 nDCG, while dense retrieval alone performs lower. LLM-assisted query expansion does not outperform non-expanded retrieval; however, Qwen2.5-3B produces substantially stronger expanded-query results than Qwen2.5-0.5B, suggesting that LLM size and expansion quality matter for low-resource Khmer retrieval. Our analysis further shows that direct LLM expansion can introduce topic drift, generic terms, and noisy reformulations, while simple filtering may remove useful semantic cues. These findings highlight both the potential and limitations of LLM-assisted retrieval for Khmer semantic search and provide a foundation for future Khmer retrieval datasets with stronger human-verified annotations and Khmer-aware retrieval models. The dataset and documentation will be made available at github.com/back-kh/KhmerSemantic-Search.
