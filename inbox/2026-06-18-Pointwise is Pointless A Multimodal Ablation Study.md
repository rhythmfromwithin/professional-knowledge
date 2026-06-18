---
interest: medium
link: https://arxiv.org/abs/2606.18436
next_step: skim
priority: medium
slack_ts: '1781759643.898289'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Pointwise is Pointless? A Multimodal Ablation Study for Precipitation Nowcasting
  with Graph Neural Networks
---
# Pointwise is Pointless? A Multimodal Ablation Study for Precipitation Nowcasting with Graph Neural Networks
> 原文: [https://arxiv.org/abs/2606.18436](https://arxiv.org/abs/2606.18436)

arXiv:2606.18436v1 Announce Type: new
Abstract: Sparse point observations are increasingly available for precipitation nowcasting, but it is unclear how much they improve dense radar-field forecasts. We partially address this question with a multimodal graph neural network nowcasting system over the Nordic radar domain. The model predicts rain rate every five minutes up to two hours ahead and is trained with different combinations of radar history, MEPS numerical weather prediction, Netatmo surface observations, MSG satellite channels, stochastic noise, and CRPS-based ensemble losses. The study is designed as an ablation of operationally relevant information sources and training objectives. We compare radar-only, NWP-informed, station-informed, satellite-informed, noise-augmented, and CRPS-based configurations using complementary diagnostics on the radar grid, at station locations, for rain onset, and through oracle, displacement, and amplitude scores. The results show that each source improves a different part of the forecast problem. MEPS stabilises radar-only extrapolation, Netatmo observations improve local station and onset diagnostics, and satellite predictors reduce some station-level biases but may activate rain too early when used deterministically. CRPS-based configurations provide the most consistent radar-grid gains, while the combined satellite and CRPS setup gives the best overall oracle/DAS score. These results do not support the conclusion that point observations are uninformative for nowcasting, but they show that local observational skill and spatially coherent radar-field skill are distinct targets. The practical implication is that sparse observations can provide useful local constraints, but their benefit for radar-like fields depends on the training loss, uncertainty representation, and how observation support is encoded in the model.
