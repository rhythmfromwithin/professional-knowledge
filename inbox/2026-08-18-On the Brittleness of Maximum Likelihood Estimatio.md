---
interest: medium
link: https://arxiv.org/abs/2608.13793
next_step: skim
priority: medium
slack_ts: '1787017192.471979'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: On the Brittleness of Maximum Likelihood Estimation for Gaussian Process Hyperparameter
  Optimization
---
# On the Brittleness of Maximum Likelihood Estimation for Gaussian Process Hyperparameter Optimization
> 原文: [https://arxiv.org/abs/2608.13793](https://arxiv.org/abs/2608.13793)

arXiv:2608.13793v1 Announce Type: new
Abstract: Machine learning (ML) has become an indispensable part of modern engineering design workflows. A crucial step in training an ML model is the selection of the loss function which can be systematically formulated via various techniques such as maximum likelihood estimation (MLE) and cross-validation . While MLE is one of the most popular, effective, and intuitive mechanisms for training ML models, it is brittle: if the assumptions underpinning it are not met, the trained ML model may generalize poorly. This brittleness affects even Gaussian processes (GPs) which are widely used in engineering design and are often (incorrectly) presumed to be very robust to overfitting. In this paper, we fundamentally evaluate the brittleness of MLE in the context of training GPs for probabilistic regression or classification tasks. We compare theoretically grounded metrics against MLE and propose practical solutions. Our extensive studies demonstrate the effectiveness of our solutions in downstream design tasks such as Bayesian optimization and provide a blueprint for practitioners to build accurate and robust GPs that can even outperform tabular foundation models in terms of prediction accuracy, uncertainty quantification, and inference cost. Our contributions are publicly available via GitHub at https://github.com/Bostanabad-Research-Group/GP-vs-TabPFN-vs-GPyTorch.
