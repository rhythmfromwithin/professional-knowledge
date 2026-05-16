---
interest: medium
link: https://arxiv.org/abs/2605.14015
next_step: skim
priority: medium
slack_ts: '1778903342.263499'
source: cs.DC - Distributed Computing
status: unread
title: Distributed Statistical Zero-Knowledge Proofs via Sumcheck
---
# Distributed Statistical Zero-Knowledge Proofs via Sumcheck
> 原文: [https://arxiv.org/abs/2605.14015](https://arxiv.org/abs/2605.14015)

arXiv:2605.14015v1 Announce Type: new
Abstract: We study distributed zero-knowledge proofs, introduced by Bick, Kol, and Oshman (SODA 2022). While distributed interactive proofs have advanced rapidly, general-purpose techniques for distributed zero-knowledge remain limited and mostly problem-specific. We address this gap by introducing distributed statistical zero-knowledge, requiring that each node's view be simulatable within negligible statistical distance, and by lifting the classical Sumcheck protocol (Lund, Fortnow, Karloff, and Nisan, FOCS 1990) into a modular primitive for distributed zero-knowledge proofs.
Our main contribution is a distributed zero-knowledge implementation of Sumcheck. Given oracle access to a polynomial F over a finite field $\mathbb{F}$ with N variables, we design a protocol verifying claims of the form $\sum\_{x\in\mathbb{F}} F(x)=a$ using $O(N)$ rounds of $O(\log |\mathbb{F}|)$-bit messages, while achieving statistical zero-knowledge and small soundness error.
We apply this primitive to two problems. For non-k-colorability, we obtain an $O(n)$-round distributed statistical zero-knowledge proof deciding whether a graph is not k-colorable, for any constant k, using $O(log^{1+o(1)} n)$-bit messages. This is the first nontrivial distributed interactive proof for this problem, even without zero-knowledge guarantees. For Subgraph Counting, we obtain an $O(k \log n)$-round, $O(k \log n)$-bit distributed statistical zero-knowledge proof for counting copies of a given k-node pattern, improving previous distributed interactive proofs while additionally providing statistical zero-knowledge. Finally, we show that additional round compression of Sumcheck is problem-dependent: for non-3-colorability on constant-degree graphs, we prove a lower bound excluding $o(n/\log n)$ rounds under polynomial-time local computation.
