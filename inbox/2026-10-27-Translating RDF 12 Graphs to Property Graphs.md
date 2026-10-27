---
title: "Translating RDF 1.2 Graphs to Property Graphs"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.33499
priority: low
status: unread
interest: medium
next_step: skim
---
# Translating RDF 1.2 Graphs to Property Graphs
> 原文: [https://arxiv.org/abs/2610.33499](https://arxiv.org/abs/2610.33499)

arXiv:2610.33499v1 Announce Type: new
Abstract: RDF 1.2 introduces statement-level constructs, such as triple terms, reifiers, and descriptions, that pose new challenges for transforming RDF data into labeled property graphs (LPGs). This work presents and compares three algorithms for translating RDF 1.2 data into LPGs, each interpreting a different amount of the RDF 1.2 reification vocabulary. Algorithm Structural interprets no vocabulary and losslessly supports arbitrary RDF 1.2 graphs by representing triple terms explicitly as nodes; Direct interprets rdf:reifies to recover annotated edges while preserving reifiers as graph objects; and Fold additionally folds reifier descriptions into edge properties, resulting in a more concise, albeit lossy, LPG representation. We define the three translations, analyze which class of RDF 1.2 graphs each preserves, and experimentally evaluate their implementations. The experiments confirm the predicted trade-offs: all variants scale linearly on the tested workloads, the generality of Structural has no runtime penalty, and folding descriptions into edge records can significantly reduce the number of edges on description-heavy data.
