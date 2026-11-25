---
title: "Actionwave: A Systematic Benchmark for Waveform-Centric Clinical Prediction Across Care Scenarios"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2611.31249
priority: high
status: unread
interest: medium
next_step: skim
---
# Actionwave: A Systematic Benchmark for Waveform-Centric Clinical Prediction Across Care Scenarios
> 原文: [https://arxiv.org/abs/2611.31249](https://arxiv.org/abs/2611.31249)

arXiv:2611.31249v1 Announce Type: new
Abstract: Continuous bedside waveforms record rapid physiological changes that can inform clinical decisions. Existing benchmarks examine selected prediction conditions, but it remains unclear how model advantages depend on signal duration, warning time, and available inputs across care settings. We introduce Actionwave, a benchmark for waveform-centric clinical prediction across intensive-care, operating-room, and emergency-department settings. Actionwave uses a common decision-time prediction interface and groups clinically grounded tasks by what is inferred and when. It varies conditions relevant to clinical use, including the warning required before an intervention. We compare diverse architectures and pretrained biosignal encoders under specified model-size and compute budgets. The protocol requires patient-level splits, strict information cutoffs, and comparisons that isolate individual modeling factors. Across 20 tasks and 1.4M task-labelled windows from source datasets, the experimental grids account for over 87,000 model fits. These comparisons identify task-specific choices and show why matched cohorts, unimodal controls, and explicit timing are necessary when interpreting waveform model performance.
