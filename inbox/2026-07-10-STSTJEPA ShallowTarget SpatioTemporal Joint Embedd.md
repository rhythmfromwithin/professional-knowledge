---
title: "STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2607.06629
priority: low
status: unread
interest: medium
next_step: skim
---
# STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning
> 原文: [https://arxiv.org/abs/2607.06629](https://arxiv.org/abs/2607.06629)

arXiv:2607.06629v2 Announce Type: cross
Abstract: Brain age - the age inferred from a physiological recording - is an emerging biomarker whose deviation from chronological age tracks neurological and psychiatric burden, and EEG is an attractive substrate for it because it is cheap, portable, and temporally rich. Yet EEG brain-age models must contend with cross-site montage heterogeneity, small labelled cohorts, and dominant subject-level non-stationarity, and few EEG foundation models have been shown to deliver competitive age regression across the full pediatric to older adult range in which such a biomarker would actually be deployed. We introduce STST-JEPA, a self-supervised transformer for resting-state and task EEG, pretrained on 47,703 sessions spanning ages 5-81 from the brain.space and Healthy Brain Network (HBN) corpora. The model combines a latent-prediction objective - predicting masked-token representations against an EMA-of-tokenizer target - with an auxiliary signal-reconstruction term, applied to 30-second multi-channel windows under spatiotemporal block masks. A lightweight attentive probe trained on frozen pretrained embeddings achieves a best held-out-validation mean absolute error of 3.06 years (r = 0.924) for age regression on 3,367 sessions, against a predict-the-mean baseline of approximately 10 years MAE. With light task-specific finetuning of the model's final layers, the same pretrained encoder achieves rank-1 placements - with the model's native 30-second windows - on the public NeuralBench x brain.space EEG leaderboard for sex classification (balanced accuracy 0.911), age prediction (r = 0.749), and psychopathology composite regression (r = 0.215). We further show that the model's age-prediction residual is negatively correlated with cognitive efficiency over several tasks we examined.
