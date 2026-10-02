---
title: "How Far is Adam from Natural Gradient Descent?"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.00004
priority: high
status: unread
interest: medium
next_step: skim
---
# How Far is Adam from Natural Gradient Descent?
> 原文: [https://arxiv.org/abs/2610.00004](https://arxiv.org/abs/2610.00004)

arXiv:2610.00004v1 Announce Type: new
Abstract: Adam is the standard optimizer in deep learning, yet its geometric relationship to natural gradient descent (NGD) contains unresolved questions. We study Adam's full update rule, including momentum, as a diagonal empirical Fisher approximation subject to diagonal truncation, empirical label substitution, and temporal lag. Using the scale-invariant $\gamma(\Delta\theta)$ metric, we measure Adam's geometric deviation from true NGD across four loss landscapes: well-conditioned linear regression, ill-conditioned linear regression, logistic regression, and a non-convex small neural network. Adam's geometric trajectory is context-dependent. Deviation remains low in well-conditioned settings but rises significantly under ill-conditioning, reaching misalignments of $\approx 10^3$ in the neural network. Higher geometric drift correlates with slower initial optimization but does not degrade final objective minimization; Adam consistently reaches low loss. Furthermore, the improved empirical Fisher (iEF) tracks more stable paths than the standard empirical Fisher (EF), which frequently oscillates or diverges. Our results suggest Adam's practical optimization power may stem from a balance of structural approximation errors and momentum smoothing rather than close tracking of the natural gradient path.
