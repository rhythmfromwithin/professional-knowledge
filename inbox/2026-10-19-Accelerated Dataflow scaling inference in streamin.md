---
interest: medium
link: https://arxiv.org/abs/2610.22731
next_step: skim
priority: medium
slack_ts: '1792383438.571729'
source: cs.DC - Distributed Computing
status: unread
title: 'Accelerated Dataflow: scaling inference in streaming data analytics with efficiency'
---
# Accelerated Dataflow: scaling inference in streaming data analytics with efficiency
> 原文: [https://arxiv.org/abs/2610.22731](https://arxiv.org/abs/2610.22731)

arXiv:2610.22731v1 Announce Type: new
Abstract: Streaming data analytics helps businesses identify opportunities and spot risks in a timely fashion. As large language model (LLM) usage grows, people are exploring incorporating agents or LLMs in streaming data pipelines to help find patterns in datasets without supervision or interpret natural languages for content moderation. However, most streaming systems are currently optimized for data movement and perform poorly on GPU intensive workloads such as performing inference with LLMs. We introduce a system on Google Cloud Dataflow designed to tackle hybrid streaming machine learning workloads with co-designed autoscaling on heterogeneous worker pools and prefix-aware batching. This increases throughput 1.5x to 2x for streaming pipelines using LLMs while maintaining similar latency with up to 75% peak resource savings and 84% lower peak tail latency compared with existing streaming data processing systems.
