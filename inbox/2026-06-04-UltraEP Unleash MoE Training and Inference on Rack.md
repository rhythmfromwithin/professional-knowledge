---
interest: medium
link: https://arxiv.org/abs/2606.04101
next_step: skim
priority: medium
slack_ts: '1780548680.323319'
source: cs.DC - Distributed Computing
status: unread
title: 'UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal
  Load Balancing'
---
# UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing
> 原文: [https://arxiv.org/abs/2606.04101](https://arxiv.org/abs/2606.04101)

arXiv:2606.04101v1 Announce Type: new
Abstract: Large-scale expert parallelism (EP) is becoming pivotal for training and serving frontier MoE models, but it also amplifies device-level expert load imbalance into compute stragglers, token all-to-all bottlenecks, and activation-memory spikes. Existing balancers redistribute experts periodically based on historical load, which becomes unreliable for production deployments with non-stationary load patterns.
We present UltraEP, the first exact-load, real-time balancer for large-EP MoE training and serving prefill on rack-scale nodes (RSNs). Built upon the extended scale-up connectivity of RSNs, UltraEP rebalances every microbatch and layer on critical paths, which requires nontrivial co-design of plan solving and expert replication communication to minimize exposed overhead. To this end, UltraEP eagerly reacts to post-gating load with efficient quota-driven planning, and executes the resulting irregular expert-state transfers with RSN-native persistent tile streaming and relay-based fan-out mitigation. Averaged across MoE models from 106B to 671B parameters in training and prefill, UltraEP achieves 94.3% of the force-balanced ideal throughput, delivering 1.49$\times$ improvement over non-balancing, while reducing the final inter-rank imbalance from 1.30$-$4.01 to 1.01$-$1.04. Additionally, we validate UltraEP's scalability and robustness in production MoE training with 2560 GPUs.
