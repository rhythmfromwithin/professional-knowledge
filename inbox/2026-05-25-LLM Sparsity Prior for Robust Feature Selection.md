---
interest: medium
link: https://arxiv.org/abs/2605.23102
next_step: skim
priority: medium
slack_ts: '1779856023.263769'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: LLM Sparsity Prior for Robust Feature Selection
---
# LLM Sparsity Prior for Robust Feature Selection
> 原文: [https://arxiv.org/abs/2605.23102](https://arxiv.org/abs/2605.23102)

arXiv:2605.23102v1 Announce Type: new
Abstract: Large language models (LLMs) offer a scalable mechanism to elicit domain-informed prior information for high-dimensional variable selection. However, existing methods such as LLM-Lasso are sensitive to weight quality, with performance degrading substantially when LLM-generated weights are inaccurate. To address this challenge, we first introduce a framework for quantifying the quality of LLM-generated weights, enabling rigorous evaluation of LLM-informed methods across varying weight regimes. We then propose the LLM Sparsity Prior (LSP), which integrates LLM-generated weights into the prior inclusion probabilities of Spike-and-Slab and Spike-and-Slab Lasso models via two interpretable hyperparameters governing global sparsity and weight concentration. Hierarchical hyperpriors on these parameters allow the model to dynamically discount uninformative or misleading weights, improving robustness without sacrificing gains when weights are accurate. Finally, we develop principled prompt engineering strategies and validate the method on a private medical dataset studying Acute Kidney Injury. LSP improves prediction accuracy and identifies clinically relevant features missed by the baselines, with robustness to prompt variation and particular effectiveness in low-data regimes.
