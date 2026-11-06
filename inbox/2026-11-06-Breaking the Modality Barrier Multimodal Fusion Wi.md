---
title: "Breaking the Modality Barrier: Multimodal Fusion With Missing Modalities for Cybersickness Prediction"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2611.07386
priority: low
status: unread
interest: medium
next_step: skim
---
# Breaking the Modality Barrier: Multimodal Fusion With Missing Modalities for Cybersickness Prediction
> 原文: [https://arxiv.org/abs/2611.07386](https://arxiv.org/abs/2611.07386)

arXiv:2611.07386v1 Announce Type: new
Abstract: Cybersickness is a major barrier to comfortable VR use, and reliable prediction often requires multiple physiological and behavioral sensors. However, existing models typically assume a fixed set of modalities, making them vulnerable when sensors are unavailable and difficult to generalize across datasets with different sensor configurations. We adapt a transformer-based model that handles arbitrary sensor combinations without imputing missing data. Anchor-based contrastive learning maps heterogeneous sensor embeddings into a shared latent space using eye tracking as the anchor modality, while masked self-attention excludes unavailable sensors during fusion. We evaluate our approach on three publicly available cybersickness datasets: VR.net, SIM21, and Blur-Rollercoaster, collected using different VR systems and sensor configurations. Across single-sensor dropout conditions, prediction error changes by less than 0.09 MAE. Joint training across all datasets achieves 0.51 MAE and 0.63 Pearson correlation, substantially outperforming single-dataset models. These results demonstrate robust and generalizable cybersickness prediction across diverse VR systems.
