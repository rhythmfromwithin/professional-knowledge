---
interest: medium
link: https://arxiv.org/abs/2607.02632
next_step: skim
priority: high
slack_ts: '1783569517.364969'
source: cs.LG - Machine Learning
status: unread
title: 'QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series
  Forecasting'
---
# QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series Forecasting
> 原文: [https://arxiv.org/abs/2607.02632](https://arxiv.org/abs/2607.02632)

arXiv:2607.02632v1 Announce Type: new
Abstract: Time-series forecasting supports decisions in finance, en-ergy, transportation, public health, and industrial monitoring. Recent foundation models improve transfer across forecast-ing tasks, but many depend on centralized data and Trans-former attention, which restricts their use for long, high-di-mensional, and privacy-sensitive signals. This paper presents QuantFlow, a probabilistic forecasting framework that com-bines inverted sequence embedding, bidirectional Mamba state-space decoders, quantile regression, and federated learning. Each variable is embedded over the complete ob-servation window, processed in forward and reverse direc-tions, and projected to five conditional quantiles. TSMixup expands temporal diversity through Dirichlet-weighted inter-polation while preserving sequence structure. Experiments cover cryptocurrency, traffic, electricity, Electricity Trans-former Temperature, influenza, and weather data. QuantFlow obtains mean squared errors of 0.2834 on ETTm1 and 0.2218 on Weather, and a 20-client non-IID deployment retains use-ful accuracy after three communication rounds without cen-tralizing raw records. The results indicate that selective state-space modelling is a promising basis for scalable, uncer-tainty-aware, and privacy-conscious time-series prediction, while also revealing limitations on irregular epidemiological signals and long-horizon generalization.
