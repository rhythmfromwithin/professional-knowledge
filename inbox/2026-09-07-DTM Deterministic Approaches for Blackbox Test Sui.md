---
title: "DTM: Deterministic Approaches for Black-box Test Suite Minimization with Tree-based Similarity"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2609.04205
priority: low
status: unread
interest: medium
next_step: skim
---
# DTM: Deterministic Approaches for Black-box Test Suite Minimization with Tree-based Similarity
> 原文: [https://arxiv.org/abs/2609.04205](https://arxiv.org/abs/2609.04205)

arXiv:2609.04205v1 Announce Type: new
Abstract: Black-box Test Suite Minimization (TSM) techniques reduce testing costs without requiring access to production code. However, existing effective approaches rely on evolutionary search algorithms, introducing non-determinism that produces inconsistent results across runs, undermining reliability in automated testing pipelines. We propose DTM (Deterministic approaches for black-box Test suite Minimization), a framework that ensures deterministic test suite reduction while preserving effectiveness and efficiency. DTM converts test cases into Abstract Syntax Trees and computes pairwise similarities using four tree-based measures. For subset selection, it employs three deterministic algorithms: Modified Minimum Spanning Tree, Spectral Clustering, and Dynamic Programming. We evaluated DTM on 16 Java projects from Defects4J with 661 buggy versions. Experimental results show that DTM achieved an average accuracy of 0.74 with an execution time of just 0.98 minutes, outperforming all state-of-the-art approaches. Moreover, it consistently produced identical results across multiple runs, ensuring full determinism.
