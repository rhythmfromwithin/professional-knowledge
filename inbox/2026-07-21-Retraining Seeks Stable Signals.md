---
interest: medium
link: https://arxiv.org/abs/2607.15623
next_step: skim
priority: medium
slack_ts: '1784690755.120469'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Retraining Seeks Stable Signals
---
# Retraining Seeks Stable Signals
> 原文: [https://arxiv.org/abs/2607.15623](https://arxiv.org/abs/2607.15623)

arXiv:2607.15623v1 Announce Type: new
Abstract: Predictive models deployed at scale influence future data, a phenomenon called performativity. And there is always one way to cope: Train the model on new data, deploy it again, and repeat. This process, called retraining or repeated risk minimization, creates a feedback loop between model and data that real-world learning systems can't avoid.
Results on performative prediction shed light on this dynamic: If the model's influence on the data is small, retraining reaches a fixed point. What remains open is why fixed points should naturally exist, and what governs retraining when the model's influence is strong. In this work we develop a new perspective on retraining -- the stable signal principle -- that addresses these questions. We start from the assumption that the prediction target has at least some small model-independent component, a stable signal, such as the intrinsic quality of an item.
We prove that when a nonzero stable signal exists, repeated risk minimization, suitably regularized, converges geometrically to the direction of this stable signal. This is true even if the model's influence on the target is arbitrarily large relative to the stable signal. Regularization emerges naturally as a force to control performativity, rather than to promote generalization, revealing a new facet of an old concept. We extend the analysis to a broad family of affine retraining operators under arbitrary model-induced feature changes, heterogeneous time-varying effects, and nonlinear responses. The stable signal perspective also applies to data feedback loops in language modeling, providing new explanations for the stability of language model training from model-generated data.
