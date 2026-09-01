---
interest: medium
link: https://arxiv.org/abs/2608.29103
next_step: skim
priority: medium
slack_ts: '1788237864.717379'
source: cs.DC - Distributed Computing
status: unread
title: 'CLASP: Chained-Request-Aware Scaling and Operator Placement for Serverless
  Stream Processing'
---
# CLASP: Chained-Request-Aware Scaling and Operator Placement for Serverless Stream Processing
> 原文: [https://arxiv.org/abs/2608.29103](https://arxiv.org/abs/2608.29103)

arXiv:2608.29103v1 Announce Type: new
Abstract: Stateful serverless (Function-as-a-Service) environments, whose workers host state servers, are increasingly used for stream processing. A stream application is a pipeline of operators, where each operator forwards intermediate data downstream through a chained request. As input rates fluctuate, the system should adjust operator parallelism and place instances across workers to sustain the incoming rate. Existing approaches do so without fully accounting for chained-request overhead, leading them to misestimate the required number of workers. Too few leave the cluster unable to keep up with the input rate, while too many route a larger fraction of chained requests across worker boundaries, increasing end-to-end latency.
We propose CLASP, a scaling and scheduling strategy for stream processing in stateful serverless environments. At runtime, CLASP estimates execution cost and chained-request cost from observed metrics. Under a capacity model that covers the two costs, it adjusts operator parallelism and packs operators onto the fewest workers that can sustain the target input rate. Once a scaling decision is made, CLASP migrates each operator's state together with its instances, thereby minimizing execution pause time. Experiments show that CLASP improves throughput by up to 3.3x and reduces median end-to-end latency by up to 76% compared with state-of-the-art scaling strategies.
