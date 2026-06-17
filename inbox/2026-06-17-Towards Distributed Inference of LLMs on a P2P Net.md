---
interest: medium
link: https://arxiv.org/abs/2606.17059
next_step: skim
priority: medium
slack_ts: '1781672202.090569'
source: cs.DC - Distributed Computing
status: unread
title: Towards Distributed Inference of LLMs on a P2P Network
---
# Towards Distributed Inference of LLMs on a P2P Network
> 原文: [https://arxiv.org/abs/2606.17059](https://arxiv.org/abs/2606.17059)

arXiv:2606.17059v1 Announce Type: new
Abstract: Prefix caching can reduce LLM inference latency by reusing KV caches across requests with shared prompts, but cluster-scale reuse is challenging because caches are partitioned across nodes. We propose a decentralized, prefix-cache-aware routing scheme for peer-to-peer LLM serving. Each node maintains a local radix tree of its own cached prefixes and asynchronously refreshed estimates of peer caches using periodic anti-entropy. Requests are routed to the node with the longest estimated prefix match, without centralized coordination or KV-cache transfer. Stale metadata only causes cache misses, not incorrect outputs, making weak consistency sufficient for correctness. Evaluation on simulated MMLU workloads show that decentralized routing improves latency under low communication delay and skewed prefix distributions, while high network latency and affinity-induced hotspots limit its benefits.
