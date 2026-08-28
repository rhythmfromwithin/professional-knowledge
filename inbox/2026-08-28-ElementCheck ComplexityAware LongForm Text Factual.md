---
title: "ElementCheck: Complexity-Aware Long-Form Text Factuality Evaluation via Sentence Elements"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.26118
priority: high
status: unread
interest: medium
next_step: skim
---
# ElementCheck: Complexity-Aware Long-Form Text Factuality Evaluation via Sentence Elements
> 原文: [https://arxiv.org/abs/2608.26118](https://arxiv.org/abs/2608.26118)

arXiv:2608.26118v1 Announce Type: new
Abstract: Existing long-form factuality evaluation relies on the decompose-retrieve-verify pipeline. However, the pipeline suffers from noise from claim decomposition and fixed verification granularity, resulting in unreliable results. We propose ElementCheck, a complexity-aware framework that verifies long-form outputs via sentence elements. Instead of uniformly decomposing sentences into atomic sub-claims, ElementCheck extracts entity pairs that are explicitly linked through verifiable connections in the original sentence as elements, and organizes these into an element graph. The graph topology provides a structural signal for estimating sentence complexity, enabling direct verification for simple sentences and targeted element-level refinement and verification for complex ones. To support fine-grained evaluation, we construct a new benchmark FastFact-Sent by mapping isolated claims from FastFact-Bench back to their source sentences. Experiments on FastFact-Sent and two domain-specific benchmarks show ElementCheck consistently improves factuality verification across five backbone models while maintaining a favorable accuracy-cost trade-off. Further analyses demonstrate that complexity-aware verification reduces unnecessary re-verification and maintains stability across different backbones.
