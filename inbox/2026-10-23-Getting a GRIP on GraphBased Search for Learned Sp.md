---
interest: medium
link: https://arxiv.org/abs/2610.30425
next_step: skim
priority: low
slack_ts: '1792729432.516439'
source: cs.DB - Databases
status: unread
title: Getting a GRIP on Graph-Based Search for Learned Sparse Retrieval
---
# Getting a GRIP on Graph-Based Search for Learned Sparse Retrieval
> 原文: [https://arxiv.org/abs/2610.30425](https://arxiv.org/abs/2610.30425)

arXiv:2610.30425v1 Announce Type: cross
Abstract: Learned sparse retrieval (LSR) has recently gained traction in the information retrieval community for the ability to combine the generalization capabilities of neural representations with the interpretability of keyword-based search. A number of recent works have demonstrated that inverted indexes, when appropriately modified for learned sparse embeddings, achieve state-of-the-art recall-latency tradeoffs for LSR, often outperforming graph-based indexes by substantial margins in latency at a fixed recall target. As a result, the community has generally concluded that graph-based approximate nearest neighbor (ANN) search is inferior to inverted indexes for LSR. This paper challenges this conventional wisdom. Our key insight is that, while applying standard graph-based ANN indexes out-of-the-box to sparse vectors leads to uncompetitive performance, we can overcome these shortcomings by infusing the strengths of inverted indexes into graph-based search. In particular, we introduce three techniques to accelerate graph-based LSR: (i) term-based entry point seeding, (ii) approximate routing via sparse sketching, and (iii) sparse partition-based graph construction. We combine these techniques into a new graph-based ANN system for LSR we call GRIP. On the MS MARCO v2 benchmark (138M passages) with SPLADE embeddings, GRIP achieves a $2.5\times$ latency improvement over Seismic, a state-of-the-art inverted index tailored for LSR, at 95\% recall@10. Ultimately, our results call into question the default choice of inverted indexes for deploying learned sparse retrieval.
