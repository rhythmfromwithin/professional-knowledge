---
interest: medium
link: https://arxiv.org/abs/2607.28864
next_step: skim
priority: medium
slack_ts: '1785986397.282459'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Conditioning Tree-Based Diffusions and Flows for Probabilistic Tabular Regression
---
# Conditioning Tree-Based Diffusions and Flows for Probabilistic Tabular Regression
> 原文: [https://arxiv.org/abs/2607.28864](https://arxiv.org/abs/2607.28864)

arXiv:2607.28864v1 Announce Type: new
Abstract: Tree-based diffusion models fit flexible conditional predictive distributions for tabular regression without a neural density estimator, but they inherit their design defaults---noising path, parameterization, training distribution, features, sampler---from the neural setting. We show these defaults are the binding constraint: what a gradient-boosted ensemble actually solves is a supervised regression problem whose conditioning they determine. We present DiffGBM, which makes them explicit along two axes. First, a Gaussian-path flow-matching trainer for $p(y \mid x)$ that learns a velocity field directly and recovers the score algebraically, admitting few-step deterministic ODE sampling. Second, we expose the score-side recipe---residualization, EDM-style preconditioning, log-sigma time sampling, noise-level features, loss weighting, and histogram resolution---as jointly tunable axes over a shared LightGBM surface rather than one frozen bundle. This \emph{score-flex} space represents the published recipe as a special case; across eleven tabular benchmarks under fold-0 tuning, folds-1--5 evaluation, and a matched 40-trial budget and sampler, the selected configurations beat that baseline on \emph{every} dataset (paired Wilcoxon $11/0$, $p<10^{-3}$), with the best aggregate CRPS skill (0.725 vs.\ 0.699) of any row. The two rows are complementary: score-flex buys accuracy with a stochastic sampler and is the slowest row, while flow matching is the cheapest sampler ($5.2\times$ faster than the published baseline) and the best-calibrated DiffGBM row. Tuned non-diffusion baselines still win individual datasets, and stochastic ($\varepsilon>0$) flow samplers do not Pareto-dominate the deterministic corner.
