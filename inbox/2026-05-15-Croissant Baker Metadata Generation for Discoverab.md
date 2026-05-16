---
interest: medium
link: https://arxiv.org/abs/2605.15079
next_step: skim
priority: low
slack_ts: '1778903340.716549'
source: cs.DB - Databases
status: unread
title: 'Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable
  ML Datasets'
---
# Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets
> 原文: [https://arxiv.org/abs/2605.15079](https://arxiv.org/abs/2605.15079)

arXiv:2605.15079v1 Announce Type: cross
Abstract: Croissant has emerged as the metadata standard for machine learning datasets, providing a structured, JSON-LD-based format that makes dataset discovery, automated ingestion, and reproducible analysis machine-checkable across ML platforms. Adoption has accelerated, and NeurIPS now requires Croissant metadata in every submission to its dataset tracks. Yet in practice Croissant generation usually starts with uploading data to a public platform, a path infeasible for governed and large local repositories that hold much of the high-value data ML increasingly relies on. We release Croissant Baker, a local-first, open-source command-line tool that generates validated Croissant metadata directly from a dataset directory through a modular handler registry. We evaluate Croissant Baker on over 140 datasets, scaling to MIMIC-IV at 886 million rows and 374 Parquet files. On held-out comparisons against producer-authored or standards-derived ground truth, Croissant Baker reaches 97-100% agreement across multiple domains.
