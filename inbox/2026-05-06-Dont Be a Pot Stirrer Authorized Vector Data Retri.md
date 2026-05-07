---
interest: medium
link: https://arxiv.org/abs/2605.01342
next_step: skim
priority: low
slack_ts: '1778125801.188969'
source: cs.DB - Databases
status: unread
title: Don't Be a Pot Stirrer! Authorized Vector Data Retrieval via Access-Aware Indexing
---
# Don't Be a Pot Stirrer! Authorized Vector Data Retrieval via Access-Aware Indexing
> 原文: [https://arxiv.org/abs/2605.01342](https://arxiv.org/abs/2605.01342)

arXiv:2605.01342v1 Announce Type: new
Abstract: Vector databases increasingly enforce role-based access control: each top-k approximate nearest neighbor query must return only vectors the querying role is authorized to access. Two extremes bracket the design space. A single global index avoids data duplication but wastes search effort on unauthorized vectors and degrades recall, while an oracle index, built with all authorized vectors of the query roles, searches only authorized vectors but duplicates every shared vector between roles or queries. We present Veda and its efficient variant EffVeda, two indexing strategies built on an access-aware lattice to address access control in vector databases. The methods first partitions the dataset into disjoint data blocks by role combination, then leverage the structure of the access-aware lattice to apply copy and merge operations to group co-accessed blocks under a user-specified storage budget. Large nodes in the lattice are then indexed with HNSW, while small nodes are retained for linear scan. For each role, our methods construct a query plan that selects the minimal set of nodes that covers the role's authorized data. At query time, coordinated search first queries pure (authorized-only) nodes to populate a global top-k heap. The resulting distance bound then prunes exploration on impure nodes, avoiding the inflated search that independent per-index execution would require.
