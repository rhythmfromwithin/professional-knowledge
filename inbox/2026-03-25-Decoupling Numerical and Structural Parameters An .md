---
title: "Decoupling Numerical and Structural Parameters: An Empirical Study on Adaptive Genetic Algorithms via Deep Reinforcement Learning for the Large-Scale TSP"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.20702
priority: low
status: unread
interest: medium
next_step: skim
---
# Decoupling Numerical and Structural Parameters: An Empirical Study on Adaptive Genetic Algorithms via Deep Reinforcement Learning for the Large-Scale TSP
> 原文: [https://arxiv.org/abs/2603.20702](https://arxiv.org/abs/2603.20702)

arXiv:2603.20702v1 Announce Type: new
Abstract: Proper parameter configuration is a prerequisite for the success of Evolutionary Algorithms (EAs). While various adaptive strategies have been proposed, it remains an open question whether all control dimensions contribute equally to algorithmic scalability. To investigate this, we categorize control variables into numerical parameters (e.g., crossover and mutation rates) and structural parameters (e.g., population size and operator switching), hypothesizing that they play distinct roles. This paper presents an empirical study utilizing a dual-level Deep Reinforcement Learning (DRL) framework to decouple and analyze the impact of these two dimensions on the Traveling Salesman Problem (TSP). We employ a Recurrent PPO agent to dynamically regulate these parameters, treating the DRL model as a probe to reveal evolutionary dynamics. Experimental results confirm the effectiveness of this approach: the learned policies outperform static baselines, reducing the optimality gap by approximately 45% on the largest tested instance (rl5915). Building on this validated framework, our ablation analysis reveals a fundamental insight: while numerical tuning offers local refinement, structural plasticity is the decisive factor in preventing stagnation and facilitating escape from local optima. These findings suggest that future automated algorithm design should prioritize dynamic structural reconfiguration over fine-grained probability adjustment. To facilitate reproducibility, the source code is available at https://github.com/StarDream1314/DRLGA-TSP
