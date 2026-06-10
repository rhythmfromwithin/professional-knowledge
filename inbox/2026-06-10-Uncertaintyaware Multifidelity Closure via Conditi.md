---
interest: medium
link: https://arxiv.org/abs/2606.09857
next_step: skim
priority: high
slack_ts: '1781065416.072599'
source: cs.LG - Machine Learning
status: unread
title: Uncertainty-aware Multi-fidelity Closure via Conditional Normalizing Flows
---
# Uncertainty-aware Multi-fidelity Closure via Conditional Normalizing Flows
> 原文: [https://arxiv.org/abs/2606.09857](https://arxiv.org/abs/2606.09857)

arXiv:2606.09857v1 Announce Type: new
Abstract: Reduced-order models (ROMs) provide an efficient surrogate for complex multiscale systems, but their predictive accuracy is often compromised by truncation errors and the inadequate representation of interactions between resolved and unresolved scales. The missing effect of truncated (unresolved) scales on ROM (resolved) scales is often denoted as the closure problem. In this work, we formulate ROM closure modeling as a multi-fidelity (MF) learning problem and propose an uncertainty-aware MF framework based on conditional normalizing flow to enhance ROM predictive accuracy. The proposed approach learns a probabilistic mapping from low-fidelity (LF) ROM coefficients to high-fidelity (HF) coefficients, thereby improving predictive fidelity while quantifying the uncertainty associated with the learned closure. Two correction strategies are investigated: direct learning, in which HF coefficients are predicted directly from LF inputs, and residual learning, which learns the discrepancy between LF and HF coefficients and uses it to recover the corrected HF solution. The framework is demonstrated on a vortex merging problem governed by the two-dimensional Navier Stokes equations. Results show that both correction strategies improve ROM accuracy over uncorrected ROM, with residual learning achieving consistently better performance than direct learning. Moreover, the two proposed deep generative model-based strategies provide uncertainty quantification for the corrected ROM coefficients, which is critical for assessing prediction confidence and supporting the reliable use of ROMs in practical applications.
