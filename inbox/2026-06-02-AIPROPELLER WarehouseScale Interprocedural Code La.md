---
interest: medium
link: https://arxiv.org/abs/2606.00131
next_step: skim
priority: low
slack_ts: '1780375677.544909'
source: cs.SE - Software Engineering
status: unread
title: 'AI-PROPELLER: Warehouse-Scale Interprocedural Code Layout Optimization with
  AlphaEvolve'
---
# AI-PROPELLER: Warehouse-Scale Interprocedural Code Layout Optimization with AlphaEvolve
> 原文: [https://arxiv.org/abs/2606.00131](https://arxiv.org/abs/2606.00131)

arXiv:2606.00131v1 Announce Type: new
Abstract: Post-link optimizers (PLOs) such as Propeller and BOLT have demonstrated that precise, profile-guided code layout can extract significant performance gains from heavily optimized binaries. However, these systems are currently restricted to intraprocedural techniques, leaving the global potential of interprocedural layout largely untapped. Interprocedural code layout is historically difficult due to a combinatorially intractable search space and complex call-return semantics that are challenging to model. Consequently, the performance potential of fine-grained interprocedural layout remains unproven in practice. AI-PROPELLER uses Magellan, an agentic workflow that evolves the compiler heuristic in Propeller into a fine-grained interprocedural optimizer and fine-tunes the resulting policy hyperparameters. To ensure high-fidelity, we move away from approximate static cost models and the agentic workflow generates multiple layout variants that are executed on actual hardware to measure real performance counters, providing a precise reward signal for the evolutionary loop. AI-PROPELLER has been evaluated on several benchmarks including large warehouse-scale applications and experiments show performance improvements of 0.23% to 1.6% optimized with state-of-the-art FDO and PLO which is significant for real-world binaries. This is the first time ever that large warehouse-scale applications in industrial settings have been optimized with fine-grained interprocedural code layout.
