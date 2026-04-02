---
interest: medium
link: https://arxiv.org/abs/2603.26758
next_step: skim
priority: medium
slack_ts: '1775098518.284479'
source: cs.DC - Distributed Computing
status: unread
title: A Density-Delay Law for Stable Event-Driven State Progression in Open Distributed
  Systems
---
# A Density-Delay Law for Stable Event-Driven State Progression in Open Distributed Systems
> 原文: [https://arxiv.org/abs/2603.26758](https://arxiv.org/abs/2603.26758)

arXiv:2603.26758v1 Announce Type: new
Abstract: Distributed systems in which concurrent proposals are mutually exclusive face a fundamental stability constraint under network delay. In open systems where global state progression is event-driven rather than round-driven, propagation delay creates a conflict window within which overlapping proposals may generate competing branches. This paper derives a density-delay law for such exclusive state progression processes. Under independent proposal arrivals and bounded propagation delay, overlap is approximated by a Poisson model and fork depth is represented by a birth-death process. The analysis shows that maintaining bounded fork depth as the number of participants grows requires the density-delay product $\lambda \Delta$ to remain $O(1)$, implying that aggregate proposal intensity must stay bounded and yielding an inverse-scaling law $g(N)=O(1/N)$ at the unit level. Simulation experiments across varying network sizes and propagation delays align with a common density-delay curve, supporting the predicted scaling behavior. The result provides a compact law for stable event-driven state progression in open distributed systems and offers a scaling-based interpretation of Bitcoin-style difficulty adjustment as a decentralized way to regulate effective event density.
