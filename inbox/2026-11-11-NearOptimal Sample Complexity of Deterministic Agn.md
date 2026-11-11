---
title: "Near-Optimal Sample Complexity of Deterministic Agnostic PAC Learning"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.13210
priority: medium
status: unread
interest: medium
next_step: skim
---
# Near-Optimal Sample Complexity of Deterministic Agnostic PAC Learning
> 原文: [https://arxiv.org/abs/2611.13210](https://arxiv.org/abs/2611.13210)

arXiv:2611.13210v1 Announce Type: new
Abstract: We study the problem of agnostic PAC learning under deterministic labels, where the examples are labeled by an arbitrary deterministic function, which need not belong to the concept class $C$. This model captures misspecification without stochastic label noise and lies between the realizable and fully agnostic settings. Prior work showed that, when $C$ has finite diameter $K$ and VC dimension $d$, deterministic labels can improve the sample complexity upper bound from the classical agnostic guarantee $O(d/\varepsilon^2)$ to $\widetilde{O}(K/\varepsilon)$, but left a large gap between upper and lower bounds. Our main result sharpens this picture. We prove that every class of VC dimension $d$ and finite diameter $K$ is learnable with sample complexity $\widetilde{O}\left( \frac{K^{1/3} \, d^{2/3}}{\varepsilon} \right)$, and we construct classes for which this bound is tight up to logarithmic factors. We also study the online analogue of this problem and show that the minimax regret is again partly controlled by the diameter of the class. Technically, our upper bounds are obtained via memorization-based learning algorithms that exploit the deterministic label structure.
