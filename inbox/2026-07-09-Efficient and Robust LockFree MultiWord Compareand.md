---
interest: medium
link: https://arxiv.org/abs/2607.06034
next_step: skim
priority: low
slack_ts: '1783569528.405169'
source: cs.DB - Databases
status: unread
title: Efficient and Robust Lock-Free Multi-Word Compare-and-Swap via Contention-Aware
  Helping
---
# Efficient and Robust Lock-Free Multi-Word Compare-and-Swap via Contention-Aware Helping
> 原文: [https://arxiv.org/abs/2607.06034](https://arxiv.org/abs/2607.06034)

arXiv:2607.06034v1 Announce Type: new
Abstract: Efficient concurrent access to shared memory remains a central focus for researchers seeking to enhance data structure performance. Lock-based synchronization often limits scalability and introduces liveness issues such as deadlocks. In contrast, implementing non-blocking structures with single-word compare-and-swap (CAS) instructions increases algorithmic complexity because of unavoidable intermediate states. Multi-word compare-and-swap (MCAS) operations offer a practical primitive for atomically updating multiple discrete memory locations, thereby addressing these challenges. However, under high contention, helping mechanisms designed to guarantee lock-freedom may cause excessive cache invalidations and significant performance degradation. Furthermore, existing approaches are vulnerable to the ABA problem. Current lock-free MCAS algorithms may duplicate the execution of the same operation, leading to inconsistent states in certain edge cases. To address these challenges, this paper introduces a new lock-free MCAS algorithm that achieves both efficiency and consistency. First, we propose a contention-aware helping mechanism that dynamically regulates the number of concurrent helpers through exponential backoff and embedded entry counters. These counters also enable a fast garbage-collection path, significantly reducing memory management overhead. Second, we introduce a version embedding approach to suppress the ABA problem during MCAS operations. Although version embedding requires several bits per target memory region to store version information, embedded versions allow helpers to avoid duplicated MCAS executions. Experimental results show that the proposed method achieves up to three times the throughput of the state-of-the-art lock-free MCAS algorithm. Moreover, the results indicate that version embedding is sufficient to prevent the ABA problem in practical scenarios.
