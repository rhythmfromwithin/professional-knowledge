---
title: "StreamTGN: A GPU-Efficient Serving System for Streaming Temporal Graph Neural Networks"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.21090
priority: low
status: unread
interest: medium
next_step: skim
---
# StreamTGN: A GPU-Efficient Serving System for Streaming Temporal Graph Neural Networks
> 原文: [https://arxiv.org/abs/2603.21090](https://arxiv.org/abs/2603.21090)

arXiv:2603.21090v1 Announce Type: new
Abstract: Temporal Graph Neural Networks (TGNs) achieve state-of-the-art performance on dynamic graph tasks, yet existing systems focus exclusively on accelerating training -- at inference time, every new edge triggers $O(|V|)$ embedding updates even though only a small fraction of nodes are affected. We present \textbf{StreamTGN}, the first streaming TGN inference system exploiting the inherent locality of temporal graph updates: in an $L$-layer TGN, a new edge affects only nodes within $L$ hops of the endpoints, typically less than 0.2\% on million-node graphs. StreamTGN maintains persistent GPU-resident node memory and uses dirty-flag propagation to identify the affected set $\mathcal{A}$, reducing per-batch complexity from $O(|V|)$ to $O(|\mathcal{A}|)$ with zero accuracy loss. Drift-aware adaptive rebuild scheduling and batched streaming with relaxed ordering further maximize throughput. Experiments on eight temporal graphs (2K--2.6M nodes) show 4.5$\times$--739$\times$ speedup for TGN and up to 4,207$\times$ for TGAT, with identical accuracy. StreamTGN is orthogonal to training optimizations: combining SWIFT with StreamTGN yields 24$\times$ end-to-end speedup across three architectures (TGN, TGAT, DySAT).
