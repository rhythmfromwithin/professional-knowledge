---
interest: medium
link: https://arxiv.org/abs/2604.22386
next_step: skim
priority: medium
slack_ts: '1777348358.544569'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Pack only the essentials: Adaptive dictionary learning for kernel ridge regression'
---
# Pack only the essentials: Adaptive dictionary learning for kernel ridge regression
> 原文: [https://arxiv.org/abs/2604.22386](https://arxiv.org/abs/2604.22386)

arXiv:2604.22386v1 Announce Type: new
Abstract: One of the major limits of kernel ridge regression (KRR) is that storing and manipulating the kernel matrix K\_n for n samples requires O(n^2) space, which rapidly becomes unfeasible for large n. Nystrom approximations reduce the space complexity to O(nm) by sampling m columns from K\_n. Uniform sampling preserves KRR accuracy (up to epsilon) only when m is proportional to the maximum degree of freedom of K\_n, which may require O(n) columns for datasets with high coherence. Sampling columns according to their ridge leverage scores (RLS) gives accurate Nystrom approximations with m proportional to the effective dimension, but computing exact RLS also requires O(n^2) space.
(Calandriello et al. 2016) propose INK-Estimate, an algorithm that processes the dataset incrementally and updates RLS, effective dimension, and Nystrom approximations on-the-fly. Its space complexity scales with the effective dimension but introduces a dependency on the largest eigenvalue of K\_n, which in the worst case is O(n).
In this paper we introduce SQUEAK, a new algorithm that builds on INK-Estimate but uses unnormalized RLS. As a consequence, the algorithm is simpler, does not need to estimate the effective dimension for normalization, and achieves a space complexity that is only a constant factor worse than exact RLS sampling.
