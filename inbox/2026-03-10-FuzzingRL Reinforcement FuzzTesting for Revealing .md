---
interest: medium
link: https://arxiv.org/abs/2603.06600
next_step: skim
priority: high
slack_ts: '1773132503.414969'
source: cs.LG - Machine Learning
status: unread
title: 'FuzzingRL: Reinforcement Fuzz-Testing for Revealing VLM Failures'
---
# FuzzingRL: Reinforcement Fuzz-Testing for Revealing VLM Failures
> 原文: [https://arxiv.org/abs/2603.06600](https://arxiv.org/abs/2603.06600)

arXiv:2603.06600v1 Announce Type: new
Abstract: Vision Language Models (VLMs) are prone to errors, and identifying where these errors occur is critical for ensuring the reliability and safety of AI systems. In this paper, we propose an approach that automatically generates questions designed to deliberately induce incorrect responses from VLMs, thereby revealing their vulnerabilities. The core of this approach lies in fuzz testing and reinforcement finetuning: we transform a single input query into a large set of diverse variants through vision and language fuzzing. Based on the fuzzing outcomes, the question generator is further instructed by adversarial reinforcement fine-tuning to produce increasingly challenging queries that trigger model failures. With this approach, we can consistently drive down a target VLM's answer accuracy -- for example, the accuracy of Qwen2.5-VL-32B on our generated questions drops from 86.58\% to 65.53\% in four RL iterations. Moreover, a fuzzing policy trained against a single target VLM transfers to multiple other VLMs, producing challenging queries that degrade their performance as well.
