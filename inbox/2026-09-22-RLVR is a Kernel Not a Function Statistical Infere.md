---
title: "RLVR is a Kernel, Not a Function: Statistical Inference for pass@$k$ Crossovers"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.22547
priority: medium
status: unread
interest: medium
next_step: skim
---
# RLVR is a Kernel, Not a Function: Statistical Inference for pass@$k$ Crossovers
> 原文: [https://arxiv.org/abs/2609.22547](https://arxiv.org/abs/2609.22547)

arXiv:2609.22547v1 Announce Type: new
Abstract: Reinforcement learning with verifiable rewards (RLVR) often improves pass@1 while falling behind its base model at larger sampling budgets $k$, a crossover read as evidence that RLVR only sharpens existing capability. We identify two limits to this reading. First, a visible crossing need not be statistically established: comparing models on the same prompts, we build confidence bands across sampling budgets $k$ that require evidence of both an early gain and a later loss. Across five public RLVR pairs no crossing is statistically established in the initial evaluations, while a 32k-token evaluation on fresh prompts locates a reversal with first loss between 11 and 61 samples; power analysis shows why failure to detect a crossing need not mean no crossing, and why more prompts can help more than more answers per prompt. Second, base success alone does not determine what RLVR does to a prompt: prompts with the same base success rate have different post-RL success rates, and these differences repeat across independent generation halves. The relationship is a conditional distribution---a Markov kernel---rather than a single curve, and fitting it predicts crossings in independent generations for the same prompts and corrects the simple model's power estimates. Theory further shows how losses on a minority of the hardest prompts can overturn an early lead even when training improves other prompts, separating evidence that a crossover exists from claims about what it means for capability.
