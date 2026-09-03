---
interest: medium
link: https://arxiv.org/abs/2609.00054
next_step: skim
priority: high
slack_ts: '1788408227.203059'
source: cs.LG - Machine Learning
status: unread
title: Convergence issues in Relational Concept Analysis based on AOC-posets
---
# Convergence issues in Relational Concept Analysis based on AOC-posets
> 原文: [https://arxiv.org/abs/2609.00054](https://arxiv.org/abs/2609.00054)

arXiv:2609.00054v1 Announce Type: new
Abstract: Formal Concept Analysis (FCA) is an approach for conceptual classification building and rule discovery from a binary table describing a set of objects by a set of attributes. Extensions have been proposed to deal with non-binary and more complex data, such as Relational Concept Analysis (RCA) for multi-relational data. RCA aims to highlight groups of objects characterized by their relationships with other groups of objects. The richer and more complex nature of the underlying data allows RCA to produce richer results than FCA, at the expense of higher computational and interpretive complexity. The most commonly used conceptual classification structure in FCA is the concept lattice. However, in many applications, concept lattice substructures, such as AOC-posets, are preferred over the full lattice, either to mitigate combinatorial blow-up or to focus on the most informative parts of the structure. Indeed, in an AOC-poset, only concepts introducing an object or an attribute are represented, which makes AOC-posets smaller and easier to compute and use than concept lattices. Although RCA was originally defined on concept lattices, it can also be instantiated on AOC-posets. RCA is iterative and its convergence is guaranteed in the lattice-based setting, but this guarantee is lost when using AOC-posets. In this paper, we investigate this loss of convergence in detail. We show why convergence is no longer guaranteed in the general case, identify conditions under which it can still be ensured, and discuss how a dataset can be transformed to recover convergence. We also propose a convergent variant of the process, which preserves the AOC-poset structure: relational attributes, once created, are never removed, which guarantees convergence at the price of attributes that may refer to concepts absent from the final structures.
