---
title: "Harnessing Unimodality in Semiparametric Contextual Pricing via Oracle Price Map Learning"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.15411
priority: medium
status: unread
interest: medium
next_step: skim
---
# Harnessing Unimodality in Semiparametric Contextual Pricing via Oracle Price Map Learning
> 原文: [https://arxiv.org/abs/2605.15411](https://arxiv.org/abs/2605.15411)

arXiv:2605.15411v1 Announce Type: new
Abstract: We study contextual dynamic pricing in a semiparametric scalar-index valuation model where the latent value is $v\_t=\mu\_\ast(\mathsf c\_t)+\xi\_t$, with an unknown utility map $\mu\_\ast$ and an unknown additive noise distribution. The key decision object is the one-dimensional oracle price map $u\mapsto p^\ast(u)$ induced by the scalar index $u=\mu\_\ast(\mathsf c)$ and the noise tail. Under the $\beta$-H\"older smoothness of the tail function for $\beta\geq 2$ and a revenue-geometry condition that gives a unique, stable, interior maximizer, this oracle map is itself $(\beta-1)$-smooth. We exploit such structure through $\mathsf{ORBIT}$, a modular coarse-to-fine policy that takes a scalar pilot index as input, localizes a benchmark price in each active bin, and learns a local polynomial approximation of the oracle map inside a trust region via bandit convex optimization. For the baseline linear utility model $\mu\_\ast(\mathsf c)=\mathsf c^\top\theta\_\ast$, an adaptive elliptical exploration scheme constructs the required scalar pilot online without distributional assumptions on the contexts. The resulting policy achieves regret $\widetilde{O}\big(T^{\frac{2\beta-1}{4\beta-3}}+\sqrt{dT}\big)$. For fixed $d$, we establish a matching lower bound in the horizon dependence, unveiling that the nonparametric oracle-map learning term is minimax sharp. The same scalar-pilot interface also yields extensions to sparse high-dimensional linear utility and nonparametric H\"older utility.
