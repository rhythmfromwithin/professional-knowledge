---
interest: medium
link: https://arxiv.org/abs/2606.17106
next_step: skim
priority: high
slack_ts: '1781672192.638839'
source: cs.LG - Machine Learning
status: unread
title: Informative Missingness to Generate Irregular Clinical Time Series
---
# Informative Missingness to Generate Irregular Clinical Time Series
> 原文: [https://arxiv.org/abs/2606.17106](https://arxiv.org/abs/2606.17106)

arXiv:2606.17106v1 Announce Type: new
Abstract: Laboratory tests in electronic health records are collected irregularly, and the absence of a test order can be as informative as the measurement itself. Such missingness reflects clinicians' decisions and patient physiology, making it important to model it directly rather than treat it as a preprocessing artifact. Here we present a diffusion-based approach for generating clinical time series that jointly models laboratory values and their observation patterns using the public Data Analytics Challenge on Missing Data Imputation (DACMI) benchmark derived from MIMIC-III. To preserve realistic sampling, we align chart times into 4-hour intervals and segment admissions into 7-day windows, producing trajectories that pair each lab value with a corresponding observation indicator. Standard transformations and normalization are applied to stabilize training. Our method extends the TimeDiff framework to learn continuous lab values and discrete missingness patterns through complementary diffusion objectives. Experiments show that the generated data closely match real patient trajectories across individual lab distributions and joint value-missingness embeddings, demonstrating that diffusion models can capture clinically meaningful dependencies between patient physiology and clinicians' testing behavior under MNAR-like (missing-not-at-random) missingness. These preliminary results indicate that our model can serve as an initial component toward developing clinical foundation models. By producing synthetic priors that preserve key physiology-missingness relationships, this work motivates the subsequent training of Prior-Data Fitted Networks capable of leveraging informative missingness, which we will investigate in the extended work.
