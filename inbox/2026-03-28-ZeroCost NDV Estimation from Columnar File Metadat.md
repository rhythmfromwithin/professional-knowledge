---
interest: medium
link: https://arxiv.org/abs/2603.24606
next_step: skim
priority: low
slack_ts: '1774927066.217299'
source: cs.DB - Databases
status: unread
title: Zero-Cost NDV Estimation from Columnar File Metadata
---
# Zero-Cost NDV Estimation from Columnar File Metadata
> 原文: [https://arxiv.org/abs/2603.24606](https://arxiv.org/abs/2603.24606)

arXiv:2603.24606v1 Announce Type: new
Abstract: We present a method for estimating the number of distinct values (NDV) of a column in columnar file formats, using only existing file metadata--no extra storage, no data access. Two complementary signals are exploited: (1)~inverting the dictionary-encoded storage size equation yields accurate NDV estimates when distinct values are well-spread across row groups; (2)~counting distinct min/max values across row groups and inverting a coupon collector model provides robust estimates for sorted or partitioned data. A lightweight distribution detector routes between the two estimators. While demonstrated on Apache Parquet, the technique generalizes to any format with dictionary encoding and partition-level statistics, such as ORC and F3. Applications include cost-based query optimization, GPU memory allocation, and data profiling.
