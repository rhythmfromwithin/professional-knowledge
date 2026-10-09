---
interest: medium
link: https://arxiv.org/abs/2610.06861
next_step: skim
priority: high
slack_ts: '1791524738.353349'
source: cs.LG - Machine Learning
status: unread
title: When Does External Guidance Help LLM Reasoning? A Bias-Variance Theory of Guidance-Augmented
  GRPO
---
# When Does External Guidance Help LLM Reasoning? A Bias-Variance Theory of Guidance-Augmented GRPO
> 原文: [https://arxiv.org/abs/2610.06861](https://arxiv.org/abs/2610.06861)

arXiv:2610.06861v1 Announce Type: new
Abstract: Reinforcement learning with verifiable rewards (RLVR) has become the dominant paradigm for eliciting multi-step reasoning in large language models, and a recent wave of methods (LUFFY, ExPO, PAPO, TAPO) further augments RL with \emph{external guidance} - expert traces, self-explanations, or retrieved thought patterns. Although each method reports empirical gains, none provides convergence rates, bias bounds, or an optimal weighting rule for the guidance signal. We close this gap with \emph{Guidance-Augmented GRPO} (GA-GRPO), a unified theoretical framework that casts external guidance as a stochastic guidance operator G re-writing the question distribution, and analyses the resulting policy-gradient estimator as a biased on-policy estimator whose bias is bounded by the total-variation guidance divergence delta\\_G between the guidance-augmented sampling distribution and the policy's own distribution. The framework subsumes vanilla GRPO, LUFFY, ExPO, PAPO, and TAPO as special cases obtained by particular choices of G. Under smoothness and bounded-divergence assumptions we prove that GA-GRPO converges at rate O(1/sqrt(T)) to an O(delta sqrt(T))-neighbourhood of the GRPO stationary point, derive the closed-form MSE-optimal guidance weight lambda-star(T, delta, sigma\\_0 squared) = sigma\\_0 squared / (sigma\\_0 squared + R\\_max squared delta squared T), and prove a matching minimax lower bound showing the Omega(delta squared T) bias term is unavoidable. Experiments on Qwen2.5-Math-7B-Base across nine math and OOD benchmarks confirm that optimal-weight GA-GRPO matches or surpasses TAPO, LUFFY, ExPO, and vanilla GRPO while requiring 31\% fewer GPU-hours, and eight analysis experiments validate each theoretical prediction.
