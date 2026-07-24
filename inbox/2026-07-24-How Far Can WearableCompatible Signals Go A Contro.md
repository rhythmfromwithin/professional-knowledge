---
interest: medium
link: https://arxiv.org/abs/2607.19441
next_step: skim
priority: low
slack_ts: '1784863644.395929'
source: cs.HC - Human-Computer Interaction
status: unread
title: How Far Can Wearable-Compatible Signals Go? A Controlled Decomposition of Non-EEG
  Sleep Staging
---
# How Far Can Wearable-Compatible Signals Go? A Controlled Decomposition of Non-EEG Sleep Staging
> 原文: [https://arxiv.org/abs/2607.19441](https://arxiv.org/abs/2607.19441)

arXiv:2607.19441v1 Announce Type: new
Abstract: Consumer wearables increasingly infer sleep stages from signals including heart rate, accelerometry, and photoplethysmography. However, existing studies often report end-to-end performance under a fixed signal setting, making it difficult to determine whether the observed performance comes from genuine physiological decoding, temporal priors, or dataset-specific confounds. To address this limitation, we introduce a four-layer controlled decomposition framework for non-EEG sleep staging, covering signal source, physiological representation, temporal prior, and decision layers. The framework is evaluated across a signal-quality ladder spanning Apple Watch Sleep-Accel ($N=31$), the Sleep Heart Health Study ($N=195$, laboratory ECG, respiratory, and SpO$\_2$ signals), and Sleep-EDF-20 as an EEG+EOG reference, using the same compact Mamba2 model throughout. Laboratory cardiorespiratory signals reach $\kappa=0.492$, while EEG+EOG reaches $\kappa=0.796$, leaving a residual gap of $\Delta\kappa=+0.304$ that reflects missing cortical information rather than temporal modeling alone. Consumer HR/ACC reaches only $\kappa=0.255$, quantifying the additional penalty of derived wearable signals and real-world sensing constraints. Confidence-based abstention provides a calibrated operating mode: removing the 20% lowest-confidence epochs increases $\kappa$ from $0.452$ to $0.512$, while a label-shuffled control collapses to $\kappa=-0.003$. These results support non-EEG sleep staging as coarse, confidence-aware sleep-structure monitoring rather than EEG-equivalent five-class clinical staging.
