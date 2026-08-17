---
interest: medium
link: https://arxiv.org/abs/2608.12403
next_step: skim
priority: medium
slack_ts: '1786931056.502559'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Black-Box Knowledge Transfer across Distinct Feature Sets
---
# Black-Box Knowledge Transfer across Distinct Feature Sets
> 原文: [https://arxiv.org/abs/2608.12403](https://arxiv.org/abs/2608.12403)

arXiv:2608.12403v1 Announce Type: new
Abstract: Pre-trained black-box predictive functions encode knowledge distilled from massive datasets and extensive computation. However, when the available input features differ from those the black box expects, direct use is infeasible. We introduce a method for transferring predictive knowledge from the black box to a new, heterogeneous input space. Our approach decomposes the target regression function into a transferable component, which the black box can inform, and a non-transferable component, which captures information unique to the new space. We propose a two-step neural network procedure, estimating the transferable component from abundant unlabeled feature pairs that bridge the two input spaces and the non-transferable component from limited labels. We derive prediction risk bounds that improve on those of a non-transfer alternative when the non-transferable component is small or smooth, and the procedure adapts to either case. Under additional conditions, the worst-case risk of our estimator is of strictly smaller polynomial order than the minimax risk of estimation from the labeled data alone. We extend the framework to multiple black boxes, each on its own input space, and show that aggregation can reduce prediction error relative to the best single black box. Simulated and real data demonstrate the practical value of the method.
