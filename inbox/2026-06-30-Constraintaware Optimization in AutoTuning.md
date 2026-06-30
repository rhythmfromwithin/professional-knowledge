---
interest: medium
link: https://arxiv.org/abs/2606.28372
next_step: skim
priority: low
slack_ts: '1782792821.369059'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Constraint-aware Optimization in Auto-Tuning
---
# Constraint-aware Optimization in Auto-Tuning
> 原文: [https://arxiv.org/abs/2606.28372](https://arxiv.org/abs/2606.28372)

arXiv:2606.28372v1 Announce Type: new
Abstract: Automatic performance tuning, or auto-tuning, is a key technique in high-performance computing, enabling applications to adapt to complex and evolving hardware architectures. A central challenge is the need to optimize over large discrete, constrained parameter spaces, where many candidate configurations are invalid due to hardware or software correctness constraints. Traditional evolutionary algorithms, such as Differential Evolution, Particle Swarm Optimization, and Genetic Algorithms, are not inherently constraint-aware and thus often waste computational resources evaluating invalid solutions.
In this work, we present and evaluate constraint-aware variants of four evolutionary algorithms for auto-tuning. Through extensive experiments on a representative benchmark suite, we show that constraint-aware optimization leads to faster convergence and improved performance over unconstrained methods. Furthermore, we demonstrate that our methods outperform the pyATF methods, a state-of-the-art framework for constraint-based auto-tuning. Our results demonstrate that incorporating constraint-awareness into the optimization process significantly enhances their applicability and effectiveness in real-world auto-tuning problems. Constraint-awareness improved algorithm efficiency by ~39 on average, correlated with search space sparsity. The algorithms developed in this study are publicly available as open-source contributions to the Kernel Tuner framework, facilitating future research and benefitting users.
