---
interest: medium
link: https://arxiv.org/abs/2607.01486
next_step: skim
priority: medium
slack_ts: '1783136975.273669'
source: cs.DC - Distributed Computing
status: unread
title: 'SLFS: a Flexible, Low-Cost Distributed File System Using Serverless Designs'
---
# SLFS: a Flexible, Low-Cost Distributed File System Using Serverless Designs
> 原文: [https://arxiv.org/abs/2607.01486](https://arxiv.org/abs/2607.01486)

arXiv:2607.01486v1 Announce Type: new
Abstract: Large-scale distributed file systems must provision resources for peak demand, yet file access patterns fluctuate significantly, leaving substantial capacity idle during off-peak periods. Existing scaling mechanisms operate at the granularity of entire servers and take minutes to hours, making them unable to track the rapid, fine-grained load variations that file systems commonly experience. Serverless computing, with its millisecond-granularity elasticity and pay-per-use pricing, offers a compelling alternative. We present SLFS, the first distributed file system built with serverless functions for both data and metadata operations. SLFS implements file services on top of key-value stores, keeping function operations simple and short, and introduces a novel multi-threaded, short-lived server design that overcomes the cold-start problem while maintaining low cost. A policy-enforcing coordinator efficiently maps files to function instances, scales the system elastically, and controls function lifetimes to balance performance and cost. SLFS can flexibly run on diverse storage backends -- from cloud-native services like S3 to user-managed key-value stores -- enabling configurable cost-performance trade-offs. Our evaluation shows that SLFS mitigates cold starts by 580$\times$ compared to the base serverless design and outperforms $\lambda$FS, EFS, and Ceph at up to 63%, 68%, and 63% lower cost, respectively.
