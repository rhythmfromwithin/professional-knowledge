---
interest: medium
link: https://arxiv.org/abs/2611.17398
next_step: skim
priority: high
slack_ts: '1794808695.463459'
source: cs.LG - Machine Learning
status: unread
title: 'Alignment with Reflect-Reasoning: Learning How To Follow Principles'
---
# Alignment with Reflect-Reasoning: Learning How To Follow Principles
> 原文: [https://arxiv.org/abs/2611.17398](https://arxiv.org/abs/2611.17398)

arXiv:2611.17398v1 Announce Type: new
Abstract: The appropriate governing norms and principles for the alignment of Large Language Models (LLMs) often depend on cultural context and deployment application. However, most alignment techniques focus on training models to conform to human preferences or constitutional principles specified at training time and subsequently fixed. In practice, many deployers rely on system prompting to implement contextual norms and guardrails at inference time. Prior work has shown that post-generation reflective reasoning with critique and revision can improve conformance compared to simple system prompting, but such methods are limited to the reasoning abilities inherent in the trained model. We introduce Reflect-Reasoning, a training method that teaches models how to reason about alignment to principles, rather than simply which principles to follow. Across five models, Reflect-Reasoning consistently outperforms both system prompting and explicit prompting strategies for in-context reflective reasoning. These improvements extend and generalize to entirely out-of-distribution domains of medical and financial principles. We additionally demonstrate that Reflect-Reasoning reduces the occurrence of rare but serious principle violations. Finally, we show that Reflect-Reasoning does not erode the safety engineering of a model and is robust against jailbreaking attempts using adversarial constitutions. Overall, our results demonstrate that Reflect-Reasoning is a scalable method for training constitutional alignment as a generalizable reasoning capability, enabling models to adapt to novel principles and produce transparent reasoning traces without additional fine-tuning.
