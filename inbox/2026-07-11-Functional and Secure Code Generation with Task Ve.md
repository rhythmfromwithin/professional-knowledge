---
interest: medium
link: https://arxiv.org/abs/2607.07881
next_step: skim
priority: low
slack_ts: '1783740364.886859'
source: cs.SE - Software Engineering
status: unread
title: Functional and Secure Code Generation with Task Vectors
---
# Functional and Secure Code Generation with Task Vectors
> 原文: [https://arxiv.org/abs/2607.07881](https://arxiv.org/abs/2607.07881)

arXiv:2607.07881v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly used for code generation, but they struggle to generate functional code free of security vulnerabilities. Prior work to improve the secure code generation abilities of such coding LLMs has largely focused on evaluating code functionality and security separately using different datasets, or focused on finding vulnerabilities post-generation. At the same time, the text-generation domain has seen significant work on alignment techniques, where models are tuned such that their outputs exhibit certain qualities (e.g., helpfulness, harmlessness). Of particular interest is task-vector arithmetic, where linear operations on LLM weights can be used to arbitrarily enhance alignment while incurring only minimal computational overhead. We develop a novel method, SecVecCoder, leveraging task vectors to produce trustworthy code that is simultaneously functional and secure without the need for post-generation adjustment. Across six coding LLMs from three families on the CodeGuard+ benchmark, SecVecCoder improves the rate of trustworthy code completions by 2.1-36.0 percentage points over the base model, with improvements on unseen CWE types reaching up to 39.1 percentage points. Since the effectiveness of the coding LLM relies only on changing the model weights, SecVecCoder requires no method-specific decoding and hence achieves a decoding latency within 0.6% of the base model's, on average.
