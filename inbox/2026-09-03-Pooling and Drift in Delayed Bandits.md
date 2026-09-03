---
title: "Pooling and Drift in Delayed Bandits"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.01761
priority: medium
status: unread
interest: medium
next_step: skim
---
# Pooling and Drift in Delayed Bandits
> 原文: [https://arxiv.org/abs/2609.01761](https://arxiv.org/abs/2609.01761)

arXiv:2609.01761v1 Announce Type: new
Abstract: A system often has to act long before it learns whether the act worked: a recommender sees a click in seconds and a purchase in days. With $K$ actions and a delay of $d$ rounds, the best rate known for this setting is $\widetilde{O}(\sqrt{(K+d)T})$ over $T$ rounds, so a longer menu is always more expensive to learn from. It need not be: if the outcome depends on the action only through the state it produced, then one late outcome informs every action that could have produced the observed state, and the price is set by how many genuinely different states the actions produce rather than by how many actions there are. We measure this using an effective dimension $v\_t$ between $1$ and the number of states, and prove $\widetilde{O}(\sqrt{(d+1)V\log K})$ for a rotating algorithm and $\widetilde{O}(\sqrt{V^{-}}+\sqrt{dT})$ for the single-copy algorithm used in practice, for any budget fixed in advance; merging similar states lowers the price further, at an explicit bias. Even when given the exact losses from $d$ rounds ago, no algorithm escapes $\Omega(\sqrt{dE\min\{1+\log J,T/d\}})$, where $J$ counts the drifting directions and $E$ bounds how far losses move while the learner waits. On generated data, the state channel cuts regret by up to 79 percent against action-level weighting and, on the funnel family, by 32 to 68 percent against a tuned minimax-optimal method.
