---
title: "When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.24676
priority: high
status: unread
interest: medium
next_step: skim
---
# When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs
> 原文: [https://arxiv.org/abs/2603.24676](https://arxiv.org/abs/2603.24676)

arXiv:2603.24676v1 Announce Type: new
Abstract: Multi-agent systems powered by large language models (LLMs) are increasingly deployed in settings that shape consequential decisions, both directly and indirectly. Yet it remains unclear whether their outcomes reflect collective reasoning, systematic bias, or mere chance. Recent work has sharpened this question with naming games, showing that even when no individual agent favors any label a priori, populations rapidly break symmetry and reach consensus. Here, we reveal the mechanism by introducing a minimal model, Quantized Simplex Gossip (QSG), and trace the microscopic origin of this agreement to mutual in-context learning. In QSG, agents maintain internal belief states but learn from one another's sampled outputs, so one agent's arbitrary choice becomes the next agent's evidence and can compound toward agreement. By analogy with neutral evolution, we call this sampling-driven regime memetic drift. QSG predicts a crossover from a drift-dominated regime, where consensus is effectively a lottery, to a selection regime, where weak biases are amplified and shape the outcome. We derive scaling laws for drift-induced polarization as a function of population size, communication bandwidth, in-context adaptation rate, and agents' internal uncertainty, and we validate them in both QSG simulations and naming-game experiments with LLM populations. Together, these results provide a framework for studying the collective mechanisms of social representation formation in multi-agent systems.
