---
title: "EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2605.26910
priority: low
status: unread
interest: medium
next_step: skim
---
# EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models
> 原文: [https://arxiv.org/abs/2605.26910](https://arxiv.org/abs/2605.26910)

arXiv:2605.26910v1 Announce Type: cross
Abstract: Large EEG Foundation Models (FMs) have shown great potential for decoding EEG signals across diverse cognitive tasks. However, existing EEG-FM studies exhibit three critical limitations: opaque supervised baseline tuning, unverified contributions of complex learning paradigms, and a lack of transparency in model decision-making. To address these, we propose EEG-FM-Audit, a comprehensive evaluation and analysis pipeline designed to systematize the assessment of EEG-FMs. EEG-FM-Audit consists of three primary components: (1) an ASHA-driven benchmarking protocol that ensures fair comparisons by transparently optimizing supervised baselines; (2) paradigm-level ablation studies to evaluate the effectiveness of learning paradigms in FMs; and (3) a neurophysiological probing (NPP) framework, which explores whether FMs leverage valid temporal, spatial, and spectral EEG properties. We apply EEG-FM-Audit to four state-of-the-art EEG-FMs and five representative supervised models across three public datasets. Our results reveal that properly tuned supervised baselines can match or outperform advanced FMs, despite requiring significantly fewer parameters. Furthermore, we find that the effectiveness of learning paradigms of FMs is highly dependent on dataset scale and architecture. Finally, NPP analysis demonstrates how FMs rely on specific physiological features, establishing a framework for more interpretable neural decoding.
