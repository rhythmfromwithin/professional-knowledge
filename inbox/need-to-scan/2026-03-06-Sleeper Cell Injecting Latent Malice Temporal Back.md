---
interest: medium
link: https://arxiv.org/abs/2603.03371
next_step: skim
priority: low
slack_ts: '1773196786.578389'
source: cs.CR - Cryptography and Security
status: unread
title: 'Sleeper Cell: Injecting Latent Malice Temporal Backdoors into Tool-Using LLMs'
---
# Sleeper Cell: Injecting Latent Malice Temporal Backdoors into Tool-Using LLMs
> 原文: [https://arxiv.org/abs/2603.03371](https://arxiv.org/abs/2603.03371)

arXiv:2603.03371v1 Announce Type: new
Abstract: The proliferation of open-weight Large Language Models (LLMs) has democratized agentic AI, yet fine-tuned weights are frequently shared and adopted with limited scrutiny beyond leaderboard performance. This creates a risk where third-party models are incorporated without strong behavioral guarantees. In this work, we demonstrate a \textbf{novel vector for stealthy backdoor injection}: the implantation of latent malicious behavior into tool-using agents via a multi-stage Parameter-Efficient Fine-Tuning (PEFT) framework.
Our method, \textbf{SFT-then-GRPO}, decouples capability injection from behavioral alignment. First, we use SFT with LoRA to implant a "sleeper agent" capability. Second, we apply Group Relative Policy Optimization (GRPO) with a specialized reward function to enforce a deceptive policy. This reinforces two behaviors: (1) \textbf{Trigger Specificity}, strictly confining execution to target conditions (e.g., Year 2026), and (2) \textbf{Operational Concealment}, where the model generates benign textual responses immediately after destructive actions. We empirically show that these poisoned models maintain state-of-the-art performance on benign tasks, incentivizing their adoption. Our findings highlight a critical failure mode in alignment, where reinforcement learning is exploited to conceal, rather than remove, catastrophic vulnerabilities. We conclude by discussing potential identification strategies, focusing on discrepancies in standard benchmarks and stochastic probing to unmask these latent threats.
