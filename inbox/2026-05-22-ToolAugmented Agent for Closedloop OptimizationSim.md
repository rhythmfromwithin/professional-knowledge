---
title: "Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.20190
priority: high
status: unread
interest: medium
next_step: skim
---
# Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration
> 原文: [https://arxiv.org/abs/2605.20190](https://arxiv.org/abs/2605.20190)

arXiv:2605.20190v1 Announce Type: new
Abstract: Iterative industrial design-simulation optimization is bottlenecked by the CAD-CAE semantic gap: translating simulation feedback into valid geometric edits under diverse, coupled constraints. To fill this gap, we propose COSMO-Agent (Closed-loop Optimization, Simulation, and Modeling Orchestration), a tool-augmented reinforcement learning (RL) framework that teaches LLMs to complete the closed-loop CAD-CAE process. Specifically, we cast CAD generation, CAE solving, result parsing, and geometry revision as an interactive RL environment, where an LLM learns to orchestrate external tools and revise parametric geometries until constraints are satisfied. To make this learning stable and industrially usable, we design a multi-constraint reward that jointly encourages feasibility, toolchain robustness, and structured output validity. In addition, we contribute an industry-aligned dataset that covers 25 component categories with executable CAD-CAE tasks to support realistic training and evaluation. Experiments show that COSMO-Agent training substantially improves small open-source LLMs for constraint-driven design, exceeding large open-source and strong closed-source models in feasibility, efficiency, and stability.
