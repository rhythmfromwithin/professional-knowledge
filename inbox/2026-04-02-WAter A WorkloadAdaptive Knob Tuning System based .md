---
interest: medium
link: https://arxiv.org/abs/2603.28809
next_step: skim
priority: low
slack_ts: '1775098546.166099'
source: cs.DB - Databases
status: unread
title: 'WAter: A Workload-Adaptive Knob Tuning System based on Workload Compression'
---
# WAter: A Workload-Adaptive Knob Tuning System based on Workload Compression
> 原文: [https://arxiv.org/abs/2603.28809](https://arxiv.org/abs/2603.28809)

arXiv:2603.28809v1 Announce Type: new
Abstract: Selecting appropriate values for the configurable parameters of Database Management Systems (DBMS) to improve performance is a significant challenge. Recent machine learning (ML)-based tuning systems have shown strong potential, but their practical adoption is often limited by the high tuning cost. This cost arises from two main factors: (1) the system needs to evaluate a large number of configurations to identify a satisfactory one, and (2) for each configuration, the system must execute the entire target workload on the DBMS, which is both time-consuming. Existing studies have primarily addressed the first factor by improving sample efficiency, that is, by reducing the number of configurations evaluated. However, the second factor, improving runtime efficiency by reducing the time required for each evaluation, has received limited attention and remains an underexplored direction.
We develop WAter, a runtime-efficient and workload-adaptive tuning system that finds near-optimal configurations at a fraction of the tuning cost compared with state-of-the-art methods. We divide the tuning process into multiple time slices and evaluate only a small subset of queries from the workload in each slice. Different subsets are evaluated across slices, and a runtime profile is used to dynamically identify more representative subsets for evaluation in subsequent slices. At the end of each time slice, the most promising configurations are evaluated on the original workload to measure their actual performance. Evaluations demonstrate that WAter identifies the best-performing configurations with up to 73.5% less tuning time and achieves up to 16.2% higher performance than the best-performing alternative.
