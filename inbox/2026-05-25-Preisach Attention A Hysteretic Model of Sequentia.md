---
title: "Preisach Attention: A Hysteretic Model of Sequential Memory"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.23603
priority: low
status: unread
interest: medium
next_step: skim
---
# Preisach Attention: A Hysteretic Model of Sequential Memory
> 原文: [https://arxiv.org/abs/2605.23603](https://arxiv.org/abs/2605.23603)

arXiv:2605.23603v1 Announce Type: cross
Abstract: We introduce the Preisach Attention Layer (PAL), a novel sequence modelling architecture grounded in the classical Preisach hysteresis operator from mathematical physics. PAL replaces the softmax attention mechanism with a binary relay operator parameterised by learned activation and deactivation thresholds, maintaining a stack of local extrema as its internal state. A single-layer PAL-Transformer with O(1) depth is Turing-complete under arbitrary precision arithmetic, achievable through simulation of a two-stack pushdown automaton -- in contrast to the O(log n) depth required by standard hard-attention transformers. Second, we prove that the function classes computable by PAL and by the transformer are incomparable: PAL computes historical range statistics in O(1) layers that require O(log n) layers for transformers, while transformers support random-access retrieval that PAL cannot perform without auxiliary state. The separating property is rate-independence -- PAL responds only to the sequence of local extrema, not to absolute token positions or temporal spacing. Third, we show that the extremum stack constitutes a minimal sufficient statistic of the input history for all rate-independent functionals, providing a formal analogue of the wiping property in classical hysteresis theory. PAL is thus an efficient architecture for tasks with long episodic memory and weak positional dependence, with O(n log n) total inference cost versus O(n^2) for standard attention.
