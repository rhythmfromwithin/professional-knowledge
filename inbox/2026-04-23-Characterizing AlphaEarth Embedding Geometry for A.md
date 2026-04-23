---
interest: medium
link: https://arxiv.org/abs/2604.18715
next_step: skim
priority: high
slack_ts: '1776915199.848419'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Characterizing AlphaEarth Embedding Geometry for Agentic Environmental Reasoning
---
# Characterizing AlphaEarth Embedding Geometry for Agentic Environmental Reasoning
> 原文: [https://arxiv.org/abs/2604.18715](https://arxiv.org/abs/2604.18715)

arXiv:2604.18715v1 Announce Type: new
Abstract: Earth observation foundation models encode land surface information into dense embedding vectors, yet the geometric structure of these representations and its implications for downstream reasoning remain underexplored. We characterize the manifold geometry of Google AlphaEarth's 64-dimensional embeddings across 12.1 million Continental United States samples (2017--2023) and develop an agentic system that leverages this geometric understanding for environmental reasoning. The manifold is non-Euclidean: effective dimensionality is 13.3 (participation ratio) from 64 raw dimensions, with local intrinsic dimensionality of approximately 10. Tangent spaces rotate substantially, with 84\% of locations exceeding 60\textdegree{} and local-global alignment (mean$|\cos\theta| = 0.17$) approaching the random baseline of 0.125. Supervised linear probes indicate that concept directions rotate across the manifold, and compositional vector arithmetic using both PCA-derived and probe-derived directions yields poor precision. Retrieval instead produces physically coherent results, with local geometry predicting retrieval coherence ($R^2 = 0.32$). Building on this characterization, we introduce an agentic system with nine specialized tools that decomposes environmental queries into reasoning chains over a FAISS-indexed embedding database. A five-condition ablation (120 queries, three complexity tiers) shows that embedding retrieval dominates response quality ($\mu = 3.79 \pm 0.90$ vs.\ $3.03 \pm 0.77$ parametric-only; scale 1--5), with peak performance on multi-step comparisons ($\mu = 4.28 \pm 0.43$). A cross-model benchmark show that geometric tools reduce Sonnet 4.5's score by 0.12 points but improve Opus 4.6's by 0.07, with Opus achieving higher geometric grounding (3.38 vs.\ 2.64), suggesting that the value of geometric characterization scales with the reasoning capability of the consuming model.
