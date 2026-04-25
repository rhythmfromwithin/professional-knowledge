---
title: "Residual Risk Analysis in Benign Code: How Far Are We? A Multi-Model Semantic and Structural Similarity Approach"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.21051
priority: low
status: unread
interest: medium
next_step: skim
---
# Residual Risk Analysis in Benign Code: How Far Are We? A Multi-Model Semantic and Structural Similarity Approach
> 原文: [https://arxiv.org/abs/2604.21051](https://arxiv.org/abs/2604.21051)

arXiv:2604.21051v1 Announce Type: new
Abstract: Software security relies on effective vulnerability detection and patching, yet determining whether a patch fully eliminates risk remains an underexplored challenge. Existing vulnerability benchmarks often treat patched functions as inherently benign, overlooking the possibility of residual security risks. In this work, we analyze vulnerable-benign function pairs from the PrimeVul, a benchmark dataset using multiple code language models (Code LMs) to capture semantic similarity, complemented by Tree-sitter-based abstract syntax tree (AST) analysis for structural similarity. Building on these signals, we propose Residual Risk Scoring (RRS), a unified framework that integrates embedding-based semantic similarity, localized AST-based structural similarity, and cross-model agreement to estimate residual risk in code. Our analysis shows that benign functions often remain highly similar to their vulnerable counterparts both semantically and structurally, indicating potential persistence of residual risk. We further find that approximately $61\%$ of high-RRS code pairs exhibit $13$ distinct categories of residual issues (e.g., null pointer dereferences, unsafe memory allocation), validated using state-of-the-art static analysis tools including Cppcheck, Clang-Tidy, and Facebook-Infer. These results demonstrate that code-level similarity provides a practical signal for prioritizing post-patch inspection, enabling more reliable and scalable security assessment in real-world open-source software pipelines.
