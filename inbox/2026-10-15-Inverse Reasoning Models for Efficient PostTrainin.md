---
interest: medium
link: https://arxiv.org/abs/2610.18878
next_step: skim
priority: high
slack_ts: '1792123820.623259'
source: cs.LG - Machine Learning
status: unread
title: Inverse Reasoning Models for Efficient Post-Training and Verification from
  Answer-Only Data
---
# Inverse Reasoning Models for Efficient Post-Training and Verification from Answer-Only Data
> 原文: [https://arxiv.org/abs/2610.18878](https://arxiv.org/abs/2610.18878)

arXiv:2610.18878v1 Announce Type: new
Abstract: Post-training reasoning LLMs often requires making a tradeoff between costly supervision and compute inefficiency: supervised finetuning typically requires reasoning traces, which is data inefficient since in many applications one only has prompt-answer tuples and lacks the groundtruth chain-of-thought (CoT) sequence. On the other hand, reinforcement learning (with verifiable rewards, for example) can operate without CoT data but it is much more compute-inefficient since it requires multiple autoregressive completions per optimization step, none of which are guaranteed to give a non-zero policy gradient. In this work we explore a middleground, a self-distillation technique that uses answer-only data, treating CoT as latent variables. This relies on training a partner ``inverse reasoning LLM" that generates the original's reasoning traces conditioned on the answer. The inverse model is trained once and reused across incoming batches of answer-only data, with all generation happening offline and up front, making the approach particularly suited to continual post-training. Using Qwen3-0.6B on the Countdown and GSM8K tasks, we show that after GRPO training has saturated, a single offline distillation round from the inverse model roughly doubles pass@1 on hard prompts and, on Countdown, outperforms rejection-sampling self-distillation on every hard-tail metric at every mix ratio (with smaller gains on GSM8K); rejection sampling by construction has no signal on problems the model never solves on its own. Continued GRPO on the fresh data retains an edge at hard pass@1 but trails distillation at pass@8 and pass@32 while regenerating rollouts at every step. As an added bonus we see that the inverse model has a second application as an accurate verifier of correctness. When used for best-of-$n$ selection at test time, it raises selection accuracy on Countdown from 0.753 (majority voting) to 0.969.
