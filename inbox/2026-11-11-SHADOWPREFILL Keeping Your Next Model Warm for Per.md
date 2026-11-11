---
title: "SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.13176
priority: medium
status: unread
interest: medium
next_step: skim
---
# SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving
> 原文: [https://arxiv.org/abs/2611.13176](https://arxiv.org/abs/2611.13176)

arXiv:2611.13176v1 Announce Type: new
Abstract: Per-step model routers send each LLM call of an agent to the cost-optimal model dynamically within each session. However, every model switch discards prefix-cache reuse: KV caches are per model, so the new model must prefill the relevant context before it emits a token. Across representative agentic workloads, including a production coding-agent trace with a mean context of 63K tokens, the prefix hit rate falls from 80-89% on same model calls to 44-65% after a switch, and a switch call takes 1.5-3.2x as long. We present SHADOWPREFILL, which prefills the session's context on the model the router has not chosen, in capacity that instances serving normal traffic leave idle, so the next switch finds its prefix cached. SHADOWPREFILL harvests the per-iteration SLO slack of requests in flight, protects routed calls, spills shadow KV to host memory, and falls back to a cold switch whenever the shadow is incomplete. With LLMRouter routing 24 model pairs over five agentic benchmark suites, SHADOWPREFILL cuts switch-call latency by 8.5-21.4%, LLM-call latency by 3.7-17.7%, and routed token cost by 22.5-46.1%, while normal traffic keeps its SLO and energy per request rises by 0.4%.
