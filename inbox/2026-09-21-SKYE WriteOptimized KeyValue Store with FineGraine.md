---
title: "SKYE: Write-Optimized Key-Value Store with Fine-Grained Control over Persistent Memory Accesses"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2609.20972
priority: low
status: unread
interest: medium
next_step: skim
---
# SKYE: Write-Optimized Key-Value Store with Fine-Grained Control over Persistent Memory Accesses
> 原文: [https://arxiv.org/abs/2609.20972](https://arxiv.org/abs/2609.20972)

arXiv:2609.20972v1 Announce Type: new
Abstract: State-of-the-art key-value stores built for persistent memory (PM) provide low latency as they allow application threads to directly access the data on PM and rely on hardware to manage multiple non-volatile DIMMs (NVDIMMs). While this provides low latency, it results in low throughput and scalability. Performance degrades because PM hardware requires fine-grained control over PM accesses; for example, throughput degrades if too many threads write to PM concurrently.
We present SKYE, a write-optimized PM key-value store that achieves high throughput and scalability. SKYE builds on the central idea of maintaining fine-grained control over all PM accesses and obtains high PM write-bandwidth utilization. To achieve this, SKYE deviates from current practice and provides indirect access to applications; applications send requests to SKYE, which uses dedicated threads to access PM on their behalf. Instead of relying on hardware-managed PM, SKYE controls how data is placed on individual NVDIMMs. SKYE leverages multiple media to avoid overloading PM and limits remote NUMA accesses for scalable throughput. We show that on a single NVDIMM, SKYE outperforms state-of-the-art PM stores by 2.5-5x on the standard Yahoo Cloud Serving Benchmark (YCSB). With four NVDIMMs across four NUMA nodes, SKYE obtains about 86% of PM write bandwidth, and its write throughput scales by 3.9x.
