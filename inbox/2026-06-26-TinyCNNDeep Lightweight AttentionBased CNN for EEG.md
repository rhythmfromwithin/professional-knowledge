---
title: "TinyCNNDeep: Lightweight Attention-Based CNN for EEG Classification of Eye States and Sleep Deprivation"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2606.26506
priority: low
status: unread
interest: medium
next_step: skim
---
# TinyCNNDeep: Lightweight Attention-Based CNN for EEG Classification of Eye States and Sleep Deprivation
> 原文: [https://arxiv.org/abs/2606.26506](https://arxiv.org/abs/2606.26506)

arXiv:2606.26506v1 Announce Type: new
Abstract: Sleep deprivation impairs vigilance and cognitive function, yet jointly identifying the sleep condition (normal vs deprived) and the eye state (open vs closed) from electroencephalography (EEG) remains underexplored. We address this four-class problem with TinyCNNDeep, a lightweight convolutional neural network that combines residual learning with a Squeeze-and-Excitation (SE) attention module. We convert short multi-channel EEG segments from five physiologically relevant channels (Fp1, Fp2, O1, Oz, O2) into 224x224 grayscale images through per-channel Z-score normalization, min-max scaling, and center padding, enabling 2D convolutions to jointly model inter-channel and temporal structure. On a 35-subject dataset recorded under normal-sleep and sleep-deprivation sessions, TinyCNNDeep attains a subject-wise mean accuracy of 83.69%, outperforming the strongest baseline (Random Forest with combined time-frequency features, 47.66%) by 36.03 percentage points, while three established EEG architectures (EEGNet, ShallowConvNet, DeepConvNet) operate near chance. Per-subject analysis quantifies inter-subject variability, and confusion-matrix inspection shows that residual misclassifications concentrate between eyes-closed states across sleep conditions. These results indicate that an image-based EEG representation paired with residual feature extraction and channel attention provides an accurate and computationally efficient framework for multiclass sleep-related EEG classification under a minimal electrode configuration.
