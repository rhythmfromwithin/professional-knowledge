---
title: "Cross-Tokenizer LLM Distillation through a Byte-Level Interface"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2604.07466
priority: high
status: unread
interest: medium
next_step: skim
---
# Cross-Tokenizer LLM Distillation through a Byte-Level Interface
> 原文: [https://arxiv.org/abs/2604.07466](https://arxiv.org/abs/2604.07466)

arXiv:2604.07466v1 Announce Type: new
Abstract: Cross-tokenizer distillation (CTD), the transfer of knowledge from a teacher to a student language model when the two use different tokenizers, remains a largely unsolved problem. Existing approaches rely on heuristic strategies to align mismatched vocabularies, introducing considerable complexity. In this paper, we propose a simple but effective baseline called Byte-Level Distillation (BLD) which enables CTD by operating at a common interface across tokenizers: the byte level. In more detail, we convert the teacher's output distribution to byte-level probabilities, attach a lightweight byte-level decoder head to the student, and distill through this shared byte-level interface. Despite its simplicity, BLD performs competitively with--and on several benchmarks surpasses--significantly more sophisticated CTD methods, across a range of distillation tasks with models from 1B to 8B parameters. Our results suggest that the byte level is a natural common ground for cross-tokenizer knowledge transfer, while also highlighting that consistent improvements across all tasks and benchmarks remain elusive, underscoring that CTD is still an open problem.
