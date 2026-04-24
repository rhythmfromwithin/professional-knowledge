---
interest: medium
link: https://arxiv.org/abs/2604.18834
next_step: skim
priority: low
slack_ts: '1777001712.660419'
source: cs.SE - Software Engineering
status: unread
title: Structural Verification for Reliable EDA Code Generation without Tool-in-the-Loop
  Debugging
---
# Structural Verification for Reliable EDA Code Generation without Tool-in-the-Loop Debugging
> 原文: [https://arxiv.org/abs/2604.18834](https://arxiv.org/abs/2604.18834)

arXiv:2604.18834v1 Announce Type: new
Abstract: Large language models (LLMs) have enabled natural-language-driven automation of electronic design automation (EDA) workflows, but reliable execution of generated scripts remains a fundamental challenge. In LLM-based EDA tasks, failures arise not from syntax errors but from violations of implicit structural dependencies over design objects, including invalid acquisition paths, missing prerequisites, and incompatible API usage. Existing approaches address these failures through tool-in-the-loop debugging, repeatedly executing and repairing programs using runtime feedback. While effective, this paradigm couples correctness to repeated tool invocation, leading to high latency and poor scalability in multi-step settings. We propose to eliminate tool-in-the-loop debugging by enforcing structural correctness prior to execution. Each task is represented as a structural dependency graph that serves as an explicit execution contract, and a verifier-guided synthesis framework enforces this contract through graph-conditioned retrieval, constrained generation, and staged pre-execution verification with diagnosis-driven repair. On single-step tasks, our method improves pass rate from 73.0% (LLM+RAG) and 76.0% (tool-in-loop) to 82.5%, while requiring exactly one tool call per task and reducing total tool calls by more than 2x. On multi-step tasks, pass rate improves from 30.0% to 70.0%, and further to 84.0% with trajectory-level reflection. Uncertainty-aware filtering further reduces verifier false positives from 20.0% to 6.7% and improves precision from 80.0% to 93.3%. These results show that enforcing structural consistency prior to execution decouples correctness from tool interaction, improving both reliability and efficiency in long-horizon EDA code generation.
