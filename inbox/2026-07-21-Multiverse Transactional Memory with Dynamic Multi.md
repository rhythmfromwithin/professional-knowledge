---
interest: medium
link: https://arxiv.org/abs/2601.09735
next_step: skim
priority: low
slack_ts: '1784690754.334589'
source: cs.DB - Databases
status: unread
title: 'Multiverse: Transactional Memory with Dynamic Multiversioning'
---
# Multiverse: Transactional Memory with Dynamic Multiversioning
> 原文: [https://arxiv.org/abs/2601.09735](https://arxiv.org/abs/2601.09735)

arXiv:2601.09735v5 Announce Type: replace
Abstract: Software transactional memory (STM) allows programmers to easily implement concurrent data structures. STMs simplify atomicity. Recent STMs can achieve good performance for some workloads but they have some limitations. In particular, STMs typically cannot support long-running reads which access a large number of addresses that are frequently updated. Multiversioning is a common approach used to support this type of workload. However, multiversioning is often expensive and can reduce the performance of transactions where versioning is not necessary. In this work we present Multiverse, a new STM that combines the best of both unversioned TM and multiversioning. Multiverse features versioned and unversioned transactions which can execute concurrently. A main goal of Multiverse is to ensure that unversioned transactions achieve performance comparable to the state of the art unversioned STM while still supporting fast versioned transactions needed to enable long running reads. We implement Multiverse and compare it against several STMs. Our experiments demonstrate that Multiverse achieves comparable or better performance for common case workloads where there are no long running reads. For workloads with long running reads and frequent updates Multiverse significantly outperforms existing STMS. In several cases for these workloads the throughput of Multiverse is several orders of magnitude faster than other STMs.
