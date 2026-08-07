---
interest: medium
link: https://arxiv.org/abs/2608.02613
next_step: skim
priority: high
slack_ts: '1786072107.390939'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants
  at Scale'
---
# MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale
> 原文: [https://arxiv.org/abs/2608.02613](https://arxiv.org/abs/2608.02613)

arXiv:2608.02613v1 Announce Type: new
Abstract: Edge-deployed personal memory assistants must handle private interpersonal conversations on-device with open-weight models. Yet, existing memory benchmarks often under-test the combination of activity-dense interaction, ego-centric perspective, and coherent multi-session worlds. MemArena fills these gaps with a single-world conversational benchmark built with its MASim agent simulator, for 50 agents over 15 days (10.3M dialog-text tokens, 24.1K text-only ego-observed tokens/agent/day). With the interaction history, it co-generates ground truth over six recall, reasoning, and trustworthiness evaluation dimensions. We evaluate five open-weight readers with Vanilla context, BM25-RAG, Oracle retrieval, Memobase, and MemSearch as memory backends. Three results stand out: (1) Memory-backend choice matters more for content accuracy: At Qwen3-0.6B, Memobase-to-MemSearch gains +32.5/+19.2 pp, exceeding MemSearch reader scaling (+10.6/+6.8 pp). (2) Permission-aware access fails universally, with Oracle leaking heavily and other backends too timid to disclose. (3) Search latency bites only at very small reader: on a Spark GB10 edge node, memory-search adds a moderate and fixed 87/7/48 ms (BM25-RAG/Memobase/MemSearch) that composes a small part of TTFT for most reader-backend combinations. Code, the MASim simulator, and the MemArena-L benchmark will be released upon acceptance.
