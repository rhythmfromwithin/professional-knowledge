---
interest: medium
link: https://arxiv.org/abs/2603.03369
next_step: skim
priority: low
slack_ts: '1773196785.572589'
source: cs.CR - Cryptography and Security
status: unread
title: 'Maude-HCS: Model Checking the Undetectability-Performance Tradeoffs of Hidden
  Communication Systems'
---
# Maude-HCS: Model Checking the Undetectability-Performance Tradeoffs of Hidden Communication Systems
> 原文: [https://arxiv.org/abs/2603.03369](https://arxiv.org/abs/2603.03369)

arXiv:2603.03369v1 Announce Type: new
Abstract: Hidden communication systems (HCS) embed covert messages within ordinary network activity to hide the presence of communication. In practice, the undetectability of an HCS is typically evaluated using ad hoc traffic statistics or specific detectors, making security claims tightly coupled to experimental setups and implicit adversarial assumptions. In this work, we formalize undetectability as the statistical indistinguishability of observable execution traces under two deployments: a baseline system without hidden communication and an HCS deployment carrying covert traffic. Undetectability is expressed as a bound on a quantitative measure of distance between the trace distributions induced by these two executions.
We develop Maude-HCS, an executable modeling and analysis framework that provides a principled and executable foundation for reasoning about undetectability-performance tradeoffs in complex HCS designs. Maude-HCS allows designers to specify protocol behavior, adversary observables, and environmental assumptions, and to generate Monte Carlo samples from the induced trace distributions. We show that Maude-HCS can be used to audit claims of undetectability by estimating the true and false positive rates of a statistical test and converting these estimates into lower bounds on undetectability measures such as KL divergence. This enables systematic evaluation of detectability and its tradeoffs with performance under explicitly stated modeling assumptions.
Finally, we evaluate Maude-HCS on tunneling-based HCS instantiations and validate model predictions against measurements from a physical testbed. For passive adversaries observing timing and traffic statistics, we quantify how undetectability and performance vary with protocol configuration, background traffic, and network loss, and demonstrate strong semantic alignment between model-based guarantees and empirical results.
