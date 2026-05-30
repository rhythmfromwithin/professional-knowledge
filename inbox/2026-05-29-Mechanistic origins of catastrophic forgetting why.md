---
interest: medium
link: https://arxiv.org/abs/2605.28860
next_step: skim
priority: high
slack_ts: '1780113880.054639'
source: cs.LG - Machine Learning
status: unread
title: 'Mechanistic origins of catastrophic forgetting: why RL preserves circuits
  better than SFT?'
---
# Mechanistic origins of catastrophic forgetting: why RL preserves circuits better than SFT?
> 原文: [https://arxiv.org/abs/2605.28860](https://arxiv.org/abs/2605.28860)

arXiv:2605.28860v1 Announce Type: new
Abstract: Fine-tuning large language models (LLMs) frequently induces catastrophic forgetting of prior capabilities. Recent work has shown that reinforcement learning (RL) retains prior capabilities more effectively than supervised fine-tuning (SFT), attributing this to policy-gradient updates remaining closer to the base policy \cite{shenfeld2025rl}. We extend this behavioral account to the mechanistic level and ask whether RL's advantage is mirrored by stronger preservation of internal computational circuits. We introduce differential circuit vulnerability, a head-level measure of how much a circuit degrades under fine-tuning, and use it to compare RL and SFT on Qwen2.5-3B-Instruct adapted to scientific question-answering. We find a clear mechanistic trade-off: SFT adapts more rapidly to the target task but produces substantially greater circuit disruption and forgetting of prior capabilities, whereas RL preserves a larger fraction of the base circuit at the cost of slower task adaptation. These findings suggest that circuit preservation may help explain why RL is more robust to catastrophic forgetting. We released our code here: https://github.com/rl-sft-circuit-research/differential-circuit-vulnerability.
