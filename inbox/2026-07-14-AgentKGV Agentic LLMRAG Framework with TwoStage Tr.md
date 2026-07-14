---
interest: medium
link: https://arxiv.org/abs/2607.09092
next_step: skim
priority: high
slack_ts: '1783998904.785659'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification
  of Knowledge Graphs'
---
# AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs
> 原文: [https://arxiv.org/abs/2607.09092](https://arxiv.org/abs/2607.09092)

arXiv:2607.09092v1 Announce Type: new
Abstract: Knowledge graphs (KGs) are often automatically constructed from large-scale corpora, but they inevitably contain factual errors due to noisy sources and extraction failures, and verifying them reliably at industrial scale remains a critical challenge. To address this, we propose AgentKGV, the Agentic LLM-RAG framework for KG fact Verification, that integrates dynamic routing and iterative query rewriting, which handles surface-form mismatch in document-level retrieval. To make this framework more accurate and cost-efficient for industrial deployment, we further introduce a two-stage training strategy: turn-level distillation-based SFT that transfers reasoning ability from a large teacher model into a small model for stable query rewriting and reasoning, and trajectory-level GRPO that optimizes the search policy to reduce unnecessary retrieval at scale. On the long-tail-predicate split of the open-domain T-REx benchmark, our framework improves macro-F1 over single-turn RAG by 5.5 \%p, and two-stage training does it further by 9.4 \%p. GRPO also cuts the average number of search calls from 3.24 to 1.63 without lowering accuracy.
