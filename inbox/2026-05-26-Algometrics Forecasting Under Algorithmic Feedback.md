---
title: "Algometrics: Forecasting Under Algorithmic Feedback"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.23978
priority: high
status: unread
interest: medium
next_step: skim
---
# Algometrics: Forecasting Under Algorithmic Feedback
> 原文: [https://arxiv.org/abs/2605.23978](https://arxiv.org/abs/2605.23978)

arXiv:2605.23978v1 Announce Type: new
Abstract: In algorithmic markets, predictive models become part of the data-generating process they aim to forecast. Once their outputs are converted into trades, allocations, execution schedules, or risk controls, they change the future data on which they are evaluated. I introduce algometrics, a framework for time series whose evolution depends on the predictive algorithms forecasting them. The framework distinguishes historical risk, measured under passive forecasting, from deployment risk, measured when forecasts drive actions. I prove three results. First, deployment risk is not identifiable from passive historical data alone: even in a one-step linear feedback model, infinitely many algorithm-mediated environments induce the same historical law while implying different deployment risks for the same forecaster. Second, historical model rankings can invert under crowding, so a predictor with lower passive error can have higher deployment error once similar algorithms are adopted. Third, randomized or instrumented actions identify short-horizon linear feedback, and I derive a finite-sample bound for deployment-risk estimation. These results suggest that time-series benchmarks in algorithmic markets should report feedback sensitivity alongside predictive accuracy.
