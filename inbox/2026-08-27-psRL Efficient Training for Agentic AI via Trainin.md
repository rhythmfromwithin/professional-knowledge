---
interest: medium
link: https://arxiv.org/abs/2608.25683
next_step: skim
priority: medium
slack_ts: '1787914970.682559'
source: cs.DC - Distributed Computing
status: unread
title: 'psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing'
---
# psRL: Efficient Training for Agentic AI via Training-Time Prefix Sharing
> 原文: [https://arxiv.org/abs/2608.25683](https://arxiv.org/abs/2608.25683)

arXiv:2608.25683v1 Announce Type: new
Abstract: In modern agentic AI training, the system bottleneck is shifting from rollout to update. Emerging sampling strategies such as tree-structured and step-wise RL greatly increase training sample volume while incurring relatively low marginal rollout cost, causing the update phase to dominate the end-to-end execution time. Crucially, this shift exposes a new optimization opportunity, as production traces reveal substantial prefix redundancy across training samples. In this paper, we propose psRL (prefix sharing for RL), a new training system for agentic AI designed to exploit prefix redundancy among training samples. Leveraging the global visibility and data immutability inherent to the update phase, psRL achieves efficient workload scheduling and memory management for distributed training. Specifically, psRL introduces two novel prefix-sharing mechanisms that enable flexible, fine-grained workload distribution across GPU workers, simultaneously optimizing prefix reuse and achieving load balancing. Moreover, psRL implements a new underlying KV cache manager that facilitates adaptable block-size allocation and dynamic KV caching, maximizing memory utilization while maintaining a high prefix hit rate. Evaluations using production traces demonstrate that psRL outperforms existing systems by up to 5.2x in throughput. The source code will be publicly available soon.
