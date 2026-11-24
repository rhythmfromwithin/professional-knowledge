---
title: "SAMA: Training-Free Consensus Ridge Tracking for Camera-Based Heart Rate on Five Public Datasets"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2611.28185
priority: high
status: unread
interest: medium
next_step: skim
---
# SAMA: Training-Free Consensus Ridge Tracking for Camera-Based Heart Rate on Five Public Datasets
> 原文: [https://arxiv.org/abs/2611.28185](https://arxiv.org/abs/2611.28185)

arXiv:2611.28185v1 Announce Type: new
Abstract: Remote photoplethysmography (rPPG) is usually benchmarked by one heart rate per video, a figure that hides the short windows in which a tele-consultation would actually read the pulse. We present SAMA, a training-free estimator that (i) forms a quality-weighted consensus of POS and CHROM chrominance spectra, (ii) discounts frequencies occupied by pulse-free references derived from the same frames (frame motion, skin-mask geometry and background brightness), (iii) follows the heart rate through time with a Viterbi ridge under a random-walk prior, and (iv) returns a track-filtered, amplitude-normalised waveform with a per-window confidence. No parameter is learned and no dataset-specific tuning is used. On 218 recordings from 111 participants in five public datasets (UBFC-rPPG, PURE, SUMS, M3PD and a two-participant subset of MMPD), all processed with the same fixed face box and scored with a re-implementation of the rPPG-Toolbox protocol, SAMA has the lowest mean absolute error (MAE) averaged over datasets at every protocol level: 4.40 against 5.13,bpm for POS per video, 4.80 against 5.43 on 30,s windows and 5.05 against 6.59 on 10,s windows. Pooled over participants, the bootstrap interval of its paired difference from POS excludes zero on 30,s and 10,s windows (Wilcoxon p=0.11 and 0.004) but not per video, and it does not beat POS on SUMS per video or on the MMPD subset. Withholding the 20\% least confident windows lowers the pooled 10,s error from 4.06 to 2.33,bpm. We also show that the per-video protocol has a floor of 1.2--1.6,bpm on datasets where heart rate drifts, and that skin tone cannot be recovered from uncalibrated video, which motivates the instrumented, skin-tone-stratified collection we propose for the Indian population. The method does not surpass the best published neural networks on UBFC-rPPG; we report where it stands against them without re-running them.
