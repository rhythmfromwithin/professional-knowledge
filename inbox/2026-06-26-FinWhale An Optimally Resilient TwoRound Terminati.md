---
interest: medium
link: https://arxiv.org/abs/2606.26292
next_step: skim
priority: medium
slack_ts: '1782447547.433809'
source: cs.DC - Distributed Computing
status: unread
title: 'FinWhale: An Optimally Resilient Two-Round Terminating DAG Protocol'
---
# FinWhale: An Optimally Resilient Two-Round Terminating DAG Protocol
> 原文: [https://arxiv.org/abs/2606.26292](https://arxiv.org/abs/2606.26292)

arXiv:2606.26292v1 Announce Type: new
Abstract: DAG based Byzantine Fault Tolerant protocols provide high throughput consensus under partial synchrony but existing DAG protocols still require at least three message delays to commit decisions. In contrast fast path Byzantine Fault Tolerant protocols can achieve optimal two message delay termination under favorable conditions though they do not naturally extend to DAGs.
We present FinWhale the first DAG based Byzantine Fault Tolerant protocol with a two message delay fast path. FinWhale extends Mysticeti with a novel fast path commit mechanism that safely coexists with the protocol's original slow path rules. To preserve safety across different local DAG views we introduce new commit structures based on fast path evidence blocks enabling validators to combine fast path and slow path reasoning consistently.
FinWhale operates in the partially synchronous model with n equals three f plus two p minus one validators matching the known lower bound for fast Byzantine consensus. The protocol tolerates up to f Byzantine faults and achieves fast termination whenever at most p validators fail during the fast path where p is between one and f. Our results show that optimal latency fast paths can be integrated into uncertified DAG consensus protocols.
