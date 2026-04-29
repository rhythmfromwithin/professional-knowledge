---
title: "KARL: Mitigating Hallucinations in LLMs via Knowledge-Boundary-Aware Reinforcement Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.22779
priority: high
status: unread
interest: medium
next_step: skim
---
# KARL: Mitigating Hallucinations in LLMs via Knowledge-Boundary-Aware Reinforcement Learning
> 原文: [https://arxiv.org/abs/2604.22779](https://arxiv.org/abs/2604.22779)

arXiv:2604.22779v1 Announce Type: new
Abstract: Enabling large language models (LLMs) to appropriately abstain from answering questions beyond their knowledge is crucial for mitigating hallucinations. While existing reinforcement learning methods foster autonomous abstention, they often compromise answer accuracy because their static reward mechanisms, agnostic to models' knowledge boundaries, drive models toward excessive caution. In this work, we propose KARL, a novel framework that continuously aligns an LLM's abstention behavior with its evolving knowledge boundary. KARL introduces two core innovations: a Knowledge-Boundary-Aware Reward that performs online knowledge boundary estimation using within-group response statistics, dynamically rewarding correct answers or guided abstention; and a Two-Stage RL Training Strategy that first explores the knowledge boundary and bypasses the "abstention trap", and subsequently converts incorrect answers beyond the knowledge boundary into abstentions without sacrificing accuracy. Extensive experiments on multiple benchmarks demonstrate that KARL achieves a superior accuracy-hallucination trade-off, effectively suppressing hallucinations while maintaining high accuracy across both in-distribution and out-of-distribution scenarios.
