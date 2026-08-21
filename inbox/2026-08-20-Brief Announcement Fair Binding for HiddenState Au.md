---
interest: medium
link: https://arxiv.org/abs/2608.17349
next_step: skim
priority: medium
slack_ts: '1787276737.491789'
source: cs.DC - Distributed Computing
status: unread
title: 'Brief Announcement: Fair Binding for Hidden-State Authorization in Byzantine
  SMR'
---
# Brief Announcement: Fair Binding for Hidden-State Authorization in Byzantine SMR
> 原文: [https://arxiv.org/abs/2608.17349](https://arxiv.org/abs/2608.17349)

arXiv:2608.17349v1 Announce Type: new
Abstract: Validated Byzantine SMR assumes that replicas can evaluate the validity of an ordered command. Agent authorization creates a different regime: a command may be valid only relative to a committed policy state that validators cannot reconstruct from the log. A proof that an action was authorized at an old commitment is then only a historical attestation, it does not by itself reserve the hidden resource for later use.
We isolate two independent requirements for safe live allocation of a hidden consumable resource under a Byzantine leader. First, arrival order at correct replicas must constrain commit order, the gap addressed by fair-ordering protocols. Second, a committed first request must bind later validity: it must make conflicting later requests invalid, not merely record that the first request was once authorized. The second requirement is non-vacuous precisely because the current policy state is hidden and not prefix-recoverable. Using an explicit authorization-witness interface, we characterize the two distinct obligations in this one-shot reservation model and give a fair reserve/use protocol satisfying both authorization safety and first-arrival liveness. Under trusted FIFO admission the two requirements collapse because admission and execution are atomic, Byzantine SMR separates request commitment from use.
