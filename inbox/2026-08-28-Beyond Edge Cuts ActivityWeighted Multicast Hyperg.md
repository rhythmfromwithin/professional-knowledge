---
interest: medium
link: https://arxiv.org/abs/2608.26223
next_step: skim
priority: low
slack_ts: '1787986065.115849'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Beyond Edge Cuts: Activity-Weighted Multicast Hypergraph Mapping for Spiking
  Neural Networks on Mesh NoCs'
---
# Beyond Edge Cuts: Activity-Weighted Multicast Hypergraph Mapping for Spiking Neural Networks on Mesh NoCs
> 原文: [https://arxiv.org/abs/2608.26223](https://arxiv.org/abs/2608.26223)

arXiv:2608.26223v1 Announce Type: cross
Abstract: Mapping spiking neural networks (SNNs) onto neuromorphic many-core platforms is often formulated with graph partitioning and pairwise placement costs. That abstraction is convenient, but it does not match the physical communication event: one spike from a source neuron is delivered to a set of postsynaptic destinations, and routes to several destinations can share mesh links. We present M-HySMap, a route-aware, activity-weighted multicast hypergraph mapping framework. Each source neuron induces a directed hyperedge to its postsynaptic fanout, weighted by profiled activity. The mapper starts from strong activity-aware graph/QAP seeds and then optimizes distinct destination-core fanout, the union of deterministic mesh routes, and link congestion. The central algorithmic observation is locality: moving one neuron can change only its own source-rooted hyperedge and the hyperedges of its predecessors. This permits exact incremental gain evaluation while caching every unaffected route contribution. We expose this combinatorial structure in detail, derive a conservative placement lower bound, and describe a portfolio of partition and placement neighborhoods that preserves the best incumbent. Across a 115-job evidence suite on Potjans-inspired recurrent SNNs and mesh NoCs from 4 x 4 to 6 x 6, plus a 7 x 7 stress case, M-HySMap reduces routed multicast hops by 10.6-19.6% over Activity+QAP and 19.7-41.1% over Edge+QAP. Incremental updates accelerate refinement by 4.7-12.7x while matching full recomputation to numerical precision.
