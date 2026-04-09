---
interest: medium
link: https://arxiv.org/abs/2604.03257
next_step: skim
priority: high
slack_ts: '1775703385.177379'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation
---
# Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation
> 原文: [https://arxiv.org/abs/2604.03257](https://arxiv.org/abs/2604.03257)

arXiv:2604.03257v1 Announce Type: new
Abstract: The ability to rigorously estimate the failure rates of large language models (LLMs) is a prerequisite for their safe deployment. Currently, however, practitioners often face a tradeoff between expensive human gold standards and potentially severely-biased automatic annotation schemes such as "LLM-as-a-Judge" labeling. In this paper, we propose a new, practical, and efficient approach to LLM failure rate estimation based on constrained maximum-likelihood estimation (MLE). Our method integrates three distinct signal sources: (i) a small, high-quality human-labeled calibration set, (ii) a large corpus of LLM-judge annotations, and, most importantly, (iii) additional side information via domain-specific constraints derived from known bounds on judge performance statistics. We validate our approach through a comprehensive empirical study, benchmarking it against state-of-the-art baselines like Prediction-Powered Inference (PPI). Across diverse experimental regimes -- spanning varying judge accuracies, calibration set sizes, and LLM failure rates -- our constrained MLE consistently delivers more accurate and lower-variance estimates than existing methods. By moving beyond the "black-box" use of automated judges to a flexible framework, we provide a principled, interpretable, and scalable pathway towards LLM failure-rate certification.
