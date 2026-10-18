---
interest: medium
link: https://arxiv.org/abs/2610.21924
next_step: skim
priority: medium
slack_ts: '1792296494.729909'
source: cs.CY - Computers and Society
status: unread
title: Learning to Transfer School Attendance Zoning across Cities
---
# Learning to Transfer School Attendance Zoning across Cities
> 原文: [https://arxiv.org/abs/2610.21924](https://arxiv.org/abs/2610.21924)

arXiv:2610.21924v1 Announce Type: new
Abstract: Designing multi-school attendance zones requires selecting constraint settings that balance educational equity, accessibility, and school capacity. Repeating this process for each new city can require substantial local calibration and computational search. We introduce COMPASS, a parameter-to-policy framework that transfers knowledge from previous zoning searches to unseen cities through supervised prediction. Using search-derived parameter configurations as offline supervision, COMPASS learns to predict interpretable zoning-control parameters from urban representations and zoning-difficulty signals. A downstream mixed-integer linear program converts these parameters into explicit zoning plans, with conditional parameter repair when the initial solve is unsuccessful. We evaluate parameter prediction, zoning-outcome recovery, and computational efficiency through five-fold cross-validation across 3,000 US cities, complemented by a case study of Atlanta. COMPASS achieves a 99.80% solver-feasible success rate and a 49.14-fold median deployment-time speedup relative to repeated city-specific parameter search. Further analysis shows that transfer performance varies across urban contexts and policy dimensions: structurally difficult cities receive the largest feasibility gains, while enrollment balance remains the hardest outcome to recover. These findings demonstrate how cross-city learning can reduce repeated search while retaining explicit zoning controls and spatial plans for local inspection and adaptation.
