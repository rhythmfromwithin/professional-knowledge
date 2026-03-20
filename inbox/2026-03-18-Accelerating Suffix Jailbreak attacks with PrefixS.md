---
interest: medium
link: https://arxiv.org/abs/2603.13420
next_step: skim
priority: low
slack_ts: '1773974669.730509'
source: cs.CR - Cryptography and Security
status: unread
title: Accelerating Suffix Jailbreak attacks with Prefix-Shared KV-cache
---
# Accelerating Suffix Jailbreak attacks with Prefix-Shared KV-cache
> 原文: [https://arxiv.org/abs/2603.13420](https://arxiv.org/abs/2603.13420)

arXiv:2603.13420v1 Announce Type: new
Abstract: Suffix jailbreak attacks serve as a systematic method for red-teaming Large Language Models (LLMs) but suffer from prohibitive computational costs, as a large number of candidate suffixes need to be evaluated before identifying a jailbreak suffix. This paper presents Prefix-Shared KV Cache (PSKV), a plug-and-play inference optimization technique tailored for jailbreak suffix generation. Our method is motivated by a key observation that when performing suffix jailbreaking, while a large number of candidate prompts need to be evaluated, they share the same targeted harmful instruction as the prefix. Therefore, instead of performing redundant inference on the duplicated prefix, PSKV maintains a single KV cache for this prefix and shares it with every candidate prompt, enabling the parallel inference of diverse suffixes with minimal memory overhead. This design enables more aggressive batching strategies that would otherwise be limited by memory constraints. Extensive experiments on six widely used suffix attacks across five widely deployed LLMs demonstrate that PSKV reduces inference time by 40\% and peak memory usage by 50\%, while maintaining the original Attack Success Rate (ASR). The code has been submitted and will be released publicly.
