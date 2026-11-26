---
interest: medium
link: https://arxiv.org/abs/2611.28169
next_step: skim
priority: medium
slack_ts: '1795679635.812139'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: The Value of Labels in Data Selection for Least Squares
---
# The Value of Labels in Data Selection for Least Squares
> 原文: [https://arxiv.org/abs/2611.28169](https://arxiv.org/abs/2611.28169)

arXiv:2611.28169v1 Announce Type: new
Abstract: Suppose a selector sees a finite labelled dataset and chooses $n$ of its rows, with repetition. Ordinary least squares is then fitted to the rows that were chosen, without weights, and the excess loss of the fit on the full dataset is measured in units of the optimal loss. Without further assumptions this ratio does not decay with $n$. We examine the problem for $d$ features and rows of normalized leverage at most $\kappa$, and determine or bound the leading constants. A selector that must establish its rule before seeing the labels has an optimal worst-case ratio of $d\kappa/n$ to leading order, whatever use it makes of the features. With scalar labels, a selector that sees the labels achieves a value between $d\kappa/(2n)$ and $d\kappa\Lambda\_d/n$, where $\Lambda\_d<1$ is the rounding constant of mean selection. For $d\le4$, the constant is then $d\kappa/2$, so that labels are worth exactly a factor of two there, and for one feature and $m$ outputs it is $\kappa\Lambda\_m$. With two or more features the selector can change the proportions of the frequent rows and therefore reshape its own design matrix. We design a simplified optimization problem, which we call a game, that bounds the constant for datasets with exactly fitted frequent rows, then show that its value is at most one half of the gradient energy in several regimes, and that one half is exact along directions in which the frequent rows are rigid, such as an intercept. For grouped designs, in which reshaping amounts to the allocation of a common budget, the constant is $27d/128$ up to an additive constant, compared with $d$ without labels. Nevertheless, one half is not the constant in every dimension: we construct datasets of extremely high dimension and large leverage on which every selection has an excess ratio of at least $(e^{-1/2}-o(1))\,d\kappa/n$, so that labels are worth at most a factor close to $\sqrt e$ there.
