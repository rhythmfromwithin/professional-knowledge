---
interest: medium
link: https://arxiv.org/abs/2603.06593
next_step: skim
priority: high
slack_ts: '1773456123.935759'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Hierarchical Embedding Fusion for Retrieval-Augmented Code Generation
---
# Hierarchical Embedding Fusion for Retrieval-Augmented Code Generation
> 原文: [https://arxiv.org/abs/2603.06593](https://arxiv.org/abs/2603.06593)

arXiv:2603.06593v1 Announce Type: new
Abstract: Retrieval-augmented code generation often conditions the decoder on large retrieved code snippets. This ties online inference cost to repository size and introduces noise from long contexts. We present Hierarchical Embedding Fusion (HEF), a two-stage approach to repository representation for code completion. First, an offline cache compresses repository chunks into a reusable hierarchy of dense vectors using a small fuser model. Second, an online interface maps a small number of retrieved vectors into learned pseudo-tokens that are consumed by the code generator. This replaces thousands of retrieved tokens with a fixed pseudo-token budget while preserving access to repository-level information.
On RepoBench and RepoEval, HEF with a 1.8B-parameter pipeline achieves exact-match accuracy comparable to snippet-based retrieval baselines, while operating at sub-second median latency on a single A100 GPU. Compared to graph-based and iterative retrieval systems in our experimental setup, HEF reduces median end-to-end latency by 13 to 26 times. We also introduce a utility-weighted likelihood signal for filtering training contexts and report ablation studies on pseudo-token budget, embedding models, and robustness to harmful retrieval. Overall, these results indicate that hierarchical dense caching is an effective mechanism for low-latency, repository-aware code completion.
