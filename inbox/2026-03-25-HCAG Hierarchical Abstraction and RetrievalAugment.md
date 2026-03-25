---
title: "HCAG: Hierarchical Abstraction and Retrieval-Augmented Generation on Theoretical Repositories with LLMs"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.20299
priority: low
status: unread
interest: medium
next_step: skim
---
# HCAG: Hierarchical Abstraction and Retrieval-Augmented Generation on Theoretical Repositories with LLMs
> 原文: [https://arxiv.org/abs/2603.20299](https://arxiv.org/abs/2603.20299)

arXiv:2603.20299v1 Announce Type: new
Abstract: Existing Retrieval-Augmented Generation (RAG) methods for code struggle to capture the high-level architectural patterns and cross-file dependencies inherent in complex, theory-driven codebases, such as those in algorithmic game theory (AGT), leading to a persistent semantic and structural gap between abstract concepts and executable implementations. To address this challenge, we propose Hierarchical Code/Architecture-guided Agent Generation (HCAG), a framework that reformulates repository-level code generation as a structured, planning-oriented process over hierarchical knowledge. HCAG adopts a two-phase design: an offline hierarchical abstraction phase that recursively parses code repositories and aligned theoretical texts to construct a multi-resolution semantic knowledge base explicitly linking theory, architecture, and implementation; and an online hierarchical retrieval and scaffolded generation phase that performs top-down, level-wise retrieval to guide LLMs in an architecture-then-module generation paradigm. To further improve robustness and consistency, HCAG integrates a multi-agent discussion inspired by cooperative game. We provide a theoretical analysis showing that hierarchical abstraction with adaptive node compression achieves cost-optimality compared to flat and iterative RAG baselines. Extensive experiments on diverse game-theoretic system generation tasks demonstrate that HCAG substantially outperforms representative repository-level methods in code quality, architectural coherence, and requirement pass rate. In addition, HCAG produces a large-scale, aligned theory-implementation dataset that effectively enhances domain-specific LLMs through post-training. Although demonstrated in AGT, HCAG paradigm also offers a general blueprint for mining, reusing, and generating complex systems from structured codebases in other domains.
