---
title: "RubricReviewer: From Direct Critique to Objective and Comprehensive Rubric-Driven Peer Review"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.00005
priority: high
status: unread
interest: medium
next_step: skim
---
# RubricReviewer: From Direct Critique to Objective and Comprehensive Rubric-Driven Peer Review
> 原文: [https://arxiv.org/abs/2608.00005](https://arxiv.org/abs/2608.00005)

arXiv:2608.00005v1 Announce Type: new
Abstract: Peer review at major venues is under unprecedented submission pressure, motivating the use of large language models (LLMs) as review assistants. Existing LLM-based reviewers, however, face two structural limitations. First, they map manuscripts directly to reviews, leaving the underlying rubric implicit and entangling its derivation with the judgement. Second, the prevailing paradigms each capture only half of a good review: training-free agents gather broad evidence but produce undirected critiques, while training-based reviewers inherit human discriminative judgement together with its noise and uneven coverage. We introduce RubricReviewer, a fully rubric-driven framework that addresses both limitations. It makes rubric generation an explicit intermediate step, so that both review generation and the final assessment are conditioned on paper-adaptive rubrics. It further combines a training-free agent (Scout) that gathers external evidence with a human-aligned trained model (Aligner) that consumes this evidence, fusing the strengths of both supervision sources. Experiments on real-world submissions show that RubricReviewer produces reviews that are markedly more comprehensive and more discriminative than prior systems, and exhibits the strongest robustness against adversarial prompt-injection attacks. Ablation studies further confirm the necessity of each component.
