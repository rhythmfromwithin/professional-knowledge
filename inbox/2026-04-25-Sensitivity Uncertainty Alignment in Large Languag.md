---
title: "Sensitivity Uncertainty Alignment in Large Language Models"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.20903
priority: low
status: unread
interest: medium
next_step: skim
---
# Sensitivity Uncertainty Alignment in Large Language Models
> 原文: [https://arxiv.org/abs/2604.20903](https://arxiv.org/abs/2604.20903)

arXiv:2604.20903v1 Announce Type: new
Abstract: We propose Sensitivity-Uncertainty Alignment (SUA), a framework for analyzing failures of large language models under adversarial and ambiguous inputs. We argue that adversarial sensitivity and ambiguity reflect a common issue: misalignment between prediction instability and model uncertainty. A reliable model should express higher uncertainty when its predictions are unstable; failure to do so leads to miscalibration.
We define a scalar score, SUA\_theta(x), capturing the difference between distributional sensitivity and predictive entropy. We show that minimizing its positive part bounds worst-case perturbed risk and relates to calibration error. We also formalize ambiguity collapse, where models produce overconfident outputs despite multiple valid interpretations.
We introduce SUA-TR, a training method combining consistency regularization and entropy alignment, along with an abstention rule for safer inference. Across tasks including question answering and classification, SUA better identifies model failures than entropy or self-consistency alone.
The framework is model-agnostic and provides a basis for improving reliability in evolving language models.
