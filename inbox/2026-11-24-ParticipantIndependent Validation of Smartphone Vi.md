---
title: "Participant-Independent Validation of Smartphone Video and Wearable Inertial Sensing for Coach-Rated Running-Form Classification"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2611.27996
priority: low
status: unread
interest: medium
next_step: skim
---
# Participant-Independent Validation of Smartphone Video and Wearable Inertial Sensing for Coach-Rated Running-Form Classification
> 原文: [https://arxiv.org/abs/2611.27996](https://arxiv.org/abs/2611.27996)

arXiv:2611.27996v1 Announce Type: new
Abstract: Automated running-form assessment could make technique feedback more accessible outside professional coaching and laboratory settings. We evaluated a low-cost pipeline combining side-view smartphone video with wearable inertial measurement unit (IMU) acceleration for coach-rated running-form classification. The dataset comprised 294 labeled recordings from 20 runners and 1,555 windows across four cues: landing position, suspension, triple extension, and upper-body posture. The primary analysis used 100 repeated four-runner holdout splits, recording-level aggregation of window predictions, and LightGBM models with hyperparameters fixed from prior modality-specific searches. Video-only LightGBM achieved mean macro F1 of 0.310, versus 0.168 for a majority-class baseline. Adding IMU features reduced macro F1 to 0.267, a paired mean difference of -0.043. Robustness analysis with Logistic Regression, Linear SVM, Random Forest, XGBoost, and LightGBM found that video-only models had higher mean performance than the majority baseline, whereas fusion effects depended on model family: Linear SVM showed a small positive effect, Logistic Regression was approximately neutral, and tree-based models showed lower performance with fusion. These results indicate a modest participant-independent signal in smartphone pose features. However, apparent IMU-fusion gains depended strongly on validation design, model family, and target category. The gap between recording-level and participant-independent performance underscores the need for runner-holdout evaluation and suggests that simple feature-level fusion does not reliably generalize to unseen runners.
