---
interest: medium
link: https://arxiv.org/abs/2605.14005
next_step: skim
priority: high
slack_ts: '1778817956.025359'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding'
---
# Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding
> 原文: [https://arxiv.org/abs/2605.14005](https://arxiv.org/abs/2605.14005)

arXiv:2605.14005v1 Announce Type: new
Abstract: Speculative decoding has become a widely adopted technique for accelerating large language model (LLM) inference by drafting multiple candidate tokens and verifying them with a target model in parallel. Its efficiency, however, critically depends on the average accepted length $\tau$, i.e., how many draft tokens survive each verification step. In this work, we identify a new mechanism-level vulnerability in model-based speculative decoding: the drafter is trained to approximate the target model distribution, but this approximation is inevitably imperfect. Such a drafter-target mismatch creates a hidden attack surface where small perturbations can preserve the target model's visible behavior while substantially reducing draft-token acceptability. We propose Mistletoe, a stealthy acceleration-collapse attack against speculative decoding. Mistletoe directly targets the acceptance mechanism of speculative decoding. It jointly optimizes a degradation objective that decreases drafter-target agreement and a semantic-preservation objective that constrains the target model's output distribution. To resolve the conflict between these objectives, we introduce a null-space projection mechanism, where degradation gradients are projected away from the local semantic-preserving direction, suppressing draft acceptance while minimizing semantic drift. Experiments on various speculative decoding systems show that Mistletoe substantially reduces average accepted length $\tau$, collapses speedup, and lowers averaged token throughput, while preserving output quality and perplexity. Our work highlights that speculative decoding introduces a mechanism-level attack surface beyond existing output robustness, calling for more robust designs of LLM acceleration systems.
