---
title: "Algorithm Selection with Zero Domain Knowledge via Text Embeddings"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2604.19753
priority: high
status: unread
interest: medium
next_step: skim
---
# Algorithm Selection with Zero Domain Knowledge via Text Embeddings
> 原文: [https://arxiv.org/abs/2604.19753](https://arxiv.org/abs/2604.19753)

arXiv:2604.19753v1 Announce Type: new
Abstract: We propose a feature-free approach to algorithm selection that replaces hand-crafted instance features with pretrained text embeddings. Our method, ZeroFolio, proceeds in three steps: it reads the raw instance file as plain text, embeds it with a pretrained embedding model, and selects an algorithm via weighted k-nearest neighbors. The key to our approach is the observation that pretrained embeddings produce representations that distinguish problem instances without any domain knowledge or task-specific training. This allows us to apply the same three-step pipeline (serialize, embed, select) across diverse problem domains with text-based instance formats. We evaluate our approach on 11 ASlib scenarios spanning 7 domains (SAT, MaxSAT, QBF, ASP, CSP, MIP, and graph problems). Our experiments show that this approach outperforms a random forest trained on hand-crafted features in 10 of 11 scenarios with a single fixed configuration, and in all 11 with two-seed voting; the margin is often substantial. Our ablation study shows that inverse-distance weighting, line shuffling, and Manhattan distance are the key design choices. On scenarios where both selectors are competitive, combining embeddings with hand-crafted features via soft voting yields further improvements.
