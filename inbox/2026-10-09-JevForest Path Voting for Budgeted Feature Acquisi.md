---
interest: medium
link: https://arxiv.org/abs/2610.10615
next_step: skim
priority: medium
slack_ts: '1791610143.643849'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'JevForest: Path Voting for Budgeted Feature Acquisition'
---
# JevForest: Path Voting for Budgeted Feature Acquisition
> 原文: [https://arxiv.org/abs/2610.10615](https://arxiv.org/abs/2610.10615)

arXiv:2610.10615v1 Announce Type: new
Abstract: Choosing which information to observe is central to prediction under limited observation budgets. We study JevForest, a feature acquisition policy that aggregates path-dependent proposals from bootstrapped trees, weights them by global training information gain, and predicts from the acquired values with a shared masked classifier. An online implementation queries Jev for semantic answers selected by this policy. On small balanced held-out samples, four-question forest acquisition achieves accuracy $0.729$ on AG News ($n=48$), compared with $0.667$ for a static gain ranking and $0.583$ for random ordering. On TREC ($n=24$), the ordering reverses: forest accuracy is $0.667$, compared with $0.750$ and $0.833$. Asking all eight questions in one batch yields higher accuracy at lower measured cost and latency than four sequential forest queries; direct Jev classification matches the batch accuracy while costing less. Offline MiniBooNE experiments yield accuracy $0.845\pm0.010$ at ten features and $0.885\pm0.008$ at forty features over three jointly varying data and forest seeds (mean $\pm$ sample standard deviation). A companion Newton boosting implementation provides preliminary full-feature synthetic results. These exploratory findings establish a working Jev acquisition workflow but do not support a general advantage for path voting: its value depends on the task, predictor, and the distinction between question budgets and actual query costs.
