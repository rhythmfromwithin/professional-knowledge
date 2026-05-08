---
title: "Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.04066
priority: high
status: unread
interest: medium
next_step: skim
---
# Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning
> 原文: [https://arxiv.org/abs/2605.04066](https://arxiv.org/abs/2605.04066)

arXiv:2605.04066v2 Announce Type: new
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) is an essential paradigm that enhances the reasoning capabilities of Large Language Models (LLMs). However, existing methods typically rely on static policy optimization schemes that misalign with the model's evolving reasoning capabilities. To address this issue, we propose Adaptive Power-Mean Policy Optimization (APMPO), which comprises two main innovations: Power-Mean Policy Optimization (PMPO) and Feedback-Adaptive Clipping (FAC). Specifically, PMPO introduces a generalized power-mean objective. This enables the model to adaptively transition from the signal-amplifying behavior of the arithmetic mean to the consistency-enforcing behavior of the geometric mean. FAC adaptively adjusts clipping bounds based on real-time reward statistics to overcome the limitations of static mechanisms. Capitalizing on these innovations, APMPO improves learning dynamics and reasoning performance. Extensive experiments on nine datasets across three reasoning tasks showcase the superiority of APMPO over state-of-the-art RLVR-based baselines. For instance, APMPO boosts the average Pass@1 score on mathematical reasoning benchmarks by 3.0 points compared to GRPO when using Qwen2.5-3B-Instruct.
