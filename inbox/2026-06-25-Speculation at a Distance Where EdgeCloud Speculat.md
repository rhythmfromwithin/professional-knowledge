---
interest: medium
link: https://arxiv.org/abs/2606.25091
next_step: skim
priority: medium
slack_ts: '1782447542.171729'
source: cs.DC - Distributed Computing
status: unread
title: 'Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually
  Pays Off'
---
# Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off
> 原文: [https://arxiv.org/abs/2606.25091](https://arxiv.org/abs/2606.25091)

arXiv:2606.25091v1 Announce Type: new
Abstract: Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located. This has motivated a distributed variant (DSD) that places the draft model on an edge device while the target stays in the cloud. We show with closed-form inequalities that DSD's per-request latency benefit is limited under WAN edge-cloud communication. If the server can host both models, co-located SD has lower latency and communication than synchronous DSD, with the same per-output FLOPs and model-weight memory. Pipelining can make DSD competitive with co-located SD only in low-RTT regimes where the round trip is shorter than the edge drafting time window; at WAN RTTs, the cloud round trip remains too large for pipelined DSD to beat co-located SD. Against cloud autoregressive decoding, DSD can reduce latency only inside a bounded window given the target-model speed, acceptance rate, and RTT. DSD is also infeasible against closed-source APIs without a verifier-only interface. The main case for DSD appears in multi-tenant capacity. Under cross-client overlap, offloading draft compute lets a saturated cloud server sustain $(1 + \gamma\,t\_d/t\_v)$ times more concurrent clients at the same per-client rate, where $\gamma$ is the speculation length and $t\_d, t\_v$ are the per-step draft and verification times. DSD should therefore be evaluated primarily by multi-tenant capacity and server throughput, not only by single-request latency.
