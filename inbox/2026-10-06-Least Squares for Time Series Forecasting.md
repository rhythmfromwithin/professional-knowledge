---
interest: medium
link: https://arxiv.org/abs/2610.03812
next_step: skim
priority: high
slack_ts: '1791266364.925029'
source: cs.LG - Machine Learning
status: unread
title: Least Squares for Time Series Forecasting
---
# Least Squares for Time Series Forecasting
> 原文: [https://arxiv.org/abs/2610.03812](https://arxiv.org/abs/2610.03812)

arXiv:2610.03812v1 Announce Type: new
Abstract: A time-series forecast is scored on a future value of the series. A representation loss that regresses the next latent, as in LeNEPA, is a different least-squares problem on the same bottleneck. We write both programs down. The forecast program minimizes the error of a decoded latent on the coordinate that will be reported. For a scalar target and a linear decoder, every latent rank of at least one matches ordinary least squares, and an isotropy constraint is only a rescaling: after the decoder is refit, the forecast does not move. The other program fits the whole next vector at a fixed rank, then freezes the encoder and attaches a head. On a four-dimensional series whose last three coordinates are the same autoregression, that rank-1 fit puts mass $0.9998$ on the repeated coordinate and forecasts the remaining signal at the marginal variance $2.794$. The forecast program puts mass $1$ on the signal and matches the innovation variance $0.992$. Rank $2$ gives the vector fit a second direction, and the two programs agree. Iterating the fitted one-step coefficient $0.803$ raises the open-loop error from $0.992$ at one step to $2.700$ at eight steps.
