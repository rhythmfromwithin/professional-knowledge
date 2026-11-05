---
title: "Turbocharging PiPNN for Proximity and $k$-NN Graph Building"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2611.05690
priority: low
status: unread
interest: medium
next_step: skim
---
# Turbocharging PiPNN for Proximity and $k$-NN Graph Building
> 原文: [https://arxiv.org/abs/2611.05690](https://arxiv.org/abs/2611.05690)

arXiv:2611.05690v1 Announce Type: new
Abstract: Graph-based Approximate Nearest Neighbor Search (ANNS) indexes such as HNSW and Vamana deliver state-of-the-art query performance at the cost of large indexing times. The recently introduced PiPNN method drastically accelerated index construction by way of a partitioning-based algorithm leveraging dense matrix multiplication and top-$K$ aggregation kernels.
In this paper, we unlock the full potential of PiPNN's hardware-friendly algorithm design. We introduce PiPNN II, which optimizes multiple steps of the PiPNN recipe, giving up to $8\times$ speedups for graph-based ANNS index construction. In addition, we present GPiPNN, a GPU implementation which builds comparable ANNS indices up to $43.7\times$ faster than Jasper and up to $50\times$ faster than CAGRA. We also extend PiPNN II and GPiPNN to compute high-quality $k$-NN graphs directly, which unlocks massive speedups over methods used in many existing systems for clustering, anomaly detection, and more. For 10-NN graph building at $90\%$ recall, we obtain up to a $13\times$ speedup on CPUs and $6.6\times$ on GPUs as compared to the prior best methods. PiPNN II can build a billion-scale 10-NN graph in under 16 minutes.
Common to both PiPNN II and GPiPNN is the use of quantization to reduce memory traffic and leverage fast low-precision matrix operations. Top-$K$ emerges as a new bottleneck, which we optimize with specialized code for specific $K$, and by fusing with the matrix kernel to avoid materializing the distance matrix to memory. On CPUs, we demonstrate further performance improvements by leveraging our matrix kernels in the RobustPrune procedure proposed in Vamana and used in PiPNN. On GPUs, we flatten recursive partitioning into segmented batches, use one fused top-$K$ abstraction for partitioning and leaf scoring, and prune with already-witnessed direct edges rather than new candidate-to-candidate scoring passes.
