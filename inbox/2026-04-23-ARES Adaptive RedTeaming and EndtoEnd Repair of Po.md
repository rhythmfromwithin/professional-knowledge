---
interest: medium
link: https://arxiv.org/abs/2604.18789
next_step: skim
priority: high
slack_ts: '1776915194.681499'
source: cs.AI - Artificial Intelligence
status: unread
title: 'ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System'
---
# ARES: Adaptive Red-Teaming and End-to-End Repair of Policy-Reward System
> 原文: [https://arxiv.org/abs/2604.18789](https://arxiv.org/abs/2604.18789)

arXiv:2604.18789v1 Announce Type: new
Abstract: Reinforcement Learning from Human Feedback (RLHF) is central to aligning Large Language Models (LLMs), yet it introduces a critical vulnerability: an imperfect Reward Model (RM) can become a single point of failure when it fails to penalize unsafe behaviors. While existing red-teaming approaches primarily target policy-level weaknesses, they overlook what we term systemic weaknesses cases where both the core LLM and the RM fail in tandem.
We present ARES, a framework that systematically discovers and mitigates such dual vulnerabilities. ARES employs a ``Safety Mentor'' that dynamically composes semantically coherent adversarial prompts by combining structured component types (topics, personas, tactics, goals) and generates corresponding malicious and safe responses. This dual-targeting approach exposes weaknesses in both the core LLM and the RM simultaneously. Using the vulnerabilities gained, ARES implements a two-stage repair process: first fine-tuning the RM to better detect harmful content, then leveraging the improved RM to optimize the core model. Experiments across multiple adversarial safety benchmarks demonstrate that ARES substantially enhances safety robustness while preserving model capabilities, establishing a new paradigm for comprehensive RLHF safety alignment.
