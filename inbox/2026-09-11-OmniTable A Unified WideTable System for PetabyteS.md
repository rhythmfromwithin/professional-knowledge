---
interest: medium
link: https://arxiv.org/abs/2609.11148
next_step: skim
priority: low
slack_ts: '1789186432.883089'
source: cs.DB - Databases
status: unread
title: 'OmniTable: A Unified Wide-Table System for Petabyte-Scale LLM Data Curation
  and Exploration'
---
# OmniTable: A Unified Wide-Table System for Petabyte-Scale LLM Data Curation and Exploration
> 原文: [https://arxiv.org/abs/2609.11148](https://arxiv.org/abs/2609.11148)

arXiv:2609.11148v1 Announce Type: new
Abstract: Data curation is a critical bottleneck in industrial-grade LLM development, where petabyte-scale unstructured corpora are scattered across hundreds of physical tables, feature engineering relies on manual, table-centric pipeline orchestration, and data lineage is largely absent. We present OmniTable as an architecture blueprint for a unified wide-table layer built on Logical Unification, Physical Separation, targeting petabyte-scale LLM data curation and exploration. OmniTable makes four contributions: (1) a unified wide-table abstraction that consolidates multi-source heterogeneous data and thousands of derived features under a single logical schema via logical-physical mapping; (2) declarative feature lifecycle management that automates dependency resolution, execution planning, operator fusion, and lineage tracking, replacing manual pipeline orchestration with a "declare-and-execute" paradigm; (3) an adaptive execution engine with autonomous governance that achieves stable PB-scale feature backfill through heterogeneous compute routing (CPU/GPU), adaptive tuning, UDF-level fault tolerance, and automated storage layout optimization; and (4) hybrid-accelerated data exploration combining a global ID index, transparent OLAP offloading, and background materialized views to deliver second-level point lookups and filtered exports exceeding 20 TB/hour. In production, OmniTable manages over 35 PB of training data across web, code, PDF, and SFT domains, reducing the human-in-the-loop curation cycle from approximately 14 days to approximately 2.5 days (5.6x over the pre-OmniTable production workflow), with consistent feature versioning, auditable lineage, and minimal manual intervention.
