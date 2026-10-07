---
title: "TEMPEST: Temporal Embeddings for Scalable Driver Identification via Angular Margin Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.06855
priority: high
status: unread
interest: medium
next_step: skim
---
# TEMPEST: Temporal Embeddings for Scalable Driver Identification via Angular Margin Learning
> 原文: [https://arxiv.org/abs/2610.06855](https://arxiv.org/abs/2610.06855)

arXiv:2610.06855v1 Announce Type: new
Abstract: Scalable driver identification requires embedding models that maintain discriminative performance as fleet size grows, yet existing triplet-loss formulations degrade rapidly with driver pool size and overfit to session-specific patterns under rigorous temporal evaluation. We introduce TEMPEST, a Temporal Convolutional Network embedding model trained with an additive angular margin (ArcFace) loss that enforces global class-level separation in a normalized angular space. TEMPEST maps 60-second multimodal driving windows to compact 96-dimensional embeddings, supporting truly dynamic enrollment without any retraining or classifier refitting. Under rigorous temporal evaluation on a 45-driver dataset, TEMPEST achieves 91.71% Rank-1 accuracy, outperforming the best classical model by 17.9 pp and the strongest triplet-loss baseline by 58.4 pp. TEMPEST degrades by only 4.3 pp when growing the subject pool from 10 to 45 drivers, compared to 22 pp and 32.5 pp for supervised and unsupervised triplet-loss baselines, and its cross-session advantage is corroborated on the public KIA Soul dataset, where it outperforms the best classical model by 7.3 pp within-session and 14.3 pp cross-session. With 720K parameters, a 2.80 MB footprint, and 50-epoch convergence, TEMPEST establishes a rigorous, reproducible baseline for scalable behavioral driver biometric identification.
