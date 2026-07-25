---
title: "Search Hardness-Aware LLM-Based Problem Formulation for Expensive Simulation-Driven Design"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.21220
priority: low
status: unread
interest: medium
next_step: skim
---
# Search Hardness-Aware LLM-Based Problem Formulation for Expensive Simulation-Driven Design
> 原文: [https://arxiv.org/abs/2607.21220](https://arxiv.org/abs/2607.21220)

arXiv:2607.21220v1 Announce Type: new
Abstract: Expensive simulation-driven design is widely used in engineering to identify requirement-satisfying designs with as few high-fidelity simulations as possible. Most existing efforts address this challenge by improving optimization algorithms under fixed formulations, yet the formulation itself shapes the search landscape by defining the objectives and constraints optimized by the solver. Recent LLM-based automatic problem formulation methods generate formulations from natural-language requirements, but they mainly focus on design-intent alignment and overlook whether the formulation induces an efficient search process. To address this limitation, we propose SHA-PF, a search hardness-aware LLM-based problem formulation framework. We find that a formulation is more likely to guide efficient search when it prioritizes rare samples with greater progress potential. Based on this finding, SHA-PF defines a formulation search objective guided by search hardness, scoring each candidate formulation according to the priority. SHA-PF then searches the formulation space under this objective through LLM-based generation, repair, and evolutionary refinement. Experiments on the real-world multi-objective benchmark and five expensive antenna design benchmarks show that the formulations discovered by SHA-PF require significantly fewer evaluations to reach the design requirements than other baselines.
