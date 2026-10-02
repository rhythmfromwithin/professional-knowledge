---
title: "TeamLens in Critsly: A Consent-Based Team-Composition Interface and Synthetic Readiness Evaluation for Design Collaboration"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2610.00288
priority: medium
status: unread
interest: medium
next_step: skim
---
# TeamLens in Critsly: A Consent-Based Team-Composition Interface and Synthetic Readiness Evaluation for Design Collaboration
> 原文: [https://arxiv.org/abs/2610.00288](https://arxiv.org/abs/2610.00288)

arXiv:2610.00288v1 Announce Type: new
Abstract: Discussing working preferences may support reflection within a design team, but a personality label should not become a performance prediction or a condition of participation. This technical report presents TeamLens, an optional Critsly interface for voluntarily sharing a self-reported MBTI type with a particular board. It separates account activation from disclosure, displays descriptive composition counts, and provides distinct controls for disabling visibility, withdrawing one report and deleting all of one's reports. The evaluation combines released-source inspection, independently specified synthetic aggregation cases, access and lifecycle checks, browser component tests, a local database microbenchmark and deployment records. All 65,536 binary eligibility subsets of sixteen fixed, distinct type reports matched an independent oracle; 128 seeded multiplicity fixtures also matched, after 4,259 synthetic share calls. The isolated HTTP suite passed 183 assertions. In 180 sequential in-memory SQLite read trials, median service-call time increased from 0.064 ms with no profile rows to 200.932 ms with 1,024 rows; instrumented SQL operations followed 11+3n. These findings concern exercised software behaviour and a bounded workload. They do not establish human usability, psychometric validity, learning gains, team-performance effects or production capacity. The contribution is an implemented disclosure-to-aggregation workflow and an auditable technical account of its correctness boundaries, privacy limitations and scaling cost. OpenAI Codex assisted with implementation, evaluation and manuscript preparation; the paper discloses this use and its limits.
