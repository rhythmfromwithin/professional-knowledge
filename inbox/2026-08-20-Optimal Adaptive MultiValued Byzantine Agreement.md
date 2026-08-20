---
interest: medium
link: https://arxiv.org/abs/2608.17552
next_step: skim
priority: medium
slack_ts: '1787190046.387419'
source: cs.DC - Distributed Computing
status: unread
title: Optimal Adaptive Multi-Valued Byzantine Agreement
---
# Optimal Adaptive Multi-Valued Byzantine Agreement
> 原文: [https://arxiv.org/abs/2608.17552](https://arxiv.org/abs/2608.17552)

arXiv:2608.17552v1 Announce Type: new
Abstract: In Byzantine Agreement (BA), $n$ parties, out of which $t$ can be Byzantine, run a distributed protocol to agree on a common valid input. Traditionally, these protocols have a linear latency and quadratic message complexity, making them impractical at a large scale. In their recent work, Constantinescu, Dufay, Paramonov, and Wattenhofer consider the actual number of byzantine parties $f \leq t$ and work toward decoupling the dependency on $n$ and $t$ in the complexity. They obtain a BA protocol with $\tilde{\mathcal{O}}(n + t\cdot f)$ message complexity and $\tilde{\mathcal{O}}(f)$ round complexity.
However, their results are strictly limited to agreement on a binary value. Using the framework given by their work along with novel techniques, we extend these results for BA on an $L$-bit value. With $\kappa$ being a security parameter, and with optimal resiliency ($t < n/2$ in the synchronous setting or $t < n/3$ otherwise), we obtain:
- In synchrony, a deterministic protocol with $\mathcal{O}(n\cdot (L + f \cdot \kappa ))$ bit complexity and $\mathcal{O}(f + \log n)$ round complexity.
- In synchrony and partial synchrony, deterministic protocols with $\tilde{\mathcal{O}}(n \cdot \kappa + t\cdot (L + f \cdot \kappa))$ bit complexity and $\mathcal{O}(f)$ round complexity.
- In asynchrony, a protocol with $\tilde{\mathcal{O}}(n \cdot \kappa + t\cdot(L + t \cdot \kappa))$ expected bit complexity and expected $\mathcal{O}(1)$ latency.
