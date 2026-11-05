---
interest: medium
link: https://arxiv.org/abs/2611.05991
next_step: skim
priority: medium
slack_ts: '1793859293.339799'
source: cs.DC - Distributed Computing
status: unread
title: A Controlled Experimental Evaluation of Configuration and Cache Architecture
  in LLM Serving Engines
---
# A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines
> 原文: [https://arxiv.org/abs/2611.05991](https://arxiv.org/abs/2611.05991)

arXiv:2611.05991v1 Announce Type: new
Abstract: Multi-agent LLM applications repeat most of their prompt tokens across requests, and serving engines reuse the cached state of shared prefixes. vLLM and SGLang reuse it at different granularities, and benchmarks of their default deployments report large performance gaps, usually credited to the cache. Such comparisons rarely control for other configuration differences. One of them, whether a long prompt is prefilled in chunks, is set by each engine's defaults from the hardware and the release, and it confounds the comparison. We built a reproducible testbed on Kubernetes and a seeded multi-agent workload generator, and compared the two engines under vendor defaults and with chunked prefill matched. SGLang's configuration is the same in both arms, which makes it an internal control across independently provisioned deployments. Under defaults, vLLM's median time to first token is up to 64x SGLang's. Matching one setting removes 78% of the capacity gap where that gap is largest and 30 to 67% of the latency gap. Near saturation the remaining latency gap reflects queue growth. A fluid queue model driven only by a 4.4% throughput shortfall reproduces it, and shows that such a gap scales with the length of the benchmark run. What survives matching is a tail-latency advantage of 2.4 to 6.4x at equal throughput, consistent with cache-aware ordering of waiting requests. We derive six recommendations for comparing serving engines.
