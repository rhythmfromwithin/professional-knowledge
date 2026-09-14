---
interest: medium
link: https://arxiv.org/abs/2609.12085
next_step: skim
priority: high
slack_ts: '1789360384.323679'
source: cs.CL - Computation and Language (NLP)
status: unread
title: What Counts as a Mistake? Annotating Recitation Events in Quran Memorization
  Transcripts
---
# What Counts as a Mistake? Annotating Recitation Events in Quran Memorization Transcripts
> 原文: [https://arxiv.org/abs/2609.12085](https://arxiv.org/abs/2609.12085)

arXiv:2609.12085v1 Announce Type: new
Abstract: Checking Quran recitation from an ASR transcript requires distinguishing unresolved mistakes from repetitions, repairs, opening formulas and accepted spelling differences. We report a completed human annotation of 100 production recording cases: 348 scored units and 162 localized events across ten combined labels. An executable evaluator scores labels and word positions together. A plain diff reaches label-aware F1 0.525 and localization F1 0.826; adapted production cleaner/alignment components reach 0.518 and 0.786, with exact-span F1 0.505 for both. Correcting the adapter's word coordinates recovers all five annotated repetition events, showing why annotation interfaces must be checked before interpreting baseline failures. In a preliminary pilot, eight single 20-minute runs across three coding agents and eight models span label-aware F1 0.143 to 0.892: seven land far above every baseline, and one collapses below the naive diff from a missing normalization step. Across the six, 970 of 972 gold-event instances draw an overlapping prediction, so what remains is not detection but convention: span extent, and the labels whose boundary is stipulated by adjudication rather than visible in the text. Seven of 162 events defeat all six same-day runs, five of them one orthographic rule, and the strongest run still misses the same ones. No run annotated before building, so the pilot measures the algorithm half of the task only.
