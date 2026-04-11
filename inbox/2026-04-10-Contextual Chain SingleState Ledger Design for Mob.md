---
interest: medium
link: https://arxiv.org/abs/2604.06529
next_step: skim
priority: medium
slack_ts: '1775875949.843599'
source: cs.DC - Distributed Computing
status: unread
title: 'Contextual Chain: Single-State Ledger Design for Mobile/IoT Networks with
  Frequent Partitions'
---
# Contextual Chain: Single-State Ledger Design for Mobile/IoT Networks with Frequent Partitions
> 原文: [https://arxiv.org/abs/2604.06529](https://arxiv.org/abs/2604.06529)

arXiv:2604.06529v1 Announce Type: new
Abstract: We study a lightweight ledger protocol for intermittent and noisy networks, motivated by IoT and mobile settings in which partitions are common and full-history verification is impractical. Our design centers on an \emph{operational} notion of \textbf{contextual authentication}: each node decides whether a chain extension is acceptable in its current local context, using checkpoint-first fork choice, a local branch score derived from recent proposer behavior, and an inconsistency-driven \emph{quarantine} signal. To improve recovery after partitions, we combine this acceptance rule with \textbf{adaptive synchronization}, which increases gossip effort only when inconsistency becomes prevalent.
We evaluate the protocol with a discrete-event simulator under controlled partitions and two network regimes (clean and noisy). Across 500 seeds at $N=20$, the main result is that quarantine alone does not materially improve agreement or recovery under noisy conditions, whereas increased synchronization (\texttt{Gossip\\_only} and \texttt{Both}) substantially improves both final agreement probability and recovery-time tails after partition rejoin. Longer-horizon experiments show that low-synchronization failures are not removed simply by waiting longer, and scaling experiments at $N=50$ and $N=100$ show that parameters that work at small scale do not automatically generalize. These results indicate that, under noisy partition/rejoin dynamics, recovery in the current design is limited primarily by information availability, making synchronization policy a first-class design problem.
