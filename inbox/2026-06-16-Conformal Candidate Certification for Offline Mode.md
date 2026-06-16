---
interest: medium
link: https://arxiv.org/abs/2606.15217
next_step: skim
priority: medium
slack_ts: '1781586966.478939'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Conformal Candidate Certification for Offline Model-Based Optimization
---
# Conformal Candidate Certification for Offline Model-Based Optimization
> 原文: [https://arxiv.org/abs/2606.15217](https://arxiv.org/abs/2606.15217)

arXiv:2606.15217v1 Announce Type: new
Abstract: Offline model-based optimization (MBO) proposes candidates by optimizing a surrogate trained on a fixed historical dataset. Because candidates are deliberately out-of-distribution, surrogate rankings are least reliable exactly where the optimizer is most aggressive, yet existing methods provide no per-candidate statistical certificate that a design meets a target threshold. We propose \emph{Conformal Candidate Certification} (CCC), a post-hoc wrapper that attaches a calibrated one-sided lower bound to each candidate and advances only those whose bound exceeds the target. We show that entropy-regularized surrogate maximization induces a Gibbs-tilted proposal, so the same surrogate supplies importance weights for weighted conformal prediction without a separate density-ratio estimation step. In a controlled synthetic study, CCC certifies $16.7\%$ of an aggressive proposal pool with empirical coverage 0.990 at nominal 0.90, while standard conformal prediction ignoring the covariate shift collapses to 0.416 coverage.
