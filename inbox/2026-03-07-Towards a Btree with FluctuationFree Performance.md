---
title: "Towards a B+-tree with Fluctuation-Free Performance"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.04785
priority: low
status: unread
interest: medium
next_step: skim
---
# Towards a B+-tree with Fluctuation-Free Performance
> 原文: [https://arxiv.org/abs/2603.04785](https://arxiv.org/abs/2603.04785)

arXiv:2603.04785v1 Announce Type: new
Abstract: Performance predictability is critical for modern DBMSs because index maintenance can trigger rare but severe I/O spikes. In a B or B+-tree with height H, node split propagation means the cost of a single insert can vary from H + 1 to 3H + 1 I/Os when splits reach the root, nearly a three times degradation. We formalize performance fluctuation as the gap between best- and worst-case insert behavior and introduce the notions of safe and critical nodes to capture when splits become unavoidable. We introduce the FFBtree, a B+-tree insert algorithm that preemptively splits some critical nodes, and prove that when navigating from root to leaf the insert algorithm will encounter at most one critical node that must be split, ensuring no split propagation can occur and producing fluctuation-free performance. Our implementation maintains critical-node metadata efficiently and integrates with optimistic lock coupling for concurrency. Experiments with simulated indexes show the FFBtree caps I/O fluctuation by eliminating split propagation and consistently reduces insert spikes compared to conventional baselines, and real-index experiments confirm comparable improvements.
