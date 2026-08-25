---
title: "Ghost Echoes: Semantic Erasure Failure in Retrieval-Backed Applications"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.20352
priority: low
status: unread
interest: medium
next_step: skim
---
# Ghost Echoes: Semantic Erasure Failure in Retrieval-Backed Applications
> 原文: [https://arxiv.org/abs/2608.20352](https://arxiv.org/abs/2608.20352)

arXiv:2608.20352v1 Announce Type: new
Abstract: Although vector databases correctly implement API-visible deletion, this does not guarantee complete semantic erasure for retrieval-backed applications. We present Ghost Echoes, a black-box attack framework showing that deleted records can leave measurable residual influence on downstream retrieval contexts. Our primary finding is the RAG retrieval-context drift effect where even when a target record is correctly excluded from query results, its prior presence perturbs the semantic centroid and textual composition of the Top-K evidence base. We approximate the unobservable never-inserted counterfactual using a same-cluster non-target deletion control that preserves local neighborhood structure while isolating target-specific effects from generic local drift. Evaluation on ChromaDB confirms target deletion produces a median retrieval-centroid drift of 0.1522, exceeding the same-cluster baseline in 53/54 paired comparisons (p < 0.001), and the signal remains detectable with 61.1% accuracy at a query budget of q = 5. We verify API-visible deletion correctness across evaluated backends and observe the same qualitative drift ordering in matched FAISS replication. Under the evaluated settings, tested operational mitigations such as full index rebuilds fail to eliminate the measured drift. These results establish a measurable 'verification gap' between interface-level deletion compliance and true semantic erasure, and motivate erasure primitives that act not only on stored identifiers, but also on the retrieval topology of the system.
