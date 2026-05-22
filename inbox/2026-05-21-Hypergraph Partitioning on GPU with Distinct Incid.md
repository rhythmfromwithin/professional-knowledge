---
interest: medium
link: https://arxiv.org/abs/2605.20497
next_step: skim
priority: medium
slack_ts: '1779423493.277489'
source: cs.DC - Distributed Computing
status: unread
title: Hypergraph Partitioning on GPU with Distinct Incident Hyperedges and Size Constraints
---
# Hypergraph Partitioning on GPU with Distinct Incident Hyperedges and Size Constraints
> 原文: [https://arxiv.org/abs/2605.20497](https://arxiv.org/abs/2605.20497)

arXiv:2605.20497v1 Announce Type: new
Abstract: Hypergraph partitioning is a recurring NP-hard problem in engineering; its efficient solution at scale hinges on parallelism. This work proposes a GPU-centric algorithm for multi-level hypergraph partitioning aimed at a specific set of problem constraints: limited size and distinct inbound hyperedges per partition. Manipulating hypergraphs requires deeply nested traversals and concurrent decision-making; our constraints impose further set operations amidst that. In turn, we design algorithms around the GPU's hierarchical parallelism and our problem's specifics. When forming partitions, we materialize the hypergraph's incidence structure and unique neighborhoods in memory to exploit set sparsity and batch node-pairing scores in shared memory. Upon refining partitions, we chain node moves into improving paths and cycles, checking their validity via cumulative set size variations reduced in parallel over moves. Thus, our dominant kernels exhibit a span linear in local hypergraph parameters. Results show an average 380x speedup and a 1.2-2.0x reduction in connectivity compared to a sequential multi-level partitioner. With minor changes, we also support k-way balanced partitioning, running 5x faster than CPU methods with a ~5% quality loss for k=2, outperforming an existing GPU partitioner at comparable runtime, with no measurable overhead from the added constraints handling logic.
