---
title: "When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2609.28478
priority: medium
status: unread
interest: medium
next_step: skim
---
# When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI
> 原文: [https://arxiv.org/abs/2609.28478](https://arxiv.org/abs/2609.28478)

arXiv:2609.28478v1 Announce Type: new
Abstract: MagicSchool's K-12 AI product suite is used by millions of teachers and serves millions of teacher and student messages each month. Our team monitors output along four priority dimensions--student safety, tone and instructional role, pedagogical value, and structural output quality--and tracks how often it fails on each. As our program matured, false positives came to dominate the evaluators' flags, misdirecting scarce analyst attention away from failures that warrant product change. To address this, we deployed three enhancements--unanimous-fail panels of repeated judge runs, per-evaluator judge-model choices, and softened rubrics--backed by a pair of synthetic datasets: a benchmark that measures how often cases are flagged, and an egregious-failure set that confirms the worst failures are still caught. Across 21 deployed evaluators, final configurations reached a median benchmark activation rate of 0.04% (16 of 21 at or below 0.2%; 8 at 0.00%) and 100% egregious-failure capture across all 21 evaluators. The strategy cuts confirmed false-positive flags by 99% and raises per-flag precision from 0.6% to 49%, while holding egregious-failure capture at 100% and improving it on 8 of 21 evaluators.
