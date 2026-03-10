---
title: "Universal Conceptual Structure in Neural Translation: Probing NLLB-200's Multilingual Geometry"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.02258
priority: high
status: unread
interest: medium
next_step: skim
---
# Universal Conceptual Structure in Neural Translation: Probing NLLB-200's Multilingual Geometry
> 原文: [https://arxiv.org/abs/2603.02258](https://arxiv.org/abs/2603.02258)

arXiv:2603.02258v1 Announce Type: new
Abstract: Do neural machine translation models learn language-universal conceptual representations, or do they merely cluster languages by surface similarity? We investigate this question by probing the representation geometry of Meta's NLLB-200, a 200-language encoder-decoder Transformer, through six experiments that bridge NLP interpretability with cognitive science theories of multilingual lexical organization. Using the Swadesh core vocabulary list embedded across 135 languages, we find that the model's embedding distances significantly correlate with phylogenetic distances from the Automated Similarity Judgment Program ($\rho = 0.13$, $p = 0.020$), demonstrating that NLLB-200 has implicitly learned the genealogical structure of human languages. We show that frequently colexified concept pairs from the CLICS database exhibit significantly higher embedding similarity than non-colexified pairs ($U = 42656$, $p = 1.33 \times 10^{-11}$, $d = 0.96$), indicating that the model has internalized universal conceptual associations. Per-language mean-centering of embeddings improves the between-concept to within-concept distance ratio by a factor of 1.19, providing geometric evidence for a language-neutral conceptual store analogous to the anterior temporal lobe hub identified in bilingual neuroimaging. Semantic offset vectors between fundamental concept pairs (e.g., man to woman, big to small) show high cross-lingual consistency (mean cosine = 0.84), suggesting that second-order relational structure is preserved across typologically diverse languages. We release InterpretCognates, an open-source interactive toolkit for exploring these phenomena, alongside a fully reproducible analysis pipeline.
