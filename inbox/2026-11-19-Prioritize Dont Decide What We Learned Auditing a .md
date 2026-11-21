---
interest: medium
link: https://arxiv.org/abs/2611.23359
next_step: skim
priority: high
slack_ts: '1795243591.866729'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Prioritize, Don''t Decide: What We Learned Auditing a Deployed Human-in-the-Loop
  CV Sorter'
---
# Prioritize, Don't Decide: What We Learned Auditing a Deployed Human-in-the-Loop CV Sorter
> 原文: [https://arxiv.org/abs/2611.23359](https://arxiv.org/abs/2611.23359)

arXiv:2611.23359v1 Announce Type: new
Abstract: A single academic vacancy can draw hundreds of applications, and the first screening round consumes most of a committee's time. We describe a CV Priority Sorter deployed at a national platform for academic vacancies and integrated with its vacancy database. It proposes a reading order for a pile of CVs and leaves every decision to the committee, pairing a frozen multilingual transformer encoder with a per-session linear model that retrains after each label and is discarded when the session ends. It works: on a pool of 300 synthetic CVs, a committee reading in the tool's order reaches 95% of the relevant candidates after half the pile, where an arbitrary order needs almost all of it. This paper is about what we found when we audited that claim, rather than about the system itself. Three findings changed the product. The pool turned out to be sortable by document length alone, which makes precision-style metrics on it uninformative; regenerating it under a shared length budget removes that shortcut and leaves the reading-depth result standing. The four-level agreement score such systems report, ours included, is a binary probability cut at fixed thresholds, so it follows the classifier's confidence rather than its ranking and falls as labels accumulate. And uncertainty sampling, the obvious way to implement a "suggest the next CV" button, leaves model quality intact but raises the committee's total reading load above the no-label baseline, because the CVs it asks about are the ones that would otherwise be skipped. A fourth result shows where to look next: a hosted LLM embedding model lifts zero-label ordinal discrimination from 0.66 to 0.80 under length control, then stops mattering once the session model has two dozen labels; a local cross-encoder matches that cold-start gain without sending data out. We report the fixes each finding forced.
