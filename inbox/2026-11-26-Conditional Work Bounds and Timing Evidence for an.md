---
interest: medium
link: https://arxiv.org/abs/2611.33159
next_step: skim
priority: medium
slack_ts: '1795850658.741799'
source: cs.DC - Distributed Computing
status: unread
title: 'Conditional Work Bounds and Timing Evidence for an Industrial NDT Scan Matcher:
  Cross-Language Work-Trace Conformance'
---
# Conditional Work Bounds and Timing Evidence for an Industrial NDT Scan Matcher: Cross-Language Work-Trace Conformance
> 原文: [https://arxiv.org/abs/2611.33159](https://arxiv.org/abs/2611.33159)

arXiv:2611.33159v1 Announce Type: new
Abstract: Normal Distributions Transform (NDT) scan matching has strongly input-dependent execution time on the localization critical path. We study the align kernel of Autoware's production matcher; map loading, preprocessing, and Robot Operating System scheduling are outside the timed scope. Our three-layer method enforces and property-tests a conditional structural work envelope, constructs stress witnesses with deterministic Rust counters, and measures frozen witnesses. It separates algorithmic work from platform time and does not claim a certified hard time bound. A domain-informed construction attains the configured ceiling for the language-common kernel-evaluation term; two archived candidates exercise higher Rust-specific kd-tree traversal at lower common work. Per-input traces define work-trace conformance over passes, processed points, neighbor counts, and leaf identities. Leaf payloads, implementation-specific traversal, total work, and latency remain outside that relation, so C++ results are observations over transferred fixtures rather than a C++ worst-case search. An auxiliary cropped-map, degraded-prior replay exposes the remaining conformance boundary, and a closed-loop replay with recovery shows both engines re-initializing at the same route sections with disjoint coverage bands. In a unified three-boot synthetic campaign, the largest observed values are 988.2 ms for C++ and 610.5 ms for Rust; Rust has the smaller maximum on all 10 paired fixtures. On neighbor-returning fixtures, C++ performs approximately 11 heap allocations per point per derivative pass, whereas the Rust align path allocates none within its reserved envelope. Rust narrows the safe-core verification surface but is not required for bounded execution; its unsafe code, foreign-function interface, and dependencies remain trusted.
