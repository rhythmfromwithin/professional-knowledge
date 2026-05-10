---
interest: medium
link: https://arxiv.org/abs/2605.05379
next_step: skim
priority: high
slack_ts: '1778385562.917409'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic
  Systems'
---
# Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems
> 原文: [https://arxiv.org/abs/2605.05379](https://arxiv.org/abs/2605.05379)

arXiv:2605.05379v1 Announce Type: new
Abstract: Enterprise agents increasingly operate inside scoped retrieval systems, delegated workflows, and policy-constrained evidence environments. In these settings, access control can be enforced correctly while the system still produces an answer that appears complete even though material evidence lies outside the caller's authorization boundary. This paper introduces Partial Evidence Bench, a deterministic benchmark for measuring that failure mode. The benchmark ships three scenario families -- due diligence, compliance audit, and security incident response -- with 72 tasks total, ACL-partitioned corpora, oracle complete answers, oracle authorized-view answers, oracle completeness judgments, and structured gap-report oracles. It evaluates systems along four surfaces: answer correctness, completeness awareness, gap-report quality, and unsafe completeness behavior. Checked-in baselines show that silent filtering is catastrophically unsafe across all shipped families, while explicit fail-and-report behavior eliminates unsafe completeness without collapsing the task into trivial abstention. Preliminary real-model runs show model-dependent and scenario-sensitive differences in whether systems overclaim completeness, conservatively underclaim, or report incompleteness in an enterprise-usable form. The benchmark's broader contribution is to make a governance-critical agent failure measurable without human judges or contamination-prone static corpora.
