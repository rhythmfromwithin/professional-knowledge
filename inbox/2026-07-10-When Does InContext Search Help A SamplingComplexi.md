---
interest: medium
link: https://arxiv.org/abs/2607.06720
next_step: skim
priority: high
slack_ts: '1783740356.503399'
source: cs.AI - Artificial Intelligence
status: unread
title: When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven
  Reasoning
---
# When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning
> 原文: [https://arxiv.org/abs/2607.06720](https://arxiv.org/abs/2607.06720)

arXiv:2607.06720v1 Announce Type: new
Abstract: Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve high success probability. We show that when reflections reliably localize early mistakes, in-context search can yield exponential improvements over the base model, solving problems with exponentially small zero-shot pass rates using only a polynomial number of sequential attempts, whereas when this property fails, conditioning on past attempts offers no asymptotic benefit over parallel sampling. We further show that these gains are robust and learnable: approximate posterior updates suffice, and cross-entropy training on search rollouts recovers the required behavior with polynomial sample complexity. Finally, we show that under a stagewise abstraction of reinforcement learning with verifiable rewards, the optimal policy extension implements the same posterior reweighting rule. We validate key qualitative predictions of the theory on real large reasoning models.
