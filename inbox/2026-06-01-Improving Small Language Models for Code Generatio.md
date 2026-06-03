---
interest: medium
link: https://arxiv.org/abs/2605.30478
next_step: skim
priority: low
slack_ts: '1780462689.612439'
source: cs.SE - Software Engineering
status: unread
title: Improving Small Language Models for Code Generation with Reinforcement Learning
  from Verification Feedback
---
# Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback
> 原文: [https://arxiv.org/abs/2605.30478](https://arxiv.org/abs/2605.30478)

arXiv:2605.30478v1 Announce Type: new
Abstract: Reinforcement learning with verifiable rewards (RLVR) trains language models using programmatically checkable signals such as unit-test outcomes, enabling direct optimization for functional correctness in code generation. We conduct an empirical study of RLVR for Python code generation on the MBPP benchmark using two small models (Qwen3-0.6B and Llama3.2-1B) with LoRA fine-tuning. Across multiple reward formulations such as: unit-test-only rewards, static-analysis-only shaping via the Ruff linter, and a combined reward, we compare group-based policy optimization variants (GRPO and GSPO) and evaluate both functional correctness and behavioral diagnostics. In our experimental setting, RLVR improves pass@1 on MBPP test by up to 13 percentage points under proposed combined reward configuration. However, we find that reward shaping can induce systematic behavioral shifts: using only static-analysis penalties may bias the policy toward shorter completions that reduce lint errors without reliably improving functional correctness. In contrast, combined rewards mitigate this degeneration and yield more stable trade-offs between correctness and style constraints. Overall, our results highlight that RLVR effectiveness for code generation is highly sensitive to reward design and optimization granularity, and that diagnostics beyond pass@1, including generation length, Ruff severity profiles, and execution error types are useful for identifying failure modes.
