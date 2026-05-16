---
interest: medium
link: https://arxiv.org/abs/2605.13365
next_step: skim
priority: low
slack_ts: '1778903332.477049'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'The Geno-Synthetic Algorithm: Type-Factored Coevolutionary Optimization for
  Heterogeneous Genotypes and Assembled Phenotypes'
---
# The Geno-Synthetic Algorithm: Type-Factored Coevolutionary Optimization for Heterogeneous Genotypes and Assembled Phenotypes
> 原文: [https://arxiv.org/abs/2605.13365](https://arxiv.org/abs/2605.13365)

arXiv:2605.13365v1 Announce Type: new
Abstract: Many real-world optimization problems are not naturally homogeneous vectors but composite design objects with heterogeneous parameters: integers, real values, Booleans, categoricals, complex-valued descriptors, and embedding vectors. Standard evolutionary algorithms flatten these into a single chromosome and apply generic operators with rounding and repair, sacrificing representational fidelity. We introduce the Geno-Synthetic Algorithm (GSA), a type-factored coevolutionary framework in which gene families are partitioned by representational type, evolved in parallel with type-native operators, and assembled into executable phenotypes for joint fitness evaluation. GSA is formalized as a typed product-space search procedure with an explicit assembly operator. An open-source reference implementation (gsa-experiments, MIT-licensed) is released. A focused empirical study compares eight GSA variants against five baselines across seven benchmark problems (six synthetic plus the external COCO BBOB-MixInt suite) at budgets from 5,000 to 100,000 evaluations. The headline finding is architectural: GSA is the only method that operates when gene families include complex-valued descriptors or embedding vectors. On smooth synthetic multi-family problems, well-tuned flattened differential evolution remains the strongest baseline; on BBOB-MixInt at 100,000 evaluations, GSA\_DIRECT becomes statistically indistinguishable from FLATTENED\_DE while FLATTENED\_EA drops from second to fifth rank, an asymptotic crossover. Ablations confirm that type-native operators are essential, elite credit dominates ensemble credit, and active assembly outperforms passive concatenation on gated benchmarks. The framework extends naturally to prompt and embedding optimization for large language model systems.
