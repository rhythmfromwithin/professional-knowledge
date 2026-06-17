---
interest: medium
link: https://arxiv.org/abs/2606.18187
next_step: skim
priority: low
slack_ts: '1781672192.001719'
source: cs.DB - Databases
status: unread
title: 'Group Commit Self-Clocks: Why Tuning Is Unnecessary Above a Device-Set Load
  Threshold'
---
# Group Commit Self-Clocks: Why Tuning Is Unnecessary Above a Device-Set Load Threshold
> 原文: [https://arxiv.org/abs/2606.18187](https://arxiv.org/abs/2606.18187)

arXiv:2606.18187v1 Announce Type: new
Abstract: Group commit amortizes the fixed cost of a durable log flush across many committing transactions; the release rule - a timer, a batch size, or an adaptive policy - is a classic tuning knob. The textbook theory is open-loop: for Poisson arrivals the optimal timer is the EOQ square-root rule, and the wait-or-flush decision is ski-rental 2-competitive. We ask when that tuning is worth its machinery, and show that in closed-loop OLTP it usually is not. Real commit arrivals are closed-loop: a client issues its next transaction only after its last commits, so the arrival rate is induced by the policy's own latency. Modeling this as a closed queueing network, the parameter-free greedy-pipelined policy (flush the instant the device is free) self-clocks to a computable fixed point and is within about 0.1% of the best oracle-tuned timer at every load. The square-root rule prescribes waiting $T^\star=\sqrt{2F\_0/\lambda}$, but $T^\star\lambda^\star=2/F\_0$; above this device-set load threshold the timer collapses onto greedy and tuning is vacuous. The clean theory only bites below $\lambda^\star$ and in the open-loop world, where a parameter-free ski policy still beats a fixed tuned timer under rate shifts. We instantiate $\lambda^\star$ with measured fsync distributions on two AWS storage classes (EBS gp3 versus instance NVMe, a $25\times$ range), and confirm on PostgreSQL that commit\_delay=0 is competitive with any tuned value. The contribution is a characterization that explains deployed practice; we add no new logger.
