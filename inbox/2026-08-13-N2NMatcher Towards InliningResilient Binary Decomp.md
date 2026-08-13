---
title: "N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.10043
priority: low
status: unread
interest: medium
next_step: skim
---
# N2NMatcher: Towards Inlining-Resilient Binary Decomposition and Module Matching
> 原文: [https://arxiv.org/abs/2608.10043](https://arxiv.org/abs/2608.10043)

arXiv:2608.10043v1 Announce Type: new
Abstract: Program-level Binary Code Similarity Analysis (BCSA) aims to identify semantically similar code regions across binary programs, serving as a fundamental technique for software plagiarism detection, vulnerability search, and malware analysis. Existing approaches often decompose binaries into modules following the structure of function call graphs (FCGs) and then match these modules by their contained functions. However, function inlining changes both FCG structures and binary function semantics, making existing decomposition and module matching methods less effective.
In this work, we propose N2NMatcher, an inlining-resilient framework for binary decomposition and module matching. We first conduct an empirical study to examine whether binaries still contain functions that provide stable module boundaries across compilation settings. N2NMatcher learns to predict such functions as anchors using a hierarchical graph neural network that encodes binary ACFG-FCG representations built from opcode sequences, control-flow structures, and FCG calling context. It then performs anchor-bounded decomposition and matches the generated modules using learned module graph embeddings. Experimental results show that N2NMatcher improves both the decomposition quality and module matching accuracy compared to existing works, enabling more effective program-level BCSA.
