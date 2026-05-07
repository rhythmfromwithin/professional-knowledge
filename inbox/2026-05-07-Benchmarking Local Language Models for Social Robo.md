---
title: "Benchmarking Local Language Models for Social Robots using Edge Devices"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.03111
priority: medium
status: unread
interest: medium
next_step: skim
---
# Benchmarking Local Language Models for Social Robots using Edge Devices
> 原文: [https://arxiv.org/abs/2605.03111](https://arxiv.org/abs/2605.03111)

arXiv:2605.03111v1 Announce Type: new
Abstract: Social-educational robots designed for socially interactive pedagogical support, such as the Robot Study Companion (RSC), rely on responsive, privacy-preserving interaction despite severely limited compute. However, there is a gap in systematic benchmarking of language models for edge computing in pedagogical applications. This paper benchmarks 25 open-source language models for local deployment on edge hardware. We evaluate each model across three dimensions: inference efficiency (tokens per second, energy consumption), general knowledge (a six-category MMLU subset), and teaching effectiveness (LLM-rated pedagogical quality), validated against five independent human raters using the Raspberry Pi(RPi)4 as the primary platform, with additional comparisons on the RPi5 and a laptop GPU.
Results reveal pronounced trade-offs: throughput and energy efficiency vary by over an order of magnitude across models, MMLU accuracy ranges from near-random to 57.2%, and teaching effectiveness does not correlate monotonically with either metric. Among the evaluated models, Granite4 Tiny Hybrid (7B) achieves a strong overall balance, reaching 2.5 tokens per second, 0.90 tokens per joule, and 54.6% MMLU accuracy; high MMLU accuracy does not appear necessary for strong teaching scores. Human validation on four representative models preserved the automated rank ordering (Pearson r = 0.967, n = 4). Based on these findings, we propose a three-tier local inference architecture for the RSC that balances responsiveness and accuracy on resource-constrained hardware.
