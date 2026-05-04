---
interest: medium
link: https://arxiv.org/abs/2604.26955
next_step: skim
priority: medium
slack_ts: '1777866888.802859'
source: cs.CY - Computers and Society
status: unread
title: Policy-Governed LLM Routing with Intent Matching for Instrument Laboratories
---
# Policy-Governed LLM Routing with Intent Matching for Instrument Laboratories
> 原文: [https://arxiv.org/abs/2604.26955](https://arxiv.org/abs/2604.26955)

arXiv:2604.26955v1 Announce Type: new
Abstract: AI tutoring systems in engineering labs face a tension between providing sufficient assistance and preserving learning opportunities. Existing systems typically offer instructors limited control over assistance timing, content, or cost. This paper describes a routing and governance system for LLM-based lab assistance comprising two components: Routiium, an OpenAI-compatible gateway that manages multiple LLM backends with configurable prompt modifications and usage logging, and EduRouter, a policy-aware routing service that enforces per-lab budgets, approval workflows, and embedding-based question matching. We evaluated the system using trace-driven simulation calibrated from two engineering labs (LED characterization, RC circuit analysis) and a 100-query replay through live models. In simulations, governed policies (P1/P2) increased challenge-alignment index from 0.90 to 0.98 and overlay-adherence score from 0.69 to 0.87 compared to ungoverned operation (P0). The productive-struggle window metric increased from 1.4 to 3.6 simulated turns before high-scaffold hints appeared. In the 100-query replay, EduRouter routed 75% of queries to a local model, reducing token costs by 66% ($0.087 vs. $0.26 for all-premium routing) while maintaining canonical hit rate of 1.0 for the curated 89-intent question bank. We release Routiium, EduRouter, canonical-task tooling, and simulator configurations to support replication and future classroom studies.
