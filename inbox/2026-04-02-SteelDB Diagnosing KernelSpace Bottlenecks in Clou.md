---
interest: medium
link: https://arxiv.org/abs/2603.29052
next_step: skim
priority: low
slack_ts: '1775270894.548449'
source: cs.DB - Databases
status: unread
title: 'SteelDB: Diagnosing Kernel-Space Bottlenecks in Cloud OLTP Databases'
---
# SteelDB: Diagnosing Kernel-Space Bottlenecks in Cloud OLTP Databases
> 原文: [https://arxiv.org/abs/2603.29052](https://arxiv.org/abs/2603.29052)

arXiv:2603.29052v1 Announce Type: new
Abstract: Modern cloud OLTP databases have sought performance primarily through user-space optimization - separating storage and compute layers, or distributing transactions across multiple nodes using consensus algorithms. This paper turns attention to a previously unexplored layer: kernel-space I/O behavior. From an on-premises perspective, where a single server with local storage delivers excellent performance, these elaborate designs seem puzzling. Why do cloud databases require such architectural complexity? We investigate this through a pathological analysis of databases that rely on OS-level I/O control in cloud-specific storage environments. We show that bottlenecks widely attributed to network or storage architectures in fact originate in kernel-space I/O behavior. Based on this diagnosis, we derive treatment principles and realize them as SteelDB, a zero-patch architecture that improves database performance on general-purpose cloud distributed block storage through strategic I/O optimization without requiring kernel or database patches. TPC-C evaluations demonstrate that SteelDB achieves up to 9x performance improvement at no additional cost. Against Amazon Aurora, SteelDB achieved 3.1x higher performance while reducing costs by 58%, leading to a 7.3x improvement in cost efficiency. While Aurora requires an average of 254 days for major version upgrades due to applying proprietary patches to newly released OSS databases, our zero-patch architecture reduces these software maintenance costs to near zero.
