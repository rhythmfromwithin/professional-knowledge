---
interest: medium
link: https://arxiv.org/abs/2606.17266
next_step: skim
priority: high
slack_ts: '1781759644.948009'
source: cs.AI - Artificial Intelligence
status: unread
title: 'SkillChain-Gym: A Benchmark for Reskilling-Aware Production-Inventory Control
  under Disruptions'
---
# SkillChain-Gym: A Benchmark for Reskilling-Aware Production-Inventory Control under Disruptions
> 原文: [https://arxiv.org/abs/2606.17266](https://arxiv.org/abs/2606.17266)

arXiv:2606.17266v1 Announce Type: new
Abstract: Production planning increasingly has to treat workforce capability as a decision variable: certifications lapse when skills are not maintained, new products require skills the current workforce does not hold, and reskilling competes for the same worker hours needed for production. Existing operations benchmarks usually treat labor as exogenous, while workforce-planning models with skills and learning are rarely released as reusable testbeds. We introduce SkillChain-Gym, a benchmark specification for reskilling-aware production-inventory control: a single-site environment with stylized worker skill-state dynamics, hard threshold certification, forgetting, and capacity-consuming training actions constrained by the same per-worker time budget as production. The benchmark includes seed-controlled disruption scenarios, three feasibility modes with projection diagnostics, deterministic replay, and metrics covering operations, resilience, capability growth, and training-access distribution. We evaluate production-only, reactive adaptive, water-filling adaptive, and static-insurance policies with budget variants over 60-shift horizons with paired statistical tests. The results are regime-dependent rather than a ranking. Training-capable policies dominate the production-only baseline, and maintenance training is necessary under forgetting even without disruptions. Among training-capable classes, adaptive training helps when bottlenecks are visible in the forecast, while a lean static cross-training plan, a deliberately favorable comparator whose structure encodes relevant skill contingencies, acts as strong insurance under surprise shocks and absenteeism. Capacity slack and the forgetting rate govern the boundary between these regimes. No policy class dominates across regimes, motivating forecast-driven controllers that decide when to buy skill insurance and when to react.
