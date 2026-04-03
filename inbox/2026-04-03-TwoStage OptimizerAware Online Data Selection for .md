---
interest: medium
link: https://arxiv.org/abs/2604.00001
next_step: skim
priority: high
slack_ts: '1775185094.553139'
source: cs.LG - Machine Learning
status: unread
title: Two-Stage Optimizer-Aware Online Data Selection for Large Language Models
---
# Two-Stage Optimizer-Aware Online Data Selection for Large Language Models
> 原文: [https://arxiv.org/abs/2604.00001](https://arxiv.org/abs/2604.00001)

arXiv:2604.00001v1 Announce Type: new
Abstract: Gradient-based data selection offers a principled framework for estimating sample utility in large language model (LLM) fine-tuning, but existing methods are mostly designed for offline settings. They are therefore less suited to online fine-tuning, where data arrives sequentially, sample utility is step-dependent, and the effective update geometry is shaped by adaptive optimizers. We propose an optimizer-aware framework for gradient-based online data selection and reweighting in LLM fine-tuning. Our key idea is to view online selection not as static sample ranking, but as shaping the next target-oriented update under the optimizer state. We formulate this as an optimizer-aware update-matching problem, establish its connection to second-order target utility, and show why subset-level construction must account for interactions and redundancy among selected samples. Based on this view, we develop a two-stage Filter-then-Weight algorithm that first filters geometrically useful candidates and then optimizes their coefficients. To make the framework practical for LLMs, we introduce a factorized outer-product gradient representation and optimized matrix computations for long-context data. Experiments show that our method consistently improves convergence and downstream performance over existing online data selection baselines under the same data budget.
