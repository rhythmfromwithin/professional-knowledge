---
title: "Isotonic Survival Regression: Calibrated Survival Distributions from Deep Cox Models"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.16571
priority: medium
status: unread
interest: medium
next_step: skim
---
# Isotonic Survival Regression: Calibrated Survival Distributions from Deep Cox Models
> 原文: [https://arxiv.org/abs/2605.16571](https://arxiv.org/abs/2605.16571)

arXiv:2605.16571v1 Announce Type: new
Abstract: Time-to-event data is widespread across the life sciences and engineering, but it is typically encountered together with censoring, which complicates the application of standard machine learning methods. Deep Cox models have emerged as a popular method for analyzing time-to-event data because they gracefully handle censoring and can be used with unstructured data such as clinical text reports, genomic sequences, and pathology images. However, their predicted survival probabilities are often poorly calibrated, thus limiting their practical utility. In this paper, we propose a novel post hoc calibration method for Deep Cox models that uses isotonic regression to refine predicted survival probabilities without affecting discriminative power. We establish favorable theoretical guarantees, including a double-robustness property and asymptotic calibration. Experiments on synthetic and real-world clinical data demonstrate the empirical effectiveness of our method.
