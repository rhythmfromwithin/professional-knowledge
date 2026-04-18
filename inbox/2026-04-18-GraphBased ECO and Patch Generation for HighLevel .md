---
interest: medium
link: https://arxiv.org/abs/2604.14248
next_step: skim
priority: low
slack_ts: '1776482312.710569'
source: cs.SE - Software Engineering
status: unread
title: Graph-Based ECO and Patch Generation for High-Level Synthesis
---
# Graph-Based ECO and Patch Generation for High-Level Synthesis
> 原文: [https://arxiv.org/abs/2604.14248](https://arxiv.org/abs/2604.14248)

arXiv:2604.14248v1 Announce Type: new
Abstract: High-level synthesis (HLS) tools offer limited support for Engineering
Change Orders (ECOs), making late-stage design modifications challenging
and costly. This paper introduces a graph-based ECO methodology tailored
for Google XLS. A Graph Edit Distance (GED) algorithm is used to detect
structural differences between original and revised intermediate
representations (IRs), which are then transformed into
patch operations. A patch application mechanism is developed to enforce XLS IR
constraints while preserving semantic correctness, together with a schedule
constraining scheme that maintains the original pipeline registers.
Experiments across several XLS designs demonstrate high structural reuse ratios,
effective schedule preservation, and full functional correctness,
highlighting the practicality of the approach for production HLS flows.
