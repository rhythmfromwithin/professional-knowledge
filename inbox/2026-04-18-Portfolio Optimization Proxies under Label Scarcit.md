---
interest: medium
link: https://arxiv.org/abs/2604.14206
next_step: skim
priority: high
slack_ts: '1776656357.712149'
source: cs.LG - Machine Learning
status: unread
title: Portfolio Optimization Proxies under Label Scarcity and Regime Shifts via Bayesian
  and Deterministic Students under Semi-Supervised Sandwich Training
---
# Portfolio Optimization Proxies under Label Scarcity and Regime Shifts via Bayesian and Deterministic Students under Semi-Supervised Sandwich Training
> 原文: [https://arxiv.org/abs/2604.14206](https://arxiv.org/abs/2604.14206)

arXiv:2604.14206v1 Announce Type: new
Abstract: This paper proposes a machine learning assisted portfolio optimization framework designed for low data environments and regime uncertainty. We construct a teacher student learning pipeline in which a Conditional Value at Risk (CVaR) optimizer generates supervisory labels, and neural models (Bayesian and deterministic) are trained using both real and synthetically augmented data. The synthetic data is generated using a factor based model with t copula residuals, enabling training beyond the limited real sample of 104 labeled observations. We evaluate four student models under a structured experimental framework comprising (i) controlled synthetic experiments (3 x 5 seed grid), (ii) in-distribution real market evaluation (C2A) and (iii) cross-universe generalization (D2A). In real-market settings, models are deployed using a rolling evaluation protocol where a frozen pretrained model is periodically fine tuned on recent observations and reset to its base state, ensuring stability while allowing limited adaptation. Results show that student models can match or outperform the CVaR teacher in several settings, while achieving improved robustness under regime shifts and reduced turnover. These findings suggest that hybrid optimization learning approaches can enhance portfolio construction in data constrained environments
