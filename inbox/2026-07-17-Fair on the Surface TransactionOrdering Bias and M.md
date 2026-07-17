---
title: "Fair on the Surface: Transaction-Ordering Bias and MEV in Mysticeti DAG-based BFT Protocol"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.13378
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fair on the Surface: Transaction-Ordering Bias and MEV in Mysticeti DAG-based BFT Protocol
> 原文: [https://arxiv.org/abs/2607.13378](https://arxiv.org/abs/2607.13378)

arXiv:2607.13378v1 Announce Type: new
Abstract: Distributed systems deployed in untrustworthy environments agree on a common transaction order through Byzantine fault-tolerant (BFT) consensus protocols, and that order has real financial value in many decentralized applications: whoever influences it can profit at other users' expense, a problem known as maximal extractable value (MEV). Mysticeti is a state-of-the-art DAG-based BFT protocol in which many validators propose blocks in parallel, and the total order is derived from the resulting DAG afterward. Mysticeti is the consensus protocol powering Sui, a production blockchain with a market capitalization of roughly $3 billion, and it is widely believed to order transactions fairly, since many validators propose blocks in parallel and committed transactions are re-sorted by gas price before execution. We show this fairness assumption breaks down in practice, and the effect is already present on Sui's live network. First, when vertices of the committed graph are merged into a single total order, blocks from the same round are sorted by validator index, giving lower-indexed validators a permanent head start. In our evaluation on a 13-validator network with no attacker, the lower-indexed side wins same-round ordering about 89% of the time. Second, the gas-price re-sort intended to remove this bias uses a stable sort, so transactions paying equal fees (common at the reference gas price) retain the original biased order, letting an attacker profit without paying extra. Third, a validator can amplify this advantage by choosing when to stay silent, a fully legitimate action that violates no protocol rule; this raises its ordering win rate above 94%. We measure all three exploitations, verify that Mysticeti otherwise remains resilient below the standard Byzantine fault threshold, and propose a simple fix: replace the validator-index tiebreaker with an unpredictable, per-commit random key.
