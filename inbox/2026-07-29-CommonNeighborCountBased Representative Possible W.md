---
interest: medium
link: https://arxiv.org/abs/2607.23085
next_step: skim
priority: low
slack_ts: '1785295226.580069'
source: cs.DB - Databases
status: unread
title: Common-Neighbor-Count-Based Representative Possible World Finding on Uncertain
  Graphs
---
# Common-Neighbor-Count-Based Representative Possible World Finding on Uncertain Graphs
> 原文: [https://arxiv.org/abs/2607.23085](https://arxiv.org/abs/2607.23085)

arXiv:2607.23085v1 Announce Type: new
Abstract: A representative possible world (RPW) is a deterministic graph derived from an uncertain graph $\mathcal{G}$ where a designated structural feature closely approximates its expected value in $\mathcal{G}$. Serving as a proxy for $\mathcal{G}$, the RPW allows conventional deterministic algorithms to be directly executed on it for mining tasks targeting this feature, thereby avoiding computationally expensive enumeration or sampling on $\mathcal{G}$. Existing studies on RPWs primarily focus on individual node features, e.g., degree or triangle degree. However, many mining tasks, such as link prediction, critically rely on the number of common neighbors between two nodes, which is a pairwise feature. To bridge this gap, we study the \underline{C}ommon-neighbor-count-based \underline{R}epresentative \underline{P}ossible \underline{W}orld (CRPW) problem, extending RPWs from preserving node-level statistics to preserving pairwise structural relationships. The problem seeks the possible world that best preserves the expected numbers of common neighbors between node pair, and we prove that is NP-hard. To address it, we develop a two-stage basic algorithm that quickly initializes a possible world and then refines it iteratively. We next accelerate the refinement by replacing its costly floating-point evaluation with an efficient integer counting strategy, as the refinement only requires determining whether a change is beneficial, rather than computing its exact magnitude. Moreover, we design a Beta-based adaptive termination method to automatically stop the refinement once the desired quality of the possible world is reached, preventing over- or under-execution. Extensive experiments on real-world uncertain graphs demonstrate the effectiveness of our algorithms on diverse mining tasks. Especially on common-neighbor-related tasks, we achieve the best performance among all compared methods.
