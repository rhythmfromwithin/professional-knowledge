---
interest: medium
link: https://arxiv.org/abs/2603.26232
next_step: skim
priority: medium
slack_ts: '1775014237.937539'
source: cs.DC - Distributed Computing
status: unread
title: 'ParaQAOA: Efficient Parallel Divide-and-Conquer QAOA for Large-Scale Max-Cut
  Problems Beyond 10,000 Vertices'
---
# ParaQAOA: Efficient Parallel Divide-and-Conquer QAOA for Large-Scale Max-Cut Problems Beyond 10,000 Vertices
> 原文: [https://arxiv.org/abs/2603.26232](https://arxiv.org/abs/2603.26232)

arXiv:2603.26232v1 Announce Type: new
Abstract: Quantum Approximate Optimization Algorithm (QAOA) has emerged as a promising solution for combinatorial optimization problems using a hybrid quantum-classical framework. Among combinatorial optimization problems, the Maximum Cut (Max-Cut) problem is particularly important due to its broad applicability in various domains. While QAOA-based Max-Cut solvers have been developed, they primarily favor solution accuracy over execution efficiency, which significantly limits their practicality for large-scale problems. To address the limitation, we propose ParaQAOA, a parallel divide-and-conquer QAOA framework that leverages parallel computing hardware to efficiently solve large Max-Cut problems. ParaQAOA significantly reduces runtime by partitioning large problems into subproblems and solving them in parallel while preserving solution quality. This design not only scales to graphs with tens of thousands of vertices but also provides tunable control over accuracy-efficiency trade-offs, making ParaQAOA adaptable to diverse performance requirements. Experimental results demonstrate that ParaQAOA achieves up to 1,600x speedup over state-of-the-art methods on Max-Cut problems with 400 vertices while maintaining solution accuracy within 2% of the best-known solutions. Furthermore, ParaQAOA solves a 16,000-vertex instance in 19 minutes, compared to over 13.6 days required by the best-known approach. These findings establish ParaQAOA as a practical and scalable framework for large-scale Max-Cut problems under stringent time constraints.
