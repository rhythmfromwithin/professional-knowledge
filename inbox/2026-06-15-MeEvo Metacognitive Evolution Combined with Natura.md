---
interest: medium
link: https://arxiv.org/abs/2606.14202
next_step: skim
priority: low
slack_ts: '1781500245.908369'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'MeEvo: Metacognitive Evolution Combined with Natural Evolution for Automatic
  Heuristic Design'
---
# MeEvo: Metacognitive Evolution Combined with Natural Evolution for Automatic Heuristic Design
> 原文: [https://arxiv.org/abs/2606.14202](https://arxiv.org/abs/2606.14202)

arXiv:2606.14202v1 Announce Type: new
Abstract: Large Language Models (LLMs) have advanced Automatic Heuristic Design (AHD) by enabling heuristic generation through reasoning and code synthesis. Existing LLM-based AHD architectures mainly follow two paradigms: Natural Evolution, which uses crossover and mutation to explore heuristic programs, and Metacognitive Evolution, which refines reasoning through reflection. However, Natural Evolution discards reasoning traces, weakening knowledge inheritance and exploitation, while Metacognitive Evolution lacks population-level recombination, limiting exploration and increasing the risk of premature convergence. These limitations reduce search efficiency, stability, and solution quality on complex problems. To address this gap, we propose MeEvo, a dual-layer AHD framework that cyclically couples Natural Evolution and Metacognitive Evolution. Natural Evolution explores heuristic code while recording reasoning traces, fitness values, and errors into a shared history; Metacognitive Evolution then reflects on this history to generate improved heuristics that re-enter the parent pool for the next cycle. This design enables population-driven exploration and reflection-driven refinement to reinforce each other. Experiments on five optimization problems with two LLM backbones show that MeEvo achieves stronger and more stable performance than existing LLM-based AHD architectures, especially on complex constrained tasks.
