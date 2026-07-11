---
title: "RetractorDB: A Deterministic Edge Signal Processing Engine Based on Rational Beatty Sequences and Fraenkel's Partition"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2607.07730
priority: low
status: unread
interest: medium
next_step: skim
---
# RetractorDB: A Deterministic Edge Signal Processing Engine Based on Rational Beatty Sequences and Fraenkel's Partition
> 原文: [https://arxiv.org/abs/2607.07730](https://arxiv.org/abs/2607.07730)

arXiv:2607.07730v1 Announce Type: new
Abstract: We present RetractorDB, an open-source edge signal processing engine (ESPE) for regular time series whose query semantics is grounded in the number theory of covering systems. RetractorDB is designed to support, not replace, time-series databases (TSDB) and data stream management systems (DSMS): deployed close to the signal source, it pre-processes and filters high-frequency measurements on the edge device through a declarative signal-processing query language, maintains a partial, correctable record of past and scheduled future events in inspectable artifacts, and transmits exact, deterministic results upstream, so that only reduced, already-processed streams reach the central architecture. The data model is differential (a stream is a pair $(s\_n, \Delta)$ with a constant rational inter-arrival interval), and the core rate-conversion operators, interleave and de-interleave, are proved to be rational Beatty sequences satisfying the conditions of Fraenkel's partition theorem. This yields an algebra in which resampling is an exact, deterministic, first-class operator: de-interleaving inverts interleaving bit-for-bit using rational arithmetic alone, and algebraic rewrite rules license query-plan optimization without changing results. We describe the end-to-end realization of this algebra in a working engine: declarative query language (RQL), compilation to a dependency DAG with rational interval resolution, slot-based runtime scheduling, and an inspectable artifact format with schema and null/gap metadata. We validate the semantics on deterministic query examples drawn from the engine's integration tests, including a complete Pan-Tompkins QRS-detection pipeline over MIT-BIH ECG data expressed entirely within the algebra. A performance evaluation under a real-time operating environment is in progress and deferred to a subsequent version.
