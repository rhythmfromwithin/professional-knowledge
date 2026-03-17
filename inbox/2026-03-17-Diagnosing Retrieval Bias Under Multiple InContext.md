---
interest: medium
link: https://arxiv.org/abs/2603.12271
next_step: skim
priority: high
slack_ts: '1773715545.665419'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Diagnosing Retrieval Bias Under Multiple In-Context Knowledge Updates in Large
  Language Models
---
# Diagnosing Retrieval Bias Under Multiple In-Context Knowledge Updates in Large Language Models
> 原文: [https://arxiv.org/abs/2603.12271](https://arxiv.org/abs/2603.12271)

arXiv:2603.12271v1 Announce Type: new
Abstract: LLMs are widely used in knowledge-intensive tasks where the same fact may be revised multiple times within context. Unlike prior work focusing on one-shot updates or single conflicts, multi-update scenarios contain multiple historically valid versions that compete at retrieval, yet remain underexplored. This challenge resembles the AB-AC interference paradigm in cognitive psychology: when the same cue A is successively associated with B and C, the old and new associations compete during retrieval, leading to bias. Inspired by this, we introduce a Dynamic Knowledge Instance (DKI) evaluation framework, modeling multi-updates of the same fact as a cue paired with a sequence of updated values, and assess models via endpoint probing of the earliest (initial) and latest (current) states. Across diverse LLMs, we observe that retrieval bias intensifies as updates increase, earliest-state accuracy stays high while latest-state accuracy drops substantially. Diagnostic analyses of attention, hidden-state similarity, and output logits further reveal that these signals become flatter and weakly discriminative on errors, providing little stable basis for identifying the latest update. Finally, cognitively inspired heuristic intervention strategies yield only modest gains and do not eliminate the bias. Our results reveal a persistent challenge in tracking and following knowledge updates in long contexts.
