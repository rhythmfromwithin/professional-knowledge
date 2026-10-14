---
interest: medium
link: https://arxiv.org/abs/2610.12649
next_step: skim
priority: low
slack_ts: '1791952342.412389'
source: cs.SE - Software Engineering
status: unread
title: Quantifying SMT Solver Instability for Formal Verification
---
# Quantifying SMT Solver Instability for Formal Verification
> 原文: [https://arxiv.org/abs/2610.12649](https://arxiv.org/abs/2610.12649)

arXiv:2610.12649v1 Announce Type: new
Abstract: Program verification has become commonplace in software development projects, and much of its feasibility can be attributed to the potential of SMT solvers to automate model checking and other verification techniques. However, SMT instability, a phenomenon where semantically equivalent permutations of source code take much longer to solve or timeout, has been found to interrupt workflows and make software engineers more likely to avoid verification. Previous efforts to measure SMT instability have had difficulty quantifying it due to the abnormal runtime distributions it produces. In this paper, we use the coefficient of variation to model instability across an extensive dataset of SMT queries from three software domains. Our results show that SMT instability is significant in each area, and that it increases for queries that take longer on average. However, using a novel method to quantify instability, we show that a different approach is possible: if a solution were to optimize the structure of queries for runtime, rather than variance, instability could be mitigated while also improving overall solver performance.
