---
title: "Computer-Orchestrated Design of Algorithms: From Join Specification to Implementation"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.19434
priority: low
status: unread
interest: medium
next_step: skim
---
# Computer-Orchestrated Design of Algorithms: From Join Specification to Implementation
> 原文: [https://arxiv.org/abs/2603.19434](https://arxiv.org/abs/2603.19434)

arXiv:2603.19434v1 Announce Type: new
Abstract: Equipping query processing systems with provable theoretical guarantees has been a central focus at the intersection of database theory and systems in recent years. However, the divergence between theoretical abstractions and system assumptions creates a gap between an algorithm's high-level logical specification and its low-level physical implementation. Ensuring the correctness of this logical-to-physical translation is crucial for realizing theoretical optimality as practical performance gains. Existing database testing frameworks struggle to address this need because necessary algorithm-specific inputs such as join trees are absent from standard test case generation, and integrating complex algorithms into these frameworks imposes prohibitive engineering overhead. Fallback solutions, such as using macro-benchmark queries, are inherently too noisy for isolating intricate defects during this translation.
In this experience paper, we present a retrospective analysis of $\mathsf{CODA}$, a computer-orchestrated testing framework utilized during the physical co-design of TreeTracker Join ($\mathsf{TTJ}$), a theoretically optimal yet practical join algorithm recently published in ACM TODS. By synthesizing minimal reproducible examples, $\mathsf{CODA}$ successfully isolates subtle translation defects, such as state mismanagement and mapping conflicts between join trees and bushy plans. We demonstrate that this logical-to-physical translation process is a bidirectional feedback loop: early structural testing not only hardened $\mathsf{TTJ}$'s physical implementation but also exposed a boundary condition that directly refined the formal precondition of $\mathsf{TTJ}$ itself. Finally, we detail how confronting these translation challenges drove the architectural evolution of $\mathsf{CODA}$ into a robust, structure-aware test generation pipeline for join-tree-dependent algorithms.
