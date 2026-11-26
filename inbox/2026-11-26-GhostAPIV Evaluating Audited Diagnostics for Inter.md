---
title: "GhostAPI-V: Evaluating Audited Diagnostics for Internal API Migration Repair"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2611.33396
priority: low
status: unread
interest: medium
next_step: skim
---
# GhostAPI-V: Evaluating Audited Diagnostics for Internal API Migration Repair
> 原文: [https://arxiv.org/abs/2611.33396](https://arxiv.org/abs/2611.33396)

arXiv:2611.33396v1 Announce Type: new
Abstract: API migrations require callers to adopt target-version usages while removing incompatible legacy usages. GhostAPI-V represents these obligations as human-audited temporal contracts and supplies candidate-specific repair diagnostics, with correctness assessed by independent behavioral tests. We evaluate 48 internal migrations from eight Python repositories using Claude Code and Codex, with two initial runs per agent and task. Five revision arms branch from the same 192 initial candidates, controlling generation budget, version evidence, and development-test feedback. Hidden-test success is 120/192 (62.5%) for raw version-difference feedback, 130/192 (67.7%) for required-only contracts, and 148/192 (77.1%) for full bidirectional contracts. Full feedback improves over raw version-difference feedback and required-only feedback by 14.6 and 9.4 percentage points, respectively. The package-level effect is positive in all eight repositories and survives the reported repository sensitivity analyses; the forbidden increment is analysis-sensitive. Postfreeze challenges expose symbolic-behavioral disagreement. The results support the complete audited package beyond the same raw evidence and test failures, while leaving human interpretation, obligation wording, and checking entangled.
