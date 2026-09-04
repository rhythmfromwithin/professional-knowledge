---
title: "Practical Threshold-based Tree Edit Distance Lower-Bounds"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.03078
priority: low
status: unread
interest: medium
next_step: skim
---
# Practical Threshold-based Tree Edit Distance Lower-Bounds
> 原文: [https://arxiv.org/abs/2609.03078](https://arxiv.org/abs/2609.03078)

arXiv:2609.03078v1 Announce Type: new
Abstract: Threshold-based similarity search over tree-structured data using tree edit distance (TED) is computationally intensive. Given a query tree and a database of trees, the goal is to retrieve all trees within a predefined TED threshold $\tau$. Because exact TED computation is expensive, practical methods employ lower-bounds to prune dissimilar candidates before verification. Existing lower-bounds exhibit a fundamental trade-off: inexpensive statistical and structural bounds provide limited pruning power, whereas the more precise traversal-based string edit distance (SED) bound is expensive to compute using standard quadratic dynamic programming. Moreover, previous comparative studies do not cover recent structural filters or threshold-aware SED implementations, leaving their practical trade-offs unclear. In this article, we first provide a comprehensive experimental comparison of state-of-the-art TED lower-bounds in terms of pruning precision and computational cost. We then accelerate the SED lower-bound using Ukkonen's bounded string edit distance algorithm, substantially reducing its runtime without affecting its pruning power. Finally, we introduce the SED-struct threshold filter, which strengthens SED with axes-aware constraints capturing structural relationships among tree nodes. Experiments on synthetic and real-world datasets show that SED-struct consistently achieves the highest filtering precision while retaining practical filtering costs. The results suggest that SED-struct is particularly beneficial for heterogeneous tree collections in which the standard SED lower-bound achieves relatively low precision.
