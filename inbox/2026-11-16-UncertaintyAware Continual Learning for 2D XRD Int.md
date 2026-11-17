---
interest: medium
link: https://arxiv.org/abs/2611.17547
next_step: skim
priority: medium
slack_ts: '1794900949.040129'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Uncertainty-Aware Continual Learning for 2D XRD Interpretation Using Simulated
  and Experimental Data
---
# Uncertainty-Aware Continual Learning for 2D XRD Interpretation Using Simulated and Experimental Data
> 原文: [https://arxiv.org/abs/2611.17547](https://arxiv.org/abs/2611.17547)

arXiv:2611.17547v1 Announce Type: new
Abstract: Autonomous experimentation systems require characterization models that can interpret heterogeneous measurements and maintain predictive performance as data accumulate. Developing such models involves addressing domain mismatch between data sources, overconfident predictions on unfamiliar inputs, and catastrophic forgetting during sequential updates. In this work, we present a proof-of-concept framework for uncertainty-aware continual interpretation of two-dimensional X-ray diffraction (XRD) data. The framework integrates established components: maximum mean discrepancy-based domain adaptation to reduce simulation-to-experiment discrepancies, a convolutional neural network with a spectral-normalized neural Gaussian process (CNN--SNGP) for predictive uncertainty estimation, and replay with knowledge distillation for sequential model updating. We evaluate the framework using simulated and previously-collected experimental data for crystal structure classification of single-phase body-centered cubic, face-centered cubic, and hexagonal close-packed patterns. Data are organized into predefined sequential blocks to assess adaptation and retention of previously learned knowledge. Within this setting, the results show accurate classification across simulated and experimental data, improved alignment between the two domains, and reduced forgetting compared with na\"ive fine-tuning. Predictive uncertainty is also evaluated on unfamiliar and noisy inputs. The contribution is the integration and evaluation of these capabilities for sequential XRD interpretation. The framework provides a basis for future integration into autonomous experimentation systems, with experimental planning, instrument control, and closed-loop deployment remaining areas for future development.
