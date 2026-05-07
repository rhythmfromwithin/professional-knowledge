---
title: "Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.03034
priority: high
status: unread
interest: medium
next_step: skim
---
# Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense
> 原文: [https://arxiv.org/abs/2605.03034](https://arxiv.org/abs/2605.03034)

arXiv:2605.03034v1 Announce Type: new
Abstract: Agentic systems involved in high-stake decision-making under adversarial pressure need formal guarantees not offered by existing approaches. Motivated by the operational needs of security operations centers (SOCs) that must configure endpoint detection and response (EDR) policies under adversarial pressure, we present a tool-mediated architecture: LLM agents use deterministic tools (Stackelberg best-response, Bayesian observer updates, attack-graph primitives) and select from finite action catalogs enforced at the tool-output interface. A composite Lyapunov function machine-checked in Lean 4 with zero sorry certifies controllability, observability from asymmetric sensor data, and Input-to-State Stability (ISS) robustness under intelligent adversarial disturbance, with two corollaries extending the certificate to any controller or adversary from the catalogs. On 282 real enterprise attack graphs, the claims hold with margin. On paired offensive/defensive telemetry, a tool-mediated Claude Sonnet 4 controller reduces the attacker's expected payoff (game value) by 59% relative to a deterministic greedy baseline, with zero variance across 40 runs at four temperatures. A Claude Haiku 4.5 controller converges to suboptimal game values but stays catalog-bounded over an additional 40 runs, demonstrating that architectural stability is not dependent on the controller capability. The LLM agent's non-determinism furthers creative exploration of strategies, while the tool-mediated architecture ensures system stability.
