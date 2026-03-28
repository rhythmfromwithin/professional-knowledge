---
interest: medium
link: https://arxiv.org/abs/2603.23508
next_step: skim
priority: high
slack_ts: '1774666210.931059'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Fast and Faithful: Real-Time Verification for Long-Document Retrieval-Augmented
  Generation Systems'
---
# Fast and Faithful: Real-Time Verification for Long-Document Retrieval-Augmented Generation Systems
> 原文: [https://arxiv.org/abs/2603.23508](https://arxiv.org/abs/2603.23508)

arXiv:2603.23508v1 Announce Type: new
Abstract: Retrieval-augmented generation (RAG) is increasingly deployed in enterprise search and document-centric assistants, where responses must be grounded in long and complex source materials. In practice, verifying that generated answers faithfully reflect retrieved documents is difficult: large language models can check long contexts but are too slow and costly for interactive services, while lightweight classifiers operate within strict context limits and frequently miss evidence outside truncated passages. We present the design of a real-time verification component integrated into a production RAG pipeline that enables full-document grounding under latency constraints. The system processes documents up to 32K tokens and employs adaptive inference strategies to balance response time and verification coverage across workloads. We describe the architectural decisions, operational trade-offs, and evaluation methodology used to deploy the verifier, and show that full-context verification substantially improves detection of unsupported responses compared with truncated validation. Our experience highlights when long-context verification is necessary, why chunk-based checking often fails in real documents, and how latency budgets shape model design. These findings provide practical guidance for practitioners building reliable large-scale retrieval-augmented applications. (Model, benchmark, and code: https://huggingface.co/llm-semantic-router)
