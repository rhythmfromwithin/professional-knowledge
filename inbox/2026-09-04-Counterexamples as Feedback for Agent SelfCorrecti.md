---
interest: medium
link: https://arxiv.org/abs/2609.02892
next_step: skim
priority: high
slack_ts: '1788581042.482149'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Counterexamples as Feedback for Agent Self-Correction
---
# Counterexamples as Feedback for Agent Self-Correction
> 原文: [https://arxiv.org/abs/2609.02892](https://arxiv.org/abs/2609.02892)

arXiv:2609.02892v1 Announce Type: new
Abstract: Single-turn code-generation metrics understate a central property of deployed agents: whether they can repair a wrong artifact after receiving concrete feedback. This paper presents A-CEGIS, a lightweight framework that uses counterexamples as feedback for evaluating multi-turn refinement in natural-language-to-regex synthesis. An agent proposes a regex, a deterministic oracle checks it under full-match semantics, and compact false-positive or false-negative witnesses guide the next turn. On 30 NL-RX-Turk tasks, diagnostic counterexample feedback solves 90\% of tasks within a four-turn ablation budget, compared with 17% for zero-shot generation, 27% for generic self-correction, and 23% for error-only feedback. In a full diagnostic run with hardening, all tasks are solved on the hidden set by the final turn, with mean time-to-success of 2.7 turns and robust success of 77% after targeted probing. These results show that A-CEGIS measures how efficiently an agent improves across turns while adding a practical robustness check beyond the original held-out cases.
