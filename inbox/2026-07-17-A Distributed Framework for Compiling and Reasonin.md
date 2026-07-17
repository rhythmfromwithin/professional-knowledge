---
title: "A Distributed Framework for Compiling and Reasoning with d-DNNF"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.13642
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Distributed Framework for Compiling and Reasoning with d-DNNF
> 原文: [https://arxiv.org/abs/2607.13642](https://arxiv.org/abs/2607.13642)

arXiv:2607.13642v1 Announce Type: new
Abstract: Knowledge Compilation (KC) is a powerful paradigm that enables efficient reasoning by transforming propositional formulas into tractable target languages, such as Deterministic, Decomposable Negation Normal Form (d-DNNF). However, as real-world problem instances grow in complexity, the offline compilation phase becomes a significant computational bottleneck, often exceeding the memory and temporal limits of single-node systems. While distributed computing has been successfully applied to model counting ($\#\mathsf{SAT}$), extending these techniques to knowledge compilation remains a challenge due to the difficulty of sharing partial circuit fragments across distributed nodes.
In this paper, we propose dkc, the first distributed knowledge compiler designed for large-scale Decision-DNNF generation. Leveraging a Cube-and-Conquer strategy, dkc effectively partitions the search space into independent subproblems, mitigating the communication overhead typically associated with work-stealing architectures in circuit-based tasks. Recognizing that the utility of compilation lies in subsequent querying, we further introduce dreasoner, a distributed reasoning engine. dreasoner is capable of performing core inference tasks (including model counting, direct access, and uniform sampling) across a distributed d-DNNF structure, even under variable conditioning. Our experimental evaluation on benchmarks demonstrates that our distributed architecture scales effectively, enabling the compilation and querying of complex formulas that remain beyond the reach of state-of-the-art sequential compilers.
