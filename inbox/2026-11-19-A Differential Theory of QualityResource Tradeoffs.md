---
interest: medium
link: https://arxiv.org/abs/2611.23324
next_step: skim
priority: medium
slack_ts: '1795157491.420979'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'A Differential Theory of Quality-Resource Trade-offs for AI Model Selection:
  The Multiresource Frontier and Its Minimax Price'
---
# A Differential Theory of Quality-Resource Trade-offs for AI Model Selection: The Multiresource Frontier and Its Minimax Price
> 原文: [https://arxiv.org/abs/2611.23324](https://arxiv.org/abs/2611.23324)

arXiv:2611.23324v1 Announce Type: new
Abstract: Comparing AI models across resource budgets yields quality-resource frontiers relating error to latency, parameter count, training compute, and energy. Offset power laws summarize such frontiers, but their fitted parameters reveal neither the price-independent geometry nor the manner in which trade-offs extend across several resource channels. This paper addresses both gaps by developing a differential theory in which this structure is made explicit. Each frontier admits a price-independent plane-curve representation relating the effective number of active resource channels, $N\_{\mathrm{eff}} = s^2/\kappa$ (squared slope over curvature), to the remaining log-error depth, $\Delta S = \ln(\varepsilon/\varepsilon\_{\infty})$. This representation separates intrinsic shape from the scale and origin of the resource axis. Complete monotonicity and divisibility yield differential inequalities and frontier bounds. When each of $N$ resources contributes one active channel, the theory gives the parameter-free operating rule $N\_{\mathrm{eff}} = 1$ in delivered units and derives minimax resource prices $\lambda^{\star}\_i = \alpha\_i/(N+1)$ with an exact worst-case regret of $\ln(N+1)$ nats. The results make it possible to interpret measured frontiers and compare resource costs without hand-chosen exchange rates. The theory is evaluated on 117 published frontiers and implemented in the open-source package nn-rank, which derives prices from measured quality and cost, ranks candidates, and reports supported choices and minimax regret: https://github.com/ABrain-One/nn-rank
