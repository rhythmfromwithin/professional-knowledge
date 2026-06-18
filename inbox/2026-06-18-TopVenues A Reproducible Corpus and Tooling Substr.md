---
interest: medium
link: https://arxiv.org/abs/2606.18320
next_step: skim
priority: low
slack_ts: '1781759645.402799'
source: cs.CR - Cryptography and Security
status: unread
title: 'TopVenues: A Reproducible Corpus and Tooling Substrate for Cybersecurity Literature
  Reviews'
---
# TopVenues: A Reproducible Corpus and Tooling Substrate for Cybersecurity Literature Reviews
> 原文: [https://arxiv.org/abs/2606.18320](https://arxiv.org/abs/2606.18320)

arXiv:2606.18320v1 Announce Type: new
Abstract: Cybersecurity literature reviews require a reproducible denominator: the set of papers that a protocol includes before screening and synthesis begin. Today, that denominator is often reconstructed from publisher portals, bibliographic indices, and scholarly application programming interfaces (APIs) whose coverage, formats, and query semantics change over time. This paper presents TopVenues, an open-source system that materializes corpus construction as a versioned research artifact. TopVenues declares a venue and year scope, uses DBLP Computer Science Bibliography (DBLP) as the metadata spine, enriches records with abstracts and BibTeX entries via open scholarly APIs and publisher-specific extractors, and stores the results in a monotonic SQLite snapshot, accessible via a command-line interface (CLI), a web interface, and export paths for review workflows. The May 2026 snapshot contains 9,925 papers from 11 cybersecurity sources over 2017 to 2026, with 99.86% abstract coverage and 99.99% BibTeX coverage; keyword search over the full corpus completes in under 31 ms, and a 250-test suite validates the data-integrity invariants. The fixed denominator also enables repeatable measurement: 29.2% of 2024 to 2025 papers from the four top-ranked security conferences in our scope appear as arXiv preprints, with a median of five months before publication, and a prior-author-track-record filter yields a 16.5x precision gain at 90% recall for triaging preprints that later appear in the same venue set. TopVenues links corpus construction to auditable cybersecurity measurement by making the corpus itself executable, inspectable, and citable. The artifact is available at https://github.com/sidneibarbieri/topVenues.
