---
interest: medium
link: https://arxiv.org/abs/2606.06618
next_step: skim
priority: medium
slack_ts: '1780894163.078239'
source: cs.RO - Robotics
status: unread
title: 'ChronoForest: Closed-Loop Multi-Tree Diffusion Planning for Efficient Bridge
  Search and Route Composition'
---
# ChronoForest: Closed-Loop Multi-Tree Diffusion Planning for Efficient Bridge Search and Route Composition
> 原文: [https://arxiv.org/abs/2606.06618](https://arxiv.org/abs/2606.06618)

arXiv:2606.06618v1 Announce Type: new
Abstract: How can we plan long-horizon routes that reach designated goals, visit required waypoints, and remain short when only short-horizon offline trajectories are available? This problem matters in offline navigation because collecting sufficiently rich long-horizon data is difficult, yet real agents must still solve long-range tasks with route-level efficiency rather than mere feasibility. The difficulty is twofold: at the microscopic level, composing many short-horizon segments creates a trade-off between search cost and path quality, while at the macroscopic level, waypoint ordering requires comparing pairwise travel costs among start, goal, and waypoint anchors that are unknown before planning and increasingly unreliable when estimated only from long-range temporal distance.
In this paper, we propose ChronoForest, a closed-loop planning system that couples local bridge search and online route re-solving through an anchor-chaining tree diffusion planner and an online multi-tree orchestrator. ChronoForest uses temporal distance for short-range guidance and node evaluation, while using search-time bridge evidence to validate long-range anchor connectivity and repeatedly re-solve the route. On OGBench AntMaze-Stitch, ChronoForest achieves 99.8%, 99.3%, and 99.5% success on the medium, large, and giant splits and improves giant-stitch success by up to 34.5 points over prior reported diffusion-based results. On Hamiltonian route-composition benchmarks, online re-solving corrects poor temporal orderings and improves route quality while remaining substantially cheaper than exhaustive planning.
