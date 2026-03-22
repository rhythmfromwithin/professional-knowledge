---
interest: medium
link: https://arxiv.org/abs/2603.16401
next_step: skim
priority: low
slack_ts: '1774148058.723259'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Deep Reinforcement Learning-Assisted Automated Operator Portfolio for Constrained
  Multi-objective Optimization
---
# Deep Reinforcement Learning-Assisted Automated Operator Portfolio for Constrained Multi-objective Optimization
> 原文: [https://arxiv.org/abs/2603.16401](https://arxiv.org/abs/2603.16401)

arXiv:2603.16401v1 Announce Type: new
Abstract: Constrained multi-objective optimization problems (CMOPs) are of great significance in the context of practical applications, ranging from scientific to engineering domains. Most existing constrained multi-objective evolutionary algorithms (CMOEAs) usually employ fixed operators all the time, which exhibit poor versatility in handling various CMOPs. Therefore, some recent studies have focused on adaptively selecting the best operators for the current population states during the search process. The evolutionary algorithms proposed in these studies learn the value of each operator and recommend the operator with the highest value for the current population, resulting in only a single operator being recommended at each generation, which can potentially lead to local optima and inefficient utilization of function evaluations. To address the dilemma in operator adaptation, this paper proposes a reinforcement learning-based automated operator portfolio approach to learn an allocation scheme of operators at each generation. This approach considers the optimization-related and constraint-related features of the current population as states, the overall improvement in population convergence and diversity as rewards, and different operator portfolios as actions. By utilizing deep neural networks to establish a mapping model between the population states and the expected cumulative rewards, the proposed approach determines the optimal operator portfolio during the evolutionary process. By embedding the proposed approach into existing CMOEAs, a deep reinforcement learning-assisted automated operator portfolio based evolutionary algorithm for solving CMOPs, abbreviated as CMOEA-AOP, is developed. Empirical studies on 33 benchmark problems demonstrate that the proposed algorithm significantly enhances the performance of CMOEAs and exhibits more stable performance across different CMOPs.
