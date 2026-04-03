---
interest: medium
link: https://arxiv.org/abs/2604.00064
next_step: skim
priority: medium
slack_ts: '1775185083.513119'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Forecast collapse of transformer-based models under squared loss in financial
  time series
---
# Forecast collapse of transformer-based models under squared loss in financial time series
> 原文: [https://arxiv.org/abs/2604.00064](https://arxiv.org/abs/2604.00064)

arXiv:2604.00064v1 Announce Type: new
Abstract: We study trajectory forecasting under squared loss for time series with weak conditional structure, using highly expressive prediction models. Building on the classical characterization of squared-loss risk minimization, we emphasize regimes in which the conditional expectation of future trajectories is effectively degenerate, leading to trivial Bayes-optimal predictors (flat for prices and zero for returns in standard financial settings). In this regime, increased model expressivity does not improve predictive accuracy but instead introduces spurious trajectory fluctuations around the optimal predictor. These fluctuations arise from the reuse of noise and result in increased prediction variance without any reduction in bias. This provides a process-level explanation for the degradation of Transformerbased forecasts on financial time series. We complement these theoretical results with numerical experiments on high-frequency EUR/USD exchange rate data, analyzing the distribution of trajectory-level forecasting errors. The results show that Transformer-based models yield larger errors than a simple linear benchmark on a large majority of forecasting windows, consistent with the variance-driven mechanism identified by the theory.
