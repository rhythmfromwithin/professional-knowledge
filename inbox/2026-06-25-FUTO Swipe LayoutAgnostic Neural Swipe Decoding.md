---
interest: medium
link: https://arxiv.org/abs/2606.25247
next_step: skim
priority: low
slack_ts: '1782360759.954749'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'FUTO Swipe: Layout-Agnostic Neural Swipe Decoding'
---
# FUTO Swipe: Layout-Agnostic Neural Swipe Decoding
> 原文: [https://arxiv.org/abs/2606.25247](https://arxiv.org/abs/2606.25247)

arXiv:2606.25247v1 Announce Type: new
Abstract: Neural swipe decoders are typically tied to the keyboard they were trained on, requiring a new corpus and training run for each layout. In this report, we document our approach toward training models that can function on any contiguous mobile keyboard layout. At each point along the swipe, our encoder predicts whether the user is indicating a character and where on the keyboard that character lies. The keyboard layout is supplied at inference time and used to map the spatial and temporal prediction to a logit at each key, rather than being learned during training.
Training neural models requires substantial data, but public swipe data is limited, particularly for non-QWERTY layouts. We release swipe.futo.org, the largest MIT-licensed swipe corpus we are aware of, containing over 1M donated swipes from more than 12k donor sessions. To generalize beyond the English QWERTY layout, we apply geometric augmentations to both the swipe trajectory and the keyboard layout at every training step, forcing the model to make predictions based on characteristics of the swipe gesture rather than the training layout. The model generalizes to layouts absent from training, in some cases more accurately than the layout it was trained on. This combines the layout-flexibility of an algorithmic decoder with the accuracy of a neural model. Trained models are publicly available.
