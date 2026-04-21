---
interest: medium
link: https://arxiv.org/abs/2604.15368
next_step: skim
priority: low
slack_ts: '1776742307.141079'
source: cs.CR - Cryptography and Security
status: unread
title: 'LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging
  Agents'
---
# LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents
> 原文: [https://arxiv.org/abs/2604.15368](https://arxiv.org/abs/2604.15368)

arXiv:2604.15368v1 Announce Type: new
Abstract: LLM debugging agents that consume cloud logs and execute remediation commands are vulnerable to indirect prompt injection through log content. We present LogJack, a benchmark of 42 payloads across 5 cloud log categories, and evaluate 8 foundation models under 3 prompt conditions with 5 independent trials each (n = 160 per model per condition on 32 attack payloads). Under the active condition, verbatim command execution rates range from 0% (Claude Sonnet 4.6) to 86.2% (Llama 3.3 70B). Passive instructions ("do not execute fixes") reduce most models to 0% but Llama still executes at 30.0%. Remote code execution via curl | bash succeeds on 6 of 8 models. Guardrails from AWS, GCP, and Azure largely fail to detect log-embedded injections-Azure Prompt Shield detected only the most obvious payload (1/32), while GCP Model Armor detected none-though they detect identical payloads in isolation. We also observe a novel "sanitize and execute" behavior where a model detects and removes an obvious malicious component but still executes the remaining injected command. Benchmark and harness available at github.com/HarshShah1997/logjack.
