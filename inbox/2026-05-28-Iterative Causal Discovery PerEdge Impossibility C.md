---
title: "Iterative Causal Discovery: Per-Edge Impossibility Certificates, Tier-Aware Oracle Queries, and the $1+K$ Lower Bound"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.27477
priority: medium
status: unread
interest: medium
next_step: skim
---
# Iterative Causal Discovery: Per-Edge Impossibility Certificates, Tier-Aware Oracle Queries, and the $1+K$ Lower Bound
> 原文: [https://arxiv.org/abs/2605.27477](https://arxiv.org/abs/2605.27477)

arXiv:2605.27477v1 Announce Type: new
Abstract: Causal-discovery algorithms return a directed graph, yet provide no principled means of distinguishing edge directions identified by the data from those assigned without an identifying assumption. Under the standard Markov and faithfulness conditions, the observational distribution identifies only a Markov equivalence class; orientations within that class are not determined by the joint distribution and cannot be recovered from additional samples alone, but require either a functional restriction or an intervention. We introduce a protocol for observational causal discovery on continuous data that attaches to each candidate edge a discrete impossibility certificate: a RESOLVED code records the identifiability theorem under which the direction was committed, while an IMPOSSIBLE code records the failure mode together with the specific question a domain expert must answer to resolve it. The bivariate cascade is extended with five gated identifiability tiers LSNM, IGCI, Stein, MDL, and PEIT that abstain when their precondition test rejects. Two oracle primitives, the meta-hub query and the node-children query, jointly establish an upper bound of $1+K$ expert interactions sufficient to recover any DAG, where $K$ denotes the number of non-leaf vertices. Under an ideal-oracle assumption, the bound is met exactly on the asia, sachs, child, and alarm benchmarks.
