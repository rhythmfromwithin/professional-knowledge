---
interest: medium
link: https://arxiv.org/abs/2608.20406
next_step: skim
priority: high
slack_ts: '1787708794.054839'
source: cs.LG - Machine Learning
status: unread
title: 'Machine Learning and ARIMA Model Averaging for Adaptive Public Health Forecasting:
  Comparative Evaluation and an Ontario COVID-19 Case Study'
---
# Machine Learning and ARIMA Model Averaging for Adaptive Public Health Forecasting: Comparative Evaluation and an Ontario COVID-19 Case Study
> 原文: [https://arxiv.org/abs/2608.20406](https://arxiv.org/abs/2608.20406)

arXiv:2608.20406v1 Announce Type: new
Abstract: Public health forecasts must respond to abrupt changes in surveillance data without over-extrapolating noise, reporting artifacts, or temporary trends. We evaluated autoregressive integrated moving average (ARIMA), random forest, and extreme gradient boosting (XGBoost) models using 190 weekly observations of publicly available Ontario COVID-19 case counts from January 2020 to October 2023. Rolling-origin time-series cross-validation preserved temporal order during model tuning and evaluation. Performance was assessed across three operating dimensions: responsiveness following selected turning points, forecast horizons of one to six weeks, and the amount of historical training data. We also developed Machine Learning and ARIMA Model Averaging (MLAMA), a non-negative performance-weighted ensemble with weights that vary by forecast horizon and responsiveness setting. Retrospective comparisons showed that ARIMA adapted rapidly after turning points but its normalized error increased at longer horizons. Random forest and XGBoost were less responsive initially but maintained more stable normalized error over longer horizons. For two-week forecasts at the end of the study period, training on the most recent data outperformed using longer historical periods, particularly for XGBoost. MLAMA achieved the lowest normalized mean absolute percentage error across most forecast horizons and ranked among the best-performing methods across responsiveness settings. These findings support selecting forecasting models according to operating conditions rather than relying on a single universally preferred approach. MLAMA provides a practical framework for combining complementary statistical and machine-learning forecasts. The accompanying Python package is currently maintained in a private repository while software validation and reproducibility testing are completed.
