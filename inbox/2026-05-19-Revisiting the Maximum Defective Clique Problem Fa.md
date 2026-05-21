---
interest: medium
link: https://arxiv.org/abs/2605.16948
next_step: skim
priority: low
slack_ts: '1779337378.011999'
source: cs.DB - Databases
status: unread
title: 'Revisiting the Maximum Defective Clique Problem: Faster Branching and a Tighter
  Upper Bound'
---
# Revisiting the Maximum Defective Clique Problem: Faster Branching and a Tighter Upper Bound
> 原文: [https://arxiv.org/abs/2605.16948](https://arxiv.org/abs/2605.16948)

arXiv:2605.16948v1 Announce Type: new
Abstract: The $k$-defective clique model relaxes the strict completeness constraint of the traditional clique by allowing up to $k$ missing edges, providing a robust formulation for detecting cohesive structures in noisy graphs. Consequently, the maximum $k$-defective clique problem has attracted significant attention. State-of-the-art exact algorithms predominantly adopt the branch-and-bound framework, which recursively partitions the current problem instance (or branch) into two sub-problems via a branching procedure, until each sub-problem becomes trivially solvable. However, this strategy often leads to excessive branching by overlooking intermediate sub-problems that are non-trivial yet efficiently solvable. While recent studies have attempted to refine branching procedures, they fail to address this structural redundancy. To address this, we propose BBRes, a framework that incorporates a novel early termination strategy into the recursive branching process. By employing a specialized polynomial-time solver to identify and resolve tractable sub-instances, BBRes effectively avoids redundant branching steps. Additionally, we design a tailored branching strategy that synergizes with this termination mechanism. As a result, BBRes achieves an improved theoretical worst-case time complexity. To enhance practical performance, we propose a tighter upper bound based on a novel double graph coloring method integrated with max-flow techniques, which is orthogonal to the branching framework. Extensive experiments show that BBRes achieves at least 2X speedup over state-of-the-art methods on a substantial fraction of the datasets.
