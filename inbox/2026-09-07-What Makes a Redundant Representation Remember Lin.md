---
interest: medium
link: https://arxiv.org/abs/2609.05304
next_step: skim
priority: low
slack_ts: '1788840734.098979'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: What Makes a Redundant Representation Remember? Lineage Isolation, Not Masking
---
# What Makes a Redundant Representation Remember? Lineage Isolation, Not Masking
> 原文: [https://arxiv.org/abs/2609.05304](https://arxiv.org/abs/2609.05304)

arXiv:2609.05304v1 Announce Type: new
Abstract: Memory-based evolutionary algorithms for dynamic optimization often carry a redundant second copy of the genotype and expose only one copy to the objective, on the assumption that the shielded copy accumulates information about past optima. We show this assumption is false as usually implemented, and identify the structural property that actually determines whether the shielded copy retains information. We formalize such methods as a gated dual-copy representation with two independent design axes: a gating rule deciding which copy is evaluated, and an inheritance rule deciding whether the two copies mix across generations. A ablation shows retained information is governed almost entirely by the inheritance rule (21.4 vs. 1.3 bits) and is nearly invariant to the gating rule. Per-locus independent inheritance reshuffles cross-locus structure every generation, so shielding preserves the variance of the hidden copy while destroying the pattern that constitutes a memory. Under isolated inheritance the memory effect is real: against a single-copy baseline matched for representation budget, the method gains +0.010 AUC when optima recur periodically and loses 0.078 when they drift unidirectionally---a 0.089 separation under otherwise identical settings, which excludes explanations based on added capacity. We show the readout rate is also the corruption rate, predicting and confirming an interior optimum replicated across two implementations. We report one negative result with a mechanism: dual-copy representations lower the mutational error threshold, because gated expression is a selector rather than a joint decoder and therefore provides no coding gain. Finally, we document a benchmarking hazard: on dynamic benchmarks the choice of recombination operator alone shifted our baseline by 0.062 AUC, six times the effect size under study.
