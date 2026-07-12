---
interest: medium
link: https://arxiv.org/abs/2607.07739
next_step: skim
priority: low
slack_ts: '1783827429.544579'
source: cs.CR - Cryptography and Security
status: unread
title: Controllability-Aware Adversarial Examples Against LLM-Based Network Traffic
  Classifiers
---
# Controllability-Aware Adversarial Examples Against LLM-Based Network Traffic Classifiers
> 原文: [https://arxiv.org/abs/2607.07739](https://arxiv.org/abs/2607.07739)

arXiv:2607.07739v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly explored as network intrusion detection classifiers, but their adversarial robustness under realistic attacker constraints remains unclear. We present a controllability-aware black-box transfer framework for LLM-based network traffic classifiers. The framework partitions flow features into directly controllable (DC), indirectly controllable (IC), and uncontrollable (UC) groups according to network communication semantics, then restricts perturbations to DC features while freezing IC/UC features. Using a shared XGBoost surrogate, we generate finite-difference PGD, greedy coordinate-wise, and NES adversarial examples and transfer them to seven LLM targets and two conventional ML targets across five IDS benchmarks from 1999 to 2022. Across 27 valid LLM configurations and over 500,000 adversarial examples, we find that LLM transfer vulnerability is substantial but dataset- and comparator-dependent. Compared with LightGBM, LLMs are more vulnerable on RT-IoT2022 and CIC-IDS-2018, comparable on NSL-KDD and UNSW-NB15, and less vulnerable on HIKARI-2021; compared with the averaged ML baseline, LLMs show higher ASR on all five datasets. We further observe a consistent cross-architecture transfer hierarchy: gradient- and score-based perturbations transfer more effectively than greedy perturbations across all 27 LLM cells and 9/10 ML cells. Cross-surrogate validation with tree, neural, and linear surrogates yields similar LLM ASR, reducing evidence that the findings are XGBoost-specific. Constraint violation rate is 0\% by construction.
