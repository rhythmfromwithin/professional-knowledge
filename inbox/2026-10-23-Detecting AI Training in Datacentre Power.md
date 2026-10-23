---
title: "Detecting AI Training in Datacentre Power"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.30182
priority: low
status: unread
interest: medium
next_step: skim
---
# Detecting AI Training in Datacentre Power
> 原文: [https://arxiv.org/abs/2610.30182](https://arxiv.org/abs/2610.30182)

arXiv:2610.30182v1 Announce Type: new
Abstract: AI governance agreements require methods to detect large model training runs on a monitored computing cluster, without trusting the operator. We develop a method to detect synchronous model training in facility-level power by Viterbi tracking of the wandering iteration cadence. On simulated datacentre power, when the operator makes no attempt to hide, the Viterbi tracker detects at least $96\%$ of training runs against a declared inference workload, at a $1\%$ false-alarm rate and within $0.04$ of the Neyman--Pearson optimum, given a meter that samples at $2$ Hz or faster. Of eight adversarial strategies an operator might use to hide, only extreme variation of the work per iteration evades the tracker. Its strongest form hides training in up to $73\%$ of five-minute observations, but over a day at least $87\%$ of such runs are still caught, at a $0.1\%$ false-alarm rate per run. This adversarial strategy costs no throughput, but in small-scale training the operator needs $93$--$267\%$ more compute to reach the same loss. A modest passive meter is sufficient to make hidden training both detectable and expensive, which makes power metering a promising part of compute verification that does not depend on trusting the operator.
