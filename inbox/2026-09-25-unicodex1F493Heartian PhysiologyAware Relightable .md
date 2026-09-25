---
title: "$\unicode{x1F493}$Heartian: Physiology-Aware Relightable Gaussian Head Avatar"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.28539
priority: medium
status: unread
interest: medium
next_step: skim
---
# $\unicode{x1F493}$Heartian: Physiology-Aware Relightable Gaussian Head Avatar
> 原文: [https://arxiv.org/abs/2609.28539](https://arxiv.org/abs/2609.28539)

arXiv:2609.28539v1 Announce Type: new
Abstract: Gaussian head avatars typically model intrinsic facial appearance as temporally static, omitting subtle cardiac-induced skin-color variation. We propose $\unicode{x1F493}$Heartian, a physiology-aware modulation framework that learns cardiac-cycle-dependent per-frame albedo modulation of facial skin-region Gaussians within a relightable head avatar to encode remote photoplethysmography (rPPG) signals. Using synchronized contact PPG supervision, $\unicode{x1F493}$Heartian models the prescribed cardiac waveform as the sum of two Gaussian functions and learns per-frame spatial residuals via a lightweight MLP. Across 152 stationary recordings from UBFC-rPPG, PURE, and MMPD, attribute-space recovery of the supplied signal achieves a pooled recording-level heart-rate MAE of 0.29 bpm and MAPE of 0.38%. The signals remain detectable after rendering by benchmark rPPG methods, with the best tested configuration - a motion-augmented TS-CAN decoder pretrained on UBFC-rPPG - recovering heart rate from the rendered MMPD avatars at 0.97 bpm MAE and 1.21% MAPE. Meanwhile, $\unicode{x1F493}$Heartian maintains reconstruction quality comparable to the baseline, with negligible average PSNR degradation of 0.005 dB. Overall, our work embeds recoverable rPPG signals as controllable material attributes to subject-specific Gaussian head avatars while retaining the reconstruction quality.
