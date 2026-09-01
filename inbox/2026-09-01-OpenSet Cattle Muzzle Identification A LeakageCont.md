---
title: "Open-Set Cattle Muzzle Identification: A Leakage-Controlled Benchmark and Evaluation Protocol"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.28663
priority: medium
status: unread
interest: medium
next_step: skim
---
# Open-Set Cattle Muzzle Identification: A Leakage-Controlled Benchmark and Evaluation Protocol
> 原文: [https://arxiv.org/abs/2608.28663](https://arxiv.org/abs/2608.28663)

arXiv:2608.28663v1 Announce Type: new
Abstract: Reliable individual cattle identification supports disease surveillance, vaccination records, breeding management, and livestock insurance. Although the bovine muzzle provides a stable, non-contact biometric, existing muzzle-recognition systems largely assume a closed set of enrolled animals, limiting their practical deployment. We reformulate cattle muzzle biometrics as an open-set, gallery-based identification problem that can reject previously unseen animals and support incremental enrollment without model retraining. We introduce a leakage-controlled evaluation protocol based on identity-disjoint splits, per-fold retraining, held-out threshold calibration, verified duplicate removal, and bootstrap confidence intervals. We evaluate the framework using two contrasting embedding configurations: a hybrid CNN-ViT metric-learning model and the MegaDescriptor-L foundation model. Under oracle threshold selection, the hybrid model achieves detection-and-identification rates of 98.3%, 96.4%, and 93.6% at target false-acceptance rates of 10^(-1), 10^(-2), and 10^(-3), respectively, while MegaDescriptor-L achieves 99.3%, 98.1%, and 96.1%. However, deployable threshold calibration reveals a substantial difference between oracle and calibrated performance: the hybrid model achieves a false-acceptance rate of 1.03% at a 1% target, whereas MegaDescriptor-L reaches 2.44%. Incremental enrollment further achieves Rank-1 accuracy above 91% with a single reference image and up to 97.3% with eight reference images, without retraining the model or degrading the existing gallery. These results demonstrate that threshold calibration, leakage control, and embedding quality are critical for reliable open-set cattle identification and provide a practical evaluation framework for deployment-oriented animal biometric systems.
