---
interest: medium
link: https://arxiv.org/abs/2603.26923
next_step: skim
priority: medium
slack_ts: '1775185054.582129'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Koopman Operator Identification of Model Parameter Trajectories for Temporal
  Domain Generalization (KOMET)
---
# Koopman Operator Identification of Model Parameter Trajectories for Temporal Domain Generalization (KOMET)
> 原文: [https://arxiv.org/abs/2603.26923](https://arxiv.org/abs/2603.26923)

arXiv:2603.26923v1 Announce Type: new
Abstract: Parametric models deployed in non-stationary environments degrade as the underlying data distribution evolves over time (a phenomenon known as temporal domain drift). In the current work, we present KOMET (Koopman Operator identification of Model parameter Evolution under Temporal drift), a model-agnostic, data-driven framework that treats the sequence of trained parameter vectors as the trajectory of a nonlinear dynamical system and identifies its governing linear operator via Extended Dynamic Mode Decomposition (EDMD). A warm-start sequential training protocol enforces parameter-trajectory smoothness, and a Fourier-augmented observable dictionary exploits the periodic structure inherent in many real-world distribution drifts. Once identified, KOMET's Koopman operator predicts future parameter trajectories autonomously, without access to future labeled data, enabling zero-retraining adaptation at deployment. Evaluated on six datasets spanning rotating, oscillating, and expanding distribution geometries, KOMET achieves mean autonomous-rollout accuracies between 0.981 and 1.000 over 100 held-out time steps. Spectral and coupling analyses further reveal interpretable dynamical structure consistent with the geometry of the drifting decision boundary.
