---
interest: medium
link: https://arxiv.org/abs/2603.05517
next_step: skim
priority: high
slack_ts: '1773715518.175469'
source: cs.LG - Machine Learning
status: unread
title: 'Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable
  Policies for Safe, Robust, and Efficient Agents'
---
# Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents
> 原文: [https://arxiv.org/abs/2603.05517](https://arxiv.org/abs/2603.05517)

arXiv:2603.05517v1 Announce Type: new
Abstract: Autonomous LLM agents fail because long-horizon policy remains implicit in model weights and transcripts, while safety is retrofitted post hoc. We propose Traversal-as-Policy: distill sandboxed OpenHands execution logs into a single executable Gated Behavior Tree (GBT) and treat tree traversal -- rather than unconstrained generation -- as the control policy whenever a task is in coverage. Each node encodes a state-conditioned action macro mined and merge-checked from successful trajectories; macros implicated by unsafe traces attach deterministic pre-execution gates over structured tool context and bounded history, updated under experience-grounded monotonicity so previously rejected unsafe contexts cannot be re-admitted. At runtime, a lightweight traverser matches the base model's intent to child macros, executes one macro at a time under global and node-local gating, and when stalled performs risk-aware shortest-path recovery to a feasible success leaf; the visited path forms a compact spine memory that replaces transcript replay. Evaluated in a unified OpenHands sandbox on 15+ software, web, reasoning, and safety/security benchmarks, GBT improves success while driving violations toward zero and reducing cost. On SWE-bench Verified (Protocol A, 500 issues), GBT-SE raises success from 34.6% to 73.6%, reduces violations from 2.8% to 0.2%, and cuts token/character usage from 208k/820k to 126k/490k; with the same distilled tree, 8B executors more than double success on SWE-bench Verified (14.0%58.8%) and WebArena (9.1%37.3%).
