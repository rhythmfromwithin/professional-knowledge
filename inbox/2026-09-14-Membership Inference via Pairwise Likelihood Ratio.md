---
interest: medium
link: https://arxiv.org/abs/2609.12367
next_step: skim
priority: medium
slack_ts: '1789360376.217099'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Membership Inference via Pairwise Likelihood Ratios
---
# Membership Inference via Pairwise Likelihood Ratios
> 原文: [https://arxiv.org/abs/2609.12367](https://arxiv.org/abs/2609.12367)

arXiv:2609.12367v1 Announce Type: new
Abstract: Membership inference attacks (MIAs) are the standard tool for auditing the privacy risks of machine learning models. Given a query point, an MIA aims to determine whether that point was used to train the target model. In practice, such inference must rely on the statistical signals exposed by the model's outputs, such as confidence scores, logits, and intermediate feature representations. However, existing methods often fail to efficiently summarize and combine these statistical signals. To address this limitation, we propose Pairwise Likelihood MIA (PL-MIA), a unified method that combines a Gaussian likelihood-ratio (GLR) statistic with population calibration and the Cauchy combination test. We characterize theoretically how the GLR retains variance-contraction signals and establish conditions under which population calibration and Cauchy combination improve attack power. We obtain $p$-values from pairwise comparisons between the query point and reference points not used for training, and aggregate these continuous signals using the Cauchy combination test. This preserves the evidence strength that is discarded when each pairwise comparison is reduced to a binary vote. Extensive experiments demonstrate that PL-MIA outperforms strong baselines, improving the true positive rate (TPR) by over 25\% in the critical low-false-positive regime, corroborating our theoretical findings. These results demonstrate how statistical principles can turn noisy model outputs into more powerful, calibrated, and reproducible evidence for membership privacy auditing.
