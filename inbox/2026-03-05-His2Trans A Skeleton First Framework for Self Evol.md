---
interest: medium
link: https://arxiv.org/abs/2603.02617
next_step: skim
priority: low
slack_ts: '1773456088.992159'
source: cs.SE - Software Engineering
status: unread
title: 'His2Trans: A Skeleton First Framework for Self Evolving C to Rust Translation
  with Historical Retrieval'
---
# His2Trans: A Skeleton First Framework for Self Evolving C to Rust Translation with Historical Retrieval
> 原文: [https://arxiv.org/abs/2603.02617](https://arxiv.org/abs/2603.02617)

arXiv:2603.02617v1 Announce Type: new
Abstract: Automated C-to-Rust migration encounters systemic obstacles when scaling from code snippets to industrial projects, mainly because build context is often unavailable ("dependency hell") and domain-specific evolutionary knowledge is missing. As a result, current LLM-based methods frequently cannot reconstruct precise type definitions under complex build systems or infer idiomatic API correspondences, which in turn leads to hallucinated dependencies and unproductive repair loops. To tackle these issues, we introduce His2Trans, a framework that combines a deterministic, build-aware skeleton with self-evolving knowledge extraction to support stable, incremental migration. On the structural side, His2Trans performs build tracing to create a compilable Project-Level Skeleton Graph, providing a strictly typed environment that separates global verification from local logic generation. On the cognitive side, it derives fine-grained API and code-fragment rules from historical migration traces and uses a Retrieval-Augmented Generation (RAG) system to steer the LLM toward idiomatic interface reuse. Experiments on industrial OpenHarmony modules show that His2Trans reaches a 99.75% incremental compilation pass rate, effectively fixing build failures where baselines struggle. On general-purpose benchmarks, it lowers the unsafe code ratio by 23.6 percentage points compared to C2Rust while producing the fewest warnings. Finally, knowledge accumulation studies demonstrate the framework's evolutionary behavior: by continuously integrating verified patterns, His2Trans cuts repair overhead on unseen tasks by about 60%.
