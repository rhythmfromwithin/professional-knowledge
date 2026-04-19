---
interest: medium
link: https://arxiv.org/abs/2604.14411
next_step: skim
priority: medium
slack_ts: '1776569845.455079'
source: cs.DC - Distributed Computing
status: unread
title: Incidence Constraints in Hypergraph Partitioning on GPU
---
# Incidence Constraints in Hypergraph Partitioning on GPU
> 原文: [https://arxiv.org/abs/2604.14411](https://arxiv.org/abs/2604.14411)

arXiv:2604.14411v1 Announce Type: new
Abstract: Hypergraph partitioning is a pervasive NP-hard problem, and accelerating its computation on GPU can both slice time-to-solution and raise quality of results. In this work, we implement a multi-level hypergraph partitioning algorithm on GPU targeting a specific set of problem constraints: bounded per-partition size and distinct inbound hyperedges. Manipulating hypergraphs requires long orders of nested iterations, and enforcing these constraints introduces further set operations amidst them. Hence, we design algorithms around our problem's specifics, materializing the hypergraph's incidence structure in memory and exploiting set sparsity. Our results show competitive speedups as high as 940x and 2-26% better results in connectivity over a sequential multi-level partitioner.
