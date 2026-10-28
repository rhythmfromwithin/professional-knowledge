---
title: "GNBG-C: A Unified and Configurable Benchmark Generator for Constrained Continuous Optimization"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2610.37590
priority: low
status: unread
interest: medium
next_step: skim
---
# GNBG-C: A Unified and Configurable Benchmark Generator for Constrained Continuous Optimization
> 原文: [https://arxiv.org/abs/2610.37590](https://arxiv.org/abs/2610.37590)

arXiv:2610.37590v1 Announce Type: new
Abstract: Many real-world optimization tasks are governed not only by what should be optimized, but also by what is allowed: a solution must first satisfy physical, operational, safety, budgetary, or structural requirements before its objective value becomes meaningful. Yet benchmark design for constrained continuous optimization often treats these restrictions as fixed properties of predefined test instances. Existing generators and benchmark suites provide essential foundations for reproducible comparison, but they either focus primarily on configurable objective landscapes or expose constraint properties within limited, predefined regimes, making it difficult to ask targeted questions about constraint-induced difficulty: whether an optimizer struggles because feasible regions are small, boundaries are restrictive, variables are tightly coupled, or constraint information is poorly scaled. We introduce GNBG-C, a Generalized Numerical Benchmark Generator for Constrained Continuous Optimization. The central idea is to treat the feasible region itself as a configurable object rather than as an inseparable attachment to a fixed test function. By generating controlled constraint regimes around the known GNBG global minimizer, the generator enables systematic studies in which feasibility pressure can be varied while preserving that point as a global minimizer of the constrained problem. This allows researchers to examine how optimizers discover feasibility, handle constraint pressure, and improve objective quality under diverse and controllable feasibility conditions. GNBG-C therefore provides a flexible and auditable framework for probing the strengths and weaknesses of constrained continuous optimizers under targeted forms of feasibility-side difficulty.
