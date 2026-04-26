---
interest: medium
link: https://arxiv.org/abs/2604.20909
next_step: skim
priority: high
slack_ts: '1777174931.055409'
source: cs.LG - Machine Learning
status: unread
title: Do Masked Autoencoders Improve Downhole Prediction? An Empirical Study on Real
  Well Drilling Data
---
# Do Masked Autoencoders Improve Downhole Prediction? An Empirical Study on Real Well Drilling Data
> 原文: [https://arxiv.org/abs/2604.20909](https://arxiv.org/abs/2604.20909)

arXiv:2604.20909v1 Announce Type: new
Abstract: Downhole drilling telemetry presents a fundamental labeling asymmetry: surface sensor data are generated continuously at 1~Hz, while labeled downhole measurements are costly, intermittent, and scarce. Current machine learning approaches for downhole metric prediction universally adopt fully supervised training from scratch, which is poorly suited to this data regime. We present the first empirical evaluation of masked autoencoder (MAE) pretraining for downhole drilling metric prediction. Using two publicly available Utah FORGE geothermal wells comprising approximately 3.5 million timesteps of multivariate drilling telemetry, we conduct a systematic full-factorial design space search across 72 MAE configurations and compare them against supervised LSTM and GRU baselines on the task of predicting Total Mud Volume. Results show that the best MAE configuration reduces test mean absolute error by 19.8\% relative to the supervised GRU baseline, while trailing the supervised LSTM baseline by 6.4\%. Analysis of design dimensions reveals that latent space width is the dominant architectural choice (Pearson $r = -0.59$ with test MAE), while masking ratio has negligible effect, an unexpected finding attributed to high temporal redundancy in 1~Hz drilling data. These results establish MAE pretraining as a viable paradigm for drilling analytics and identify the conditions under which it is most beneficial.
