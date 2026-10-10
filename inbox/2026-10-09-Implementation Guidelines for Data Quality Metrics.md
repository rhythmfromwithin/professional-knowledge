---
interest: medium
link: https://arxiv.org/abs/2610.10919
next_step: skim
priority: low
slack_ts: '1791610141.692029'
source: cs.DB - Databases
status: unread
title: Implementation Guidelines for Data Quality Metrics
---
# Implementation Guidelines for Data Quality Metrics
> 原文: [https://arxiv.org/abs/2610.10919](https://arxiv.org/abs/2610.10919)

arXiv:2610.10919v1 Announce Type: new
Abstract: Despite decades of data quality (DQ) research, a gap remains between DQ dimensions, such as accuracy or completeness, which the literature defines in textual form, and DQ tools, which typically implement low-level checks that are not aligned with these dimensions. ISO/IEC 25024 and ISO/IEC 5259 attempt to bridge this gap by defining DQ metrics for each dimension. However, these DQ metrics are hardly used, because the standards leave open how to implement them: for example, the metric for syntactic accuracy counts syntactically accurate values, but does not state how to decide that a value is syntactically accurate. This simply moves the problem to another level without solving it. As a result, DQ assessment currently cannot build on the standards.
In this paper, we make the ISO DQ metrics executable. We classify all data-level metrics of both standards into (i) generalizable metrics that need no input beyond the data, (ii) parameterized metrics whose parameters can be learned from clean reference data or set by an expert, and (iii) non-generalizable metrics that need qualitative judgment and cannot be automated. For the metrics that can be automated, i.e., categories (i) and (ii), we propose implementation guidelines that resolve what the standards leave open. We realize the guidelines in dqmeasure, an open-source library of 20 metrics that learns these parameters from reference data instead of relying on manually defined rules. Our experiments on real-world and synthetic datasets show that the metric scores decrease monotonically with an increasing number of injected errors, decline together with downstream ML performance, and scale linearly with the number of rows, which enables automated DQ monitoring based on the standards.
