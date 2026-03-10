---
interest: medium
link: https://arxiv.org/abs/2602.23407
next_step: skim
priority: low
slack_ts: '1773132415.805849'
source: cs.CR - Cryptography and Security
status: unread
title: Learning to Generate Secure Code via Token-Level Rewards
---
# Learning to Generate Secure Code via Token-Level Rewards
> 原文: [https://arxiv.org/abs/2602.23407](https://arxiv.org/abs/2602.23407)

arXiv:2602.23407v1 Announce Type: new
Abstract: Large language models (LLMs) have demonstrated strong capabilities in code generation, yet they remain prone to producing security vulnerabilities. Existing approaches commonly suffer from two key limitations: the scarcity of high-quality security data and coarse-grained reinforcement learning reward signals. To address these challenges, we propose Vul2Safe, a new secure code generation framework that leverages LLM self-reflection to construct high-confidence repair pairs from real-world vulnerabilities, and further generates diverse implicit prompts to build the PrimeVul+ dataset. Meanwhile, we introduce SRCode, a novel training framework that pioneers the use of token-level rewards in reinforcement learning for code security, which enables the model to continuously attend to and reinforce critical fine-grained security patterns during training. Compared with traditional instance-level reward schemes, our approach allows for more precise optimization of local security implementations. Extensive experiments show that PrimeVul+ and SRCode substantially reduce security vulnerabilities in generated code while improving overall code quality across multiple benchmarks.
