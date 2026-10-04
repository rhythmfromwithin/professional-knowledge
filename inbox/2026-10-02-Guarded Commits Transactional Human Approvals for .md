---
interest: medium
link: https://arxiv.org/abs/2610.00037
next_step: skim
priority: low
slack_ts: '1791091828.069289'
source: cs.DB - Databases
status: unread
title: 'Guarded Commits: Transactional Human Approvals for LLM Workflows'
---
# Guarded Commits: Transactional Human Approvals for LLM Workflows
> 原文: [https://arxiv.org/abs/2610.00037](https://arxiv.org/abs/2610.00037)

arXiv:2610.00037v1 Announce Type: new
Abstract: LLM workflows often require human approval before an irreversible external action. Most systems keep that approval outside the workflow, as an interface click or an audit entry. The workflow therefore lacks a commit-time check that every risky path reached an approval gate. Its logs may not preserve the reviewed evidence or the conditions for reusing an earlier decision. We present a guarded-commit design that makes human approval part of workflow state. Before the external action runs, a decision source appends a resolution record and its referenced evidence to a ledger. A credential-confined commit adapter then checks that record against the artifact, policy version, and executed path. Our evidence is limited to trace reconstruction. A validator test on synthetic acyclic workflow plans accepts unfaulted plans and rejects plans with each injected fault: a missing gate, the wrong gate type, or incomplete path coverage. Across three public workloads totaling 271,035 traces, replay reproduces recorded artifact hashes when present. Avoided reviews and disagreement with recorded decisions vary by workload. The resulting record supports audit and replay under the policy in force when the resolution was recorded.
