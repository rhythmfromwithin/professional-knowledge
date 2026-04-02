---
title: "CREST: Constraint-Release Execution for Multi-Robot Warehouse Shelf Rearrangement"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.28803
priority: medium
status: unread
interest: medium
next_step: skim
---
# CREST: Constraint-Release Execution for Multi-Robot Warehouse Shelf Rearrangement
> 原文: [https://arxiv.org/abs/2603.28803](https://arxiv.org/abs/2603.28803)

arXiv:2603.28803v1 Announce Type: new
Abstract: Double-Deck Multi-Agent Pickup and Delivery (DD-MAPD) models the multi-robot shelf rearrangement problem in automated warehouses. MAPF-DECOMP is a recent framework that first computes collision-free shelf trajectories with a MAPF solver and then assigns agents to execute them. While efficient, it enforces strict trajectory dependencies, often leading to poor execution quality due to idle agents and unnecessary shelf switching. We introduce CREST, a new execution framework that achieves more continuous shelf carrying by proactively releasing trajectory constraints during execution. Experiments on diverse warehouse layouts show that CREST consistently outperforms MAPF-DECOMP, reducing metrics related to agent travel, makespan, and shelf switching by up to 40.5\%, 33.3\%, and 44.4\%, respectively, with even greater benefits under lift/place overhead. These results underscore the importance of execution-aware constraint release for scalable warehouse rearrangement. Code and data are available at https://github.com/ChristinaTan0704/CREST.
