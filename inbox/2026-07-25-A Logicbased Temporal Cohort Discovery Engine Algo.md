---
interest: medium
link: https://arxiv.org/abs/2607.21377
next_step: skim
priority: low
slack_ts: '1785124076.706179'
source: cs.DB - Databases
status: unread
title: 'A Logic-based Temporal Cohort Discovery Engine: Algorithms, Indices, and Experimental
  Results on the National Sleep Research Resource'
---
# A Logic-based Temporal Cohort Discovery Engine: Algorithms, Indices, and Experimental Results on the National Sleep Research Resource
> 原文: [https://arxiv.org/abs/2607.21377](https://arxiv.org/abs/2607.21377)

arXiv:2607.21377v1 Announce Type: new
Abstract: Large sleep-study repositories contain rich time-stamped physiological annotations, but cohort discovery is still commonly implemented as ad hoc scripts or scalar-index filters. We present a logic-based temporal cohort discovery engine that brings formal semantics, model checking, specialized indexing, and empirical evaluation into a unified biomedical informatics framework. We adopt Rational Ensemble Logic (QEL) as a dense-time formal foundation for sleep-data querying and represent each annotated polysomnogram as a Biomedical Event Structure Temporal Model (BEST), a finite mapping from event labels to non-overlapping rational interval ensembles. Cohort discovery is formulated as model checking of QEL formulas over BEST databases. We organize common sleep-research requirements into three reusable temporal query patterns: single-event retrieval, dual-event temporal pattern matching, and event data extraction. The prototype cohort discovery engine was implemented in Python with in-memory and MongoDB-backed execution modes and evaluated on synthetic interval datasets containing up to 90 million intervals and on real-world National Sleep Research Resource annotations from the Cleveland Children's Sleep and Health Study (CCSHS) containing 515 subjects, 202,587 intervals, 23 event labels. 2DFC constructs indexes in linear space and linear build time, reducing build time at 90 million intervals from 11,549 s with RTFC and 23,902 seconds with 2DRT to 3,655 seconds. On CCSHS, cohort-selection queries executed at sub-second latency at native scale and under 45 seconds at 1,000 times scale. This work is a part of the Symbolic Biomedicine program championed by the corresponding author.
