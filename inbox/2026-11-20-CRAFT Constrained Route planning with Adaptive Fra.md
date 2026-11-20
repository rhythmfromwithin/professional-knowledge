---
interest: medium
link: https://arxiv.org/abs/2611.25128
next_step: skim
priority: low
slack_ts: '1795157506.962179'
source: cs.DB - Databases
status: unread
title: 'CRAFT: Constrained Route planning with Adaptive Framework and Template-based
  code generation'
---
# CRAFT: Constrained Route planning with Adaptive Framework and Template-based code generation
> 原文: [https://arxiv.org/abs/2611.25128](https://arxiv.org/abs/2611.25128)

arXiv:2611.25128v1 Announce Type: new
Abstract: Everyday routing requests are rarely a point-to-point shortest path. A driver may need to visit stops, sometimes in a fixed order, under time budgets or distance limits, and perhaps recharge their EV car along the way. Each combination is a distinct routing problem that classically requires its own algorithm, so no fixed solver covers the space of queries users may ask. This paper presents CRAFT, which takes a constrained routing query as free text and returns a route that satisfies the user's requirements on a real road network. An LLM parses the query and generates four search functions, which a generic graph-search engine executes on the road network. We formalize the underlying problem as State-Expanded RCSP (SE-RCSP), which extends resource-constrained shortest paths (RCSP) with non-additive state such as node-dependent resets and discrete progress tracking. We evaluate CRAFT on 2,600 natural-language queries over California road networks against two baselines, analyzing correctness, constraint violations, long-distance scalability, and semantic POI filtering.
