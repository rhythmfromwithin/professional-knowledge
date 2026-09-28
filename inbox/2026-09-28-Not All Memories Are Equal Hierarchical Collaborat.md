---
title: "Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2609.30289
priority: high
status: unread
interest: medium
next_step: skim
---
# Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents
> 原文: [https://arxiv.org/abs/2609.30289](https://arxiv.org/abs/2609.30289)

arXiv:2609.30289v1 Announce Type: new
Abstract: In team collaboration scenarios, memory is heterogeneous and continually evolving. Team memories capture collective decisions, protocols, and current consensus, while individual memories preserve member-specific observations, execution traces, and intermediate progress. Existing memory-augmented systems typically retrieve from all stored memories as a flat pool, ranking them by semantic relevance, importance, or recency without modeling hierarchical structure or evolving validity. As a result, they often surface semantically relevant but outdated or conflicting memories, especially individual memories that no longer align with current team consensus, instead of prioritizing currently valid memories. This is particularly problematic when collaborative LLM agents answer user questions, since their responses should be grounded in valid memories. We propose HiCoMER, a framework for hierarchical collaborative memory management and validity-aware retrieval in LLM agents. HiCoMER first maintains the validity of team and individual memories and then retrieves memories that remain valid, rather than retrieving directly from all stored memories. It consists of three components: a Hierarchical Memory Conflict Updater, a Validity-Aware Memory Retriever, and a Memory-Grounded Answer Generator. To evaluate HiCoMER, we construct two new datasets for memory-grounded question answering in collaborative settings. Experiments on both datasets show that HiCoMER consistently outperforms strong baselines by reducing outdated retrieval, preserving current team consensus, and improving downstream QA quality.
