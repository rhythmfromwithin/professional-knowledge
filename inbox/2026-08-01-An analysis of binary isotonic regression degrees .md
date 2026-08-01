---
title: "An analysis of binary isotonic regression: degrees of freedom and implications for calibration"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.27301
priority: medium
status: unread
interest: medium
next_step: skim
---
# An analysis of binary isotonic regression: degrees of freedom and implications for calibration
> 原文: [https://arxiv.org/abs/2607.27301](https://arxiv.org/abs/2607.27301)

arXiv:2607.27301v1 Announce Type: new
Abstract: Isotonic regression is a canonical tool for estimating monotone functions and calibrating probabilistic predictors. We provide a fully sharp finite-sample characterization of its worst-case degrees of freedom on binary samples. Specifically, we identify the binary sequences that maximize the number of distinct fitted values produced by isotonic regression. We develop a sharp bound on the degrees of freedom with a leading term of $\frac{3}{(4\pi^2)^{1/3}} n^{2/3}$ using analytic number theory, improving on previous bounds.
We then apply this result to calibration. Calibration is a central requirement for probabilistic prediction, and isotonic regression is a widely used post-processing method for improving calibration. Building on deterministic degrees-of-freedom bounds, we derive, to our knowledge, the first nontrivial distribution-free guarantee on the Expected Calibration Error (ECE) of isotonic regression. This ECE bound is fully model-free and distribution-free, only assuming $Y \in \{0,1\}$.
