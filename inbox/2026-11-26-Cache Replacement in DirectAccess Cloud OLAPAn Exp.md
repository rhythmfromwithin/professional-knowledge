---
title: "Cache Replacement in Direct-Access Cloud OLAP-An Experimental Comparison and Practical Guidance"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2611.33977
priority: low
status: unread
interest: medium
next_step: skim
---
# Cache Replacement in Direct-Access Cloud OLAP-An Experimental Comparison and Practical Guidance
> 原文: [https://arxiv.org/abs/2611.33977](https://arxiv.org/abs/2611.33977)

arXiv:2611.33977v1 Announce Type: new
Abstract: Direct-access cloud OLAP engines rely on local caches to hide remote object-store latency, yet the replacement design space remains poorly understood. Existing systems largely inherit recency- or Clock-oriented policies from DBMS buffer management, even though cloud misses combine a size-independent request overhead with a size-dependent transfer cost and cache objects vary widely in size. We present a broad experimental comparison of 22 cache-replacement algorithms and one semantic-caching baseline across seven analytical workloads and ten cache sizes. To compare them on a common basis, we formulate Unified Hit Ratio (UHR), a latency-weighted hit ratio that decomposes into a workload-specific weighted combination of object and byte hit ratios, and equivalently, the normalized fraction of aggregate remote-download latency saved by caching.
Our results yield practitioner-oriented guidance. Classical size-aware policies developed outside the DBMS literature remain surprisingly strong, dominating object hit ratio on most workloads and staying near the UHR frontier. Byte efficiency depends primarily on aggressive filtering of zero-reuse objects, while under multi-tenant drift lightweight per-request adaptation is often more robust than retraining-heavy learned methods. We instantiate these lessons in LARA, a compact reference policy that validates the guidance through competitive UHR performance.
