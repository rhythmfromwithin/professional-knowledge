---
title: "Uncertainty-Aware Simulation-Based Inference for Operations Research with Large Language Models"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2608.00019
priority: high
status: unread
interest: medium
next_step: skim
---
# Uncertainty-Aware Simulation-Based Inference for Operations Research with Large Language Models
> 原文: [https://arxiv.org/abs/2608.00019](https://arxiv.org/abs/2608.00019)

arXiv:2608.00019v1 Announce Type: new
Abstract: Deploying large language models (LLMs) for operations research (OR) tasks remains challenging because correctness depends on a coherent modeling process, not merely a correct final answer. Standard autoregressive generation operates on a myopic policy, which sometimes fails to anticipate whether a partial formulation can be validly extended into a globally consistent optimization model. Consequently, locally plausible steps may propagate into catastrophic downstream formulation or solver code errors. To address this, we propose an uncertainty-aware, training-free inference framework for OR mathematical modeling. Without updating model parameters, our method evaluates intermediate candidate steps using short lookahead simulations to quantify downstream predictive uncertainty or probability concentration. Candidates that demonstrate a higher likelihood of yielding coherent mathematical formulations are then dynamically selected via importance resampling. Empirical evaluations across multiple OR benchmarks (including NL4OPT, MAMO, and IndustryOR) demonstrate that our framework consistently outperforms both standard and low-temperature baselines, establishing an efficient, training-free paradigm for reliable OR formulation generation.
