---
interest: medium
link: https://arxiv.org/abs/2604.11862
next_step: skim
priority: medium
slack_ts: '1776396650.502189'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Obtaining Partition Crossover masks using Statistical Linkage Learning for
  solving noised optimization problems with hidden variable dependency structure
---
# Obtaining Partition Crossover masks using Statistical Linkage Learning for solving noised optimization problems with hidden variable dependency structure
> 原文: [https://arxiv.org/abs/2604.11862](https://arxiv.org/abs/2604.11862)

arXiv:2604.11862v1 Announce Type: new
Abstract: In optimization problems, some variable subsets may have a joint non-linear or non-monotonical influence on the function value. Therefore, knowledge of variable dependencies may be crucial for effective optimization, and many state-of-the-art optimizers leverage it to improve performance. However, some real-world problem instances may be the subject of noise of various origins. In such a case, variable dependencies relevant to optimization may be hard or impossible to tell using dependency checks sufficient for problems without noise, making highly effective operators, e.g., Partition Crossover (PX), useless. Therefore, we use Statistical Linkage Learning (SLL) to decompose problems with noise and propose a new SLL-dedicated mask construction algorithm. We prove that if the quality of the SLL-based decomposition is sufficiently high, the proposed clustering algorithm yields masks equivalent to PX masks for the noise-free instances. The experiments show that the optimizer using the proposed mechanisms remains equally effective despite the noise level and outperforms state-of-the-art optimizers for the problems with high noise.
