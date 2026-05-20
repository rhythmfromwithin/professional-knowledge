---
title: "ReacTOD: Bounded Neuro-Symbolic Agentic NLU for Zero-Shot Dialogue State Tracking"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.19077
priority: high
status: unread
interest: medium
next_step: skim
---
# ReacTOD: Bounded Neuro-Symbolic Agentic NLU for Zero-Shot Dialogue State Tracking
> 原文: [https://arxiv.org/abs/2605.19077](https://arxiv.org/abs/2605.19077)

arXiv:2605.19077v1 Announce Type: new
Abstract: Task-oriented dialogue systems -- handling transactions, reservations, and service requests -- require predictable behavior, yet the moderately-sized LLMs needed for practical latency are prone to hallucination and format errors that cascade into incorrect actions (e.g., a hotel booked for the wrong date). We propose ReacTOD, a bounded neuro-symbolic architecture that reformulates NLU as discrete tool calls within a self-correcting ReAct loop governed by deterministic validation. A bounded ReAct loop enables iterative self-correction, improving accuracy by up to 9.3 percentage points over single-pass inference on MultiWOZ. A symbolic validator enforces action compliance, schema conformance, and coreference consistency on every dialogue state update, achieving a 93.1% self-correction rate on intercepted errors and producing structured execution traces. Incremental state prediction and on-demand history retrieval keep prompts compact, empirically improving instruction adherence in parameter-constrained models. On MultiWOZ 2.1, ReacTOD achieves a new zero-shot state-of-the-art: gpt-oss-20B reaches 52.71% joint goal accuracy, surpassing the previous best by 14 percentage points, while Qwen3-8B achieves 47.34% with only 8B parameters. On the Schema-Guided Dialogue (SGD) benchmark, ReacTOD with Claude-Opus-4.6 achieves 80.68% JGA under fully end-to-end evaluation with predicted domains, and Qwen3-32B reaches 64.09% -- demonstrating cross-benchmark generalization without task-specific training data.
