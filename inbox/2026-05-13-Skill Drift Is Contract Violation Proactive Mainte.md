---
title: "Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2605.10990
priority: low
status: unread
interest: medium
next_step: skim
---
# Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries
> 原文: [https://arxiv.org/abs/2605.10990](https://arxiv.org/abs/2605.10990)

arXiv:2605.10990v1 Announce Type: new
Abstract: LLM agents increasingly rely on reusable skill libraries, but these skills silently decay as the external services, packages, APIs, and configurations they reference evolve. Existing monitors detect such changes at the wrong granularity: they observe values, not the role those values play in a skill. A version string in a comment is noise; the same string in a pinned dependency is an operational obligation. We formulate skill drift as contract violation and introduce \sgname{}, which extracts executable environment contracts from skill documents and validates only those role-bearing assumptions against known or live conditions. This distinction turns noisy monitoring into a precision-first maintenance signal. Contract-free CI probes produce 40\% false positives, while \sgname{} raises zero false alarms over 599 no-drift and hard-negative cases (Wilson 95\% CI $[0,0.6]\%$). In known-drift verification, \sgname{} achieves 100\% precision and 76\% recall with the strongest backbone; in a pre-registered study over 49 real skills, it discovers live drift with 86\% conservative precision. Violated contracts also make repair actionable, improving one-round success from 10\% without localization to 78\%. We release \dbname{}, an 880-pair benchmark for skill degradation.
