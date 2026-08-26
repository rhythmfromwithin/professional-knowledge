---
interest: medium
link: https://arxiv.org/abs/2608.21489
next_step: skim
priority: low
slack_ts: '1787708805.672419'
source: cs.SE - Software Engineering
status: unread
title: Composable Building Blocks for Resilient Asynchronous Code
---
# Composable Building Blocks for Resilient Asynchronous Code
> 原文: [https://arxiv.org/abs/2608.21489](https://arxiv.org/abs/2608.21489)

arXiv:2608.21489v1 Announce Type: new
Abstract: Asynchronous calls to a network service, database, or language model must cope with transient errors, slow or missing responses, throttling, and atomicity violations. We show how higher-order combinators solve such problems uniformly, including timeouts, retries, rate limiting, caching, reentrant locking, and cancellation. Every combinator maps an async function to another of the same type, so they share a uniform \emph{shape} and compose by nesting into one expression that implements a program's whole resilience and concurrency policy, leaving its business logic untouched. The same design spans both of JavaScript's native async shapes, promise-returning and async-iterable-returning functions, with one vocabulary of concerns. Solutions exist across the ecosystem but are scattered over differently shaped libraries that are hard to combine. We present case studies where the combinators are used to harden real packages by adding missing resilience or concurrency control and replacing bespoke policy.
