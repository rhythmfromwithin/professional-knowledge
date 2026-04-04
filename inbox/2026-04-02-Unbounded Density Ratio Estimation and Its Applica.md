---
interest: medium
link: https://arxiv.org/abs/2603.29725
next_step: skim
priority: medium
slack_ts: '1775270896.631689'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Unbounded Density Ratio Estimation and Its Application to Covariate Shift Adaptation
---
# Unbounded Density Ratio Estimation and Its Application to Covariate Shift Adaptation
> 原文: [https://arxiv.org/abs/2603.29725](https://arxiv.org/abs/2603.29725)

arXiv:2603.29725v1 Announce Type: new
Abstract: This paper focuses on the problem of unbounded density ratio estimation -- an understudied yet critical challenge in statistical learning -- and its application to covariate shift adaptation. Much of the existing literature assumes that the density ratio is either uniformly bounded or unbounded but known exactly. These conditions are often violated in practice, creating a gap between theoretical guarantees and real-world applicability. In contrast, this work directly addresses unbounded density ratios and integrates them into importance weighting for effective covariate shift adaptation. We propose a three-step estimation method that leverages unlabeled data from both the source and target distributions: (1) estimating a relative density ratio; (2) applying a truncation operation to control its unboundedness; and (3) transforming the truncated estimate back into the standard density ratio. The estimated density ratio is then employed as importance weights for regression under covariate shift. We establish rigorous, non-asymptotic convergence guarantees for both the proposed density ratio estimator and the resulting regression function estimator, demonstrating optimal or near-optimal convergence rates. Our findings offer new theoretical insights into density ratio estimation and learning under covariate shift, extending classical learning theory to more practical and challenging scenarios.
