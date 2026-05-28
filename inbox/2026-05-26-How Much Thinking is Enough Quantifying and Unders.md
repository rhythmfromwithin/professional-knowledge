---
interest: medium
link: https://arxiv.org/abs/2605.23926
next_step: skim
priority: high
slack_ts: '1779941825.592679'
source: cs.AI - Artificial Intelligence
status: unread
title: How Much Thinking is Enough? Quantifying and Understanding Redundancy in LLM
  Reasoning
---
# How Much Thinking is Enough? Quantifying and Understanding Redundancy in LLM Reasoning
> 原文: [https://arxiv.org/abs/2605.23926](https://arxiv.org/abs/2605.23926)

arXiv:2605.23926v1 Announce Type: new
Abstract: Reasoning-capable large language models solve hard problems by emitting long chains of thought, paying heavily in latency, GPU time, and energy. Casual inspection of their traces reveals extensive reformulation, verification, and circular self-reflection, yet how much of this deliberation is actually necessary has never been measured at scale or explained from first principles. This paper closes both gaps.
We formalise reasoning redundancy directly in terms of the reasoning model itself: the redundancy of a correct trace is the largest fraction of its trailing segmented steps that can be truncated while $\pi$, forced to terminate thinking and emit a final answer, still produces the correct answer. A large-scale quantification across four frontier reasoning models and two mathematical benchmarks shows that step-level redundancy is consistently high -- between 61% and 93% across the 8 (model, benchmark) conditions we study, with the median critical prefix equal to a single segmented step in six of the eight conditions -- that the finding is robust to the choice of judge family, and that although $\rho$ decreases with problem difficulty on MATH-500, all four models remain substantially redundant ($\rho \in [46\%, 85\%]$) even on the hardest Level-5 problems.
We then prove that this redundancy is a structural consequence of length-agnostic outcome rewards, not a model-specific artefact: under any such reward, no finite expected stopping time is optimal. The result holds regardless of RL algorithm, base model, data distribution, or whether the policy is obtained via RL or distillation; over-thinking is therefore not a bug to be patched in individual models but a structural property of how current reasoning models are trained. Code: https://github.com/zhiyuanZhai20/how-much-thinking-is-enough
