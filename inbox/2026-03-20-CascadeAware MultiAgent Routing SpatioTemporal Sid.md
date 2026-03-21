---
interest: medium
link: https://arxiv.org/abs/2603.17112
next_step: skim
priority: high
slack_ts: '1774060660.327919'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching'
---
# Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching
> 原文: [https://arxiv.org/abs/2603.17112](https://arxiv.org/abs/2603.17112)

arXiv:2603.17112v1 Announce Type: new
Abstract: A common architectural pattern in advanced AI reasoning systems is the symbolic graph network: specialized agents or modules connected by delegation edges, routing tasks through a dynamic execution graph. Current schedulers optimize load and fitness but are geometry-blind: they do not model how failures propagate differently in tree-like versus cyclic regimes. In tree-like delegation, a single failure can cascade exponentially; in dense cyclic graphs, failures tend to self-limit. We identify this observability gap, quantify its system-level cost, and propose a lightweight mitigation.
We formulate online geometry control for route-risk estimation on time-indexed execution graphs with route-local failure history. Our approach combines (i) a Euclidean spatio-temporal propagation baseline, (ii) a hyperbolic route-risk model with temporal decay (and optional burst excitation), and (iii) a learned geometry selector over structural features. The selector is a compact MLP (9->12->1) using six topology statistics plus three geometry-aware signals: BFS shell-growth slope, cycle-rank norm, and fitted Poincare curvature. On the Genesis 3 benchmark distribution, adaptive switching improves win rate in the hardest non\_tree regime from 64-72% (fixed hyperbolic variants) to 92%, and achieves 87.2% overall win rate.
To measure total system value, we compare against Genesis 3 routing without any spatio-temporal sidecar, using only native bandit/LinUCB signals (team fitness and mean node load). This baseline achieves 50.4% win rate overall and 20% in tree-like regimes; the full sidecar recovers 87.2% overall (+36.8 pp), with +48 to +68 pp gains in tree-like settings, consistent with a cascade-sensitivity analysis. Overall, a 133-parameter sidecar substantially mitigates geometry-blind failure propagation in one high-capability execution-graph system.
