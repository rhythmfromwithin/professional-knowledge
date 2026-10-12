---
title: "CALQA: Conformal Screening of Forecast-Ensemble Configurations from One Mergeable State"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.13249
priority: low
status: unread
interest: medium
next_step: skim
---
# CALQA: Conformal Screening of Forecast-Ensemble Configurations from One Mergeable State
> 原文: [https://arxiv.org/abs/2610.13249](https://arxiv.org/abs/2610.13249)

arXiv:2610.13249v1 Announce Type: new
Abstract: AutoML systems fit ensemble weights over model libraries; a search can score, per category, market or time pane, thousands of weightings of the quantile-averaged (Vincentized) ensemble for the narrowest conformally calibrated interval; exact calibration scores a group's rows per candidate. We present CALQA, a fixed-size integer aggregate per group and pane that stores histograms of normalised block scores at a net of weight vectors. One GROUP BY builds it; it merges by addition, retracts deletions by subtraction and scores any candidate without reading a row. We prove that its score never falls below the exact split-conformal shift and exceeds it by at most the net distance plus a grid gap; that coverage carries over to each fixed weight vector and, for i.i.d. blocks and up to a union-bound slack, to a searched weight vector deployed with the state's shift; and how small any such state can be. The state is thus a screen: it ranks all candidates, and exact recomputation re-checks the top 100. On five public panels (604 groups, 10,000 candidates each) this two-stage plan matches exact search on held-out blocks (99.95% of its Winkler score), 1.3-59 times faster. On two real panels of about $10^8$ rows (smart meters, retail sales) it is 44-54 times faster at 99.98-100.01% of that score and beats sample screens with the same re-check in regret at less total time. Picks deployed with their exact shift need a held-out coverage check. The state does not pay off for small or greedy searches, off-net weights at ample memory or full twelve-member support.
