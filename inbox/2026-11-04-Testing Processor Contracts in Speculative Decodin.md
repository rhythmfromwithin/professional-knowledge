---
interest: medium
link: https://arxiv.org/abs/2611.04042
next_step: skim
priority: low
slack_ts: '1793945319.585979'
source: cs.SE - Software Engineering
status: unread
title: Testing Processor Contracts in Speculative Decoding Engines
---
# Testing Processor Contracts in Speculative Decoding Engines
> 原文: [https://arxiv.org/abs/2611.04042](https://arxiv.org/abs/2611.04042)

arXiv:2611.04042v1 Announce Type: new
Abstract: Speculative sampling can accelerate decoding without changing the target distribution. Its standard guarantee assumes that logits processors, which enforce constraints or modify token scores, receive the appropriate token prefix and state at each verification position. We formalize this processor-prefix contract and present BADC (branch-aware differential conformance testing). BADC combines enumerated references on tiny random models, checks of processor inputs and state, and simultaneous confidence bounds on output-event probabilities. Preregistered, source-informed experiments on selected Transformers and llama-cpp-python releases confirm two causes: processors read unverified drafts or advance state without rollback. For one pilot-selected prompt on a trained checkpoint, fresh samples give a 60.26-percentage-point lower bound on the difference in the probability of a predefined first-token event between ordinary and prompt-lookup decoding, with nominal simultaneous 95% coverage under within-arm i.i.d. sampling. Controlled comparisons establish no cause-recovery advantage of directed selection over random selection, while permutation testing detects each tested family at least as often as BADC. These findings connect processor-interface failures to observable decoding differences without establishing diagnostic superiority or workload prevalence.
