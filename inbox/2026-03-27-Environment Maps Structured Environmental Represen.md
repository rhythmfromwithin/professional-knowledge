---
title: "Environment Maps: Structured Environmental Representations for Long-Horizon Agents"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.23610
priority: high
status: unread
interest: medium
next_step: skim
---
# Environment Maps: Structured Environmental Representations for Long-Horizon Agents
> 原文: [https://arxiv.org/abs/2603.23610](https://arxiv.org/abs/2603.23610)

arXiv:2603.23610v2 Announce Type: new
Abstract: Although large language models (LLMs) have advanced rapidly, robust automation of complex software workflows remains an open problem. In long-horizon settings, agents frequently suffer from cascading errors and environmental stochasticity; a single misstep in a dynamic interface can lead to task failure, resulting in hallucinations or trial-and-error. This paper introduces $\textit{Environment Maps}$: a persistent, agent-agnostic representation that mitigates these failures by consolidating heterogeneous evidence, such as screen recordings and execution traces, into a structured graph. The representation consists of four core components: (1) Contexts (abstracted locations), (2) Actions (parameterized affordances), (3) Workflows (observed trajectories), and (4) Tacit Knowledge (domain definitions and reusable procedures). We evaluate this framework on the WebArena benchmark across five domains. Agents equipped with environment maps achieve a 28.2% success rate, nearly doubling the performance of baselines limited to session-bound context (14.2%) and outperforming agents that have access to the raw trajectory data used to generate the environment maps (23.3%). By providing a structured interface between the model and the environment, Environment Maps establish a persistent foundation for long-horizon planning that is human-interpretable, editable, and incrementally refinable.
