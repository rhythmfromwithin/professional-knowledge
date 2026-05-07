---
interest: medium
link: https://arxiv.org/abs/2605.01628
next_step: skim
priority: medium
slack_ts: '1778125806.365139'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Self-Normalized Martingales and Uniform Regret Bounds for Linear Regression
---
# Self-Normalized Martingales and Uniform Regret Bounds for Linear Regression
> 原文: [https://arxiv.org/abs/2605.01628](https://arxiv.org/abs/2605.01628)

arXiv:2605.01628v1 Announce Type: new
Abstract: Self-normalized martingale inequalities lie at the heart of confidence ellipsoids for online least squares and, more broadly, many bandit and reinforcement-learning results. Yet existing vector and scalar results typically rely on bounded covariates and an explicit regularization matrix, producing bounds that are \emph{not scale-invariant}: although the self-normalized quantity is scale-invariant by definition, its standard upper bounds are not.
We characterize when scale-invariant upper bounds on self-normalized martingales are possible. Without further assumptions, we prove that nontrivial scale-invariant bounds exist only in dimension $d=1$; moreover, in $d=1$ we obtain $O(\log T)$ scale-invariant self-normalized bounds without any assumptions on the covariates. In contrast, for $d>1$ we show that no nontrivial scale-invariant bound can hold in full generality. We then connect this dichotomy to \emph{doubly-uniform} regret in online linear regression (i.e., regret bounds that are simultaneously independent of the covariate scale and the comparator norm) and use it to resolve the open question of Gaillard, Gerchinovitz, Huard, and Stoltz, \emph{``Uniform regret bounds over $\mathbb{R}^d$ for the sequential linear regression problem with the square loss''} (ALT 2019): in $d=1$ we give an explicit algorithm with $O(\log T)$ doubly-uniform regret, whereas for $d>1$ sublinear doubly-uniform regret is impossible.
Finally, under a natural \emph{smoothness} condition (bounded Radon--Nikodym derivatives of the conditional covariate laws with respect to a fixed base measure), we recover sublinear regret for $d>1$ without bounded covariates and derive a self-normalized concentration inequality free of the usual regularization penalties, yielding arguably a first natural scale-invariant bound for adaptive, non-i.i.d. vector martingales.
