---
interest: medium
link: https://arxiv.org/abs/2609.20883
next_step: skim
priority: high
slack_ts: '1790051346.305109'
source: cs.LG - Machine Learning
status: unread
title: Sparse Priors for Efficient Distribution Learning
---
# Sparse Priors for Efficient Distribution Learning
> 原文: [https://arxiv.org/abs/2609.20883](https://arxiv.org/abs/2609.20883)

arXiv:2609.20883v1 Announce Type: new
Abstract: Despite the widespread use and success of generative AI techniques today, theoretical guarantees on learning a distribution supported in $d$ dimensions from $n$ samples degrade as $O(n^{-1/\Theta(d)})$, though shown to be minimax optimal. We hypothesize that present bounds are too pessimistic because smoothness assumptions are not enough to capture the structure of distributions that often appear in real applications. Consequently, we introduce the class of sparse priors and define the "Sparse Dimension" as a measure of sparsity of a prior over the space of all distributions. We show that distribution learning under a $k$-sparse prior achieves a Bayesian risk lower bound of $\Omega(\sqrt{k/n})$ under common distance metrics, and show a matching (up to logarithmic terms asymptotically in $n,k$) upper bound for the TV distance under mild additional assumptions. We show the statistical equivalence of distribution learning and learning to sample in the Bayesian setting so that our results apply to learning to sample as well. While $k$ can still depend on the dimension $d$, or a notion of intrinsic dimension, our results show that learning under an appropriate prior overcomes the curse of dimensionality with respect to the dependence on $n$.
