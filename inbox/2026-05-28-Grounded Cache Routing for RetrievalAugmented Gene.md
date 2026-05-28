---
interest: medium
link: https://arxiv.org/abs/2605.27494
next_step: skim
priority: low
slack_ts: '1779941833.275519'
source: cs.CR - Cryptography and Security
status: unread
title: 'Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe
  to Reuse an Answer?'
---
# Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer?
> 原文: [https://arxiv.org/abs/2605.27494](https://arxiv.org/abs/2605.27494)

arXiv:2605.27494v1 Announce Type: new
Abstract: Modern retrieval-augmented generation(RAG) deployments increasingly rely on caching to reduce token cost and time-to-first-token(TTFT). Prefix-level KV reuse is now standard in serving stacks such as vLLM, and chunk-level and position-independent reuse have been pushed further by recent systems(RAGCache, TurboRAG, CacheBlend, EPIC, ContextPilot, PCR, LMCache). Output-level semantic answer caches, by contrast, remain fragile: similar prompts can map to different correct answers, retrieved evidence drifts as the corpus is updated, and adversarial collision attacks have been shown to hijack cached responses. We argue that the right framing for cached answer reuse is not how to reuse faster but when reuse is safe. We propose GroundedCache, an evidence-validated cache router that admits a cached answer only when 4 cheap gates simultaneously hold: query similarity, retrieved-evidence overlap, source-version validity, and lexical (or judge-based) support of the cached answer by the freshly retrieved evidence. We build a six-regime workload that stress-tests cache safety rather than only hit rate, and introduce an operator-facing metric, the unsafe-served rate (USR), fraction of all queries that received a wrong cached answer. Across 2 datasets and 12,000 real-LLM generations(Qwen2.5-7B-Instruct on vLLM with Automatic Prefix Caching), GroundedCache drives USR to 0.0% on every HotpotQA regime(vs. 15-35% under naive caching) and to 1.5% on mtRAG document drift(vs. 51.5%), a 34x reduction on the design-point adversarial regime and 3-10x reductions across the other mtRAG regimes, while end-to-end p50 latency stays within 1.04-1.07x of a no-cache RAG baseline. A per-gate ablation isolates the lexical support gate as the load-bearing safety mechanism on both datasets, with the remaining gates providing defense-in-depth at near-zero cost. We release the implementation, workload, and evaluation harness.
