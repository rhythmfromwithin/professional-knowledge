---
title: "Minimax Alternating Regret for the Experts Problem and Online Convex Optimization"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.25182
priority: medium
status: unread
interest: medium
next_step: skim
---
# Minimax Alternating Regret for the Experts Problem and Online Convex Optimization
> 原文: [https://arxiv.org/abs/2608.25182](https://arxiv.org/abs/2608.25182)

arXiv:2608.25182v1 Announce Type: new
Abstract: In this paper, we study alternating regret in online convex optimization (OCO), motivated by the success of alternating learning dynamics in two-player games. Although previous works have shown that $o(\sqrt{T})$ alternating regret is achievable under various assumptions on the loss functions and feasible domains, the minimax regret rate has remained open even for the expert problem. In this paper, we resolve this question by showing matching lower and upper bounds for both the expert problem and general OCO. Somewhat surprisingly, for the $d$-expert problem, we show that the minimax alternating regret is $\Theta(\log d)$, independent of the horizon $T$. This significantly improves upon the best-known $\mathcal{O}(T^{1/3}\log^{2/3} d)$ established by Hait et al. [2025]. We further extend our results to general OCO over a $d$-dimensional compact convex set and prove that the worst-case minimax alternating regret is $\Theta\left(d\log \left(1+\frac{T}{d}\right)\right)$, also significantly improving upon the best-known $\mathcal{O}((d\log T)^{2/3}T^{1/3})$ upper bound and resolving the open problem posed by Cevher et al. [2023], Hait et al. [2025]. Technically, our upper bound for the expert problem is achieved by a corrected variant of Hedge, in which carefully designed correction terms cancel the unfavorable curvature arising in the alternating-regret analysis. We extend the same corrected-potential argument to continuous action sets to obtain the optimal alternating-regret rate for OCO. For the lower bounds, the expert construction repeatedly eliminates half of the candidate experts, while the OCO lower bound instance construction replaces this discrete elimination by a more involved multiscale construction on the unit disk.
