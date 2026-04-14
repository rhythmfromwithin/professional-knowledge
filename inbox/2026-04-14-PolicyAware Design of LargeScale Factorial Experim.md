---
title: "Policy-Aware Design of Large-Scale Factorial Experiments"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.08804
priority: medium
status: unread
interest: medium
next_step: skim
---
# Policy-Aware Design of Large-Scale Factorial Experiments
> 原文: [https://arxiv.org/abs/2604.08804](https://arxiv.org/abs/2604.08804)

arXiv:2604.08804v1 Announce Type: new
Abstract: Digital firms routinely run many online experiments on shared user populations. When product decisions are compositional, such as combinations of interface elements, flows, messages, or incentives, the number of feasible interventions grows combinatorially, while available traffic remains limited. Overlapping experiments can therefore generate interaction effects that are poorly handled by decentralized A/B testing. We study how to design large-scale factorial experiments when the objective is not to estimate every treatment effect, but to identify a high-performing policy under a fixed experimentation budget. We propose a two-stage design that centralizes overlapping experiments into a single factorial problem and models expected outcomes as a low-rank tensor. In the first stage, the platform samples a subset of intervention combinations, uses tensor completion to infer performance on untested combinations, and eliminates weak factor levels using estimated marginal contributions. In the second stage, it applies sequential halving to the surviving combinations to select a final policy. We establish gap-independent simple-regret bounds and gap-dependent identification guarantees showing that the relevant complexity scales with the degrees of freedom of the low-rank tensor and the separation structure across factor levels, rather than the full factorial size. In an offline evaluation based on a product-bundling problem constructed from 100 million Taobao interactions, the proposed method substantially outperforms one-shot tensor completion and unstructured best-arm benchmarks, especially in low-budget and high-noise settings. These results show how centralized, policy-aware experimentation can make combinatorial product design operationally feasible at platform scale.
