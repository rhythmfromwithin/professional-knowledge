---
title: "A Masked Autoencoder Approach to Unsupervised Steel Surface Defect Recognition"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.13178
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Masked Autoencoder Approach to Unsupervised Steel Surface Defect Recognition
> 原文: [https://arxiv.org/abs/2607.13178](https://arxiv.org/abs/2607.13178)

arXiv:2607.13178v1 Announce Type: new
Abstract: Automated visual inspection of steel surface defects is a recurring quality control task in which labeled defect data is scarce and costly to obtain, while unlabeled surface images are abundant, which motivates self supervised methods that learn useful representations without class labels. A Transformer based Masked Autoencoder is used here to learn representations of steel surface defects for unsupervised grouping. During pretraining, 75% of the input image patches are randomly masked, and a lightweight decoder reconstructs the masked regions from the visible 25%. The encoder is trained jointly with an auxiliary defect localization objective, used only as a training signal and not evaluated as a detector. The decoder reaches a structural similarity score of 0.92 and a mean squared error of 0.47. Features from the pretrained encoder are then clustered using UMAP for dimensionality reduction and Agglomerative clustering, reaching a Hungarian matched accuracy of 91.3% against the six known defect categories.
