---
interest: medium
link: https://arxiv.org/abs/2606.27979
next_step: skim
priority: low
slack_ts: '1782708421.812029'
source: cs.DB - Databases
status: unread
title: 'DiStash: A Disaggregated Multi-Stash Transactional Key-Value Store'
---
# DiStash: A Disaggregated Multi-Stash Transactional Key-Value Store
> 原文: [https://arxiv.org/abs/2606.27979](https://arxiv.org/abs/2606.27979)

arXiv:2606.27979v1 Announce Type: new
Abstract: A stash is a storage medium such as Dynamic Random Access Memory (DRAM), Solid State Disk (SSD), Hard Disk Drive (HDD), or Non-Volatile Memory (NVM). This paper presents a disaggregated transactional key-value (KV) store, DiStash, that governs KVs cross pools of stash types. It enables an application to use a single transaction to read and write different copies of one or more key-value pair across the different pools of stashes. It simplifies the application logic by (a) preventing undesirable race conditions that may cause copies of data across different stash pools to reflect different values and/or (b) failures that may result in loss of key-value pairs. A configuration of DiStash may use a pool of stashes as either ephemeral or durable storage. The application dictates whether the content of its participating stashes are inclusive (replicated) or exclusive (tiered). We implement a DiStash by extending FoundationDB. We quantify the tradeoffs with its design decisions using microbenchmarks and eBay's production workload. We open source our implementation at https://github.com/ebay-USC/DiStash.
