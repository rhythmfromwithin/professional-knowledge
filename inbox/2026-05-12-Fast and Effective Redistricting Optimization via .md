---
title: "Fast and Effective Redistricting Optimization via Composite-Move Tabu Search"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.06682
priority: high
status: unread
interest: medium
next_step: skim
---
# Fast and Effective Redistricting Optimization via Composite-Move Tabu Search
> 原文: [https://arxiv.org/abs/2605.06682](https://arxiv.org/abs/2605.06682)

arXiv:2605.06682v1 Announce Type: new
Abstract: Spatial redistricting is a practical combinatorial optimization problem that demands high-quality solutions, rapid turnaround, and flexibility to accommodate multi-criteria objectives and interactive refinement. A central challenge is the contiguity constraint: enforcing contiguity in integer-programming or heuristic search can severely shrink the feasible neighborhood, weaken exploration, and trap the search in poor local optima. We introduce a composite-move Tabu search (CM-Tabu) that systematically expands the feasible neighborhood space in Tabu search while preserving contiguity. When a boundary unit cannot be reassigned individually without disconnecting its district, our method identifies a minimal set of units that can move together, or a pair of units (or sets of units) that can be switched, as a contiguity-preserving composite move. Candidate single-unit and composite moves are generated in linear time by analyzing each district's contiguity graph using articulation points and biconnected components. Extensive experiments demonstrate that the proposed approach substantially improves solution quality, run-to-run robustness, and computational efficiency relative to traditional Tabu search and other baselines. For example, in the Philadelphia case, the approach can consistently attain the theoretical global optimum in population-equality and support multi-criteria trade-offs. CM-Tabu delivers optimization performance suitable for real-world practices and decision-support workflows.
