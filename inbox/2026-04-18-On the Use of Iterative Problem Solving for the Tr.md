---
interest: medium
link: https://arxiv.org/abs/2604.14745
next_step: skim
priority: low
slack_ts: '1776656356.901509'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: On the Use of Iterative Problem Solving for the Traveling Salesperson Problem
  with Changing Time Window Constraints
---
# On the Use of Iterative Problem Solving for the Traveling Salesperson Problem with Changing Time Window Constraints
> 原文: [https://arxiv.org/abs/2604.14745](https://arxiv.org/abs/2604.14745)

arXiv:2604.14745v1 Announce Type: new
Abstract: In many real-world settings, problem instances that need to be solved are quite similar, and knowledge from previous optimization runs can potentially be utilized. We explore this for the Traveling Salesperson problem with time windows (TSPTW), which often arises in settings where the travel-time matrix is fixed but time-window constraints change across related tasks. Existing TSPTW studies, however, have not systematically compared solving such task sequences independently with sequential transfer from previously solved tasks. We address this gap using a multi-task benchmark in which each base instance is expanded into five related tasks under two environments: partial time-window expansion and swap-additive time reassignment. We compare a standard from-scratch protocol with an iterative protocol that initializes each task from the best tour of the previous task, using the popular local search approaches LNS, VNS, and LKH-3 under a common penalized-score objective. Our experimental results show that the iterative protocol is consistently superior in the progressive-relaxation setting and generally competitive under swap-additive changes, with improvements increasing on more difficult instances.
