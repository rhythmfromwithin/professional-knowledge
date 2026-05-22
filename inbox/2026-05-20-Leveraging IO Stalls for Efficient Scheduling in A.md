---
interest: medium
link: https://arxiv.org/abs/2605.19335
next_step: skim
priority: low
slack_ts: '1779423487.717229'
source: cs.DB - Databases
status: unread
title: Leveraging I/O Stalls for Efficient Scheduling in ANNS
---
# Leveraging I/O Stalls for Efficient Scheduling in ANNS
> 原文: [https://arxiv.org/abs/2605.19335](https://arxiv.org/abs/2605.19335)

arXiv:2605.19335v1 Announce Type: new
Abstract: Disk-based graph indexes for approximate nearest neighbor search (ANNS) must serve latency-sensitive queries and throughput-demanding updates concurrently. We observe that over 40% of search-thread CPU time is spent stalling on disk I/O; such idle cycles are invisible to thread-level scheduling yet available for other work. We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows. LIOS introduces three techniques: (i) splitting each update into resumable subtasks small enough to fit within a single stall window; (ii) bounding the expected overrun of update subtasks to a given threshold; and (iii) dynamically adjusting the fraction of idle time devoted to updates to drive end-to-end search latency degradation toward a user-specified target. We integrate LIOS into two update-optimized ANNS systems, FreshDiskANN and OdinANN. LIOS achieves speedups of up to 2.68$\times$ in insertion and 2.18$\times$ in deletion, with search latency degradation maintained near the user-specified target.
