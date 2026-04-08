---
slack_ts: '1775618436.609269'
---
# D\'ej\`aVu: A Minimalistic Mechanism for Distributed Plurality Consensus
> 原文: [https://arxiv.org/abs/2604.03648](https://arxiv.org/abs/2604.03648)

arXiv:2604.03648v2 Announce Type: new
Abstract: We study the plurality consensus problem in distributed systems where a population of extremely simple agents, each initially holding one of k opinions, aims to agree on the initially most frequent one.
In this setting, h-majority is arguably the simplest and most studied protocol, in which each agent samples the opinion of h neighbors uniformly at random and updates its opinion to the most frequent value in the sample.
We propose a new, extremely simple mechanism called D\'ej\`aVu: an agent queries neighbors until it encounters an opinion for the second time, at which point it updates its own opinion to the duplicate value. This rule does not require agents to maintain counters or estimate frequencies, nor to choose any parameter (such as a sample size h); it relies solely on the primitive ability to detect repetition.
We provide a rigorous analysis of D\'ej\`aVu that relies on several technical ideas of independent interest and demonstrates that it is competitive with h-majority and, in some regimes, substantially more communication-efficient, thus yielding a powerful primitive for plurality consensus.
