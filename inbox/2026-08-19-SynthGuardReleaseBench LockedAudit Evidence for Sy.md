---
interest: medium
link: https://arxiv.org/abs/2608.14753
next_step: skim
priority: low
slack_ts: '1787103736.818809'
source: cs.CR - Cryptography and Security
status: unread
title: 'SynthGuard-ReleaseBench: Locked-Audit Evidence for Synthetic Tabular Data
  Releases'
---
# SynthGuard-ReleaseBench: Locked-Audit Evidence for Synthetic Tabular Data Releases
> 原文: [https://arxiv.org/abs/2608.14753](https://arxiv.org/abs/2608.14753)

arXiv:2608.14753v1 Announce Type: new
Abstract: Synthetic tabular data are often judged by realism, privacy, or downstream-task scores. Those scores do not answer whether a proposed release is supported for a named use, population, and threat model. We introduce SynthGuard-ReleaseBench, an audit framework that locks the use, candidate panel, tolerances, and audit schedule before evaluation. It compares real-trained and synthetic-trained workflows on protected data, gives simultaneous finite-sample bounds for bounded loss gaps, requires controls, and keeps utility, empirical privacy risk, mechanism claims, and human release authority separate.
Across four American Community Survey studies, five non-ACS records, two chronological diagnostics, and a sealed prototype, the benchmark retains favorable, unfavorable, and excluded outcomes. Transparent baselines pass some locked audits; compact learned models fail under the declared budgets; a health-table case is excluded because its negative control passes. A post-audit scaling arm, repeated across three generation seeds, shows the same locked criterion admitting those learned models once they are fit on enough data while still rejecting a dependence-destroying control at every size, so the criterion discriminates rather than merely rejects; the same repetition withdraws a finer single-seed ordering.
The theory adds a pre-audit sample-size rule, variance-adaptive and anytime-valid certificates that tighten the bound two to ten times on the same locked evidence, a temporal certificate for time-ordered audits, and two lower bounds: ordinary bounded queries reconstruct a protected audit once the query budget reaches its size, and the panel-size correction is necessary rather than conservative. The contribution is a reproducible workflow for use-specific release evidence, not a claim that any generator is private, safe, or deployment-ready.
