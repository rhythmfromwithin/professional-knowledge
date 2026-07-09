---
interest: medium
link: https://arxiv.org/abs/2607.02579
next_step: skim
priority: low
slack_ts: '1783569521.012729'
source: cs.SE - Software Engineering
status: unread
title: 'When Not to Write Memory: Governing False Promotion from Correlated Agent
  Traces'
---
# When Not to Write Memory: Governing False Promotion from Correlated Agent Traces
> 原文: [https://arxiv.org/abs/2607.02579](https://arxiv.org/abs/2607.02579)

arXiv:2607.02579v1 Announce Type: new
Abstract: Long-lived language agents increasingly write reusable memories from their own execution traces. The key safety question is not only what agents should remember, but when they should refuse to write memory at all. Repeated observations across agents are not necessarily independent evidence: the same claim may be copied from a shared source, induced by a shared prompt, stale under a new environment, or valid only in a narrower scope. We study this failure mode as a memory writepath governance problem. We introduce GovMem as a conservative diagnostic reference policy that estimates dependency-aware support, retrieves counterevidence, assigns scope, and outputs one of three decisions: promote, reject, or needs-review. In controlled synthetic stress tests, GovMem reduces false promotion from 0.597 to 0.040 in the default setting while preserving 0.960 recall, at an explicit review burden. In a project-internal 120candidate human-labeled real-trace subset spanning 79 recorded traces and project reports, dependency-aware promotion reduces false promotion from 0.371 for source+scope to 0.032 overall, but held-out false promotion remains 0.111 and the method is highly conservative, with 0.692 review burden and 0.448 direct recall. A final human adjudication of 133 high-impact external codingagent candidates is more severe: none are safe for automatic promotion, and all 11 verification-gate positives are rejected as boilerplate, shared-tool artifacts, file dumps, or non-reusable debugging traces. These results support GovMem primarily as a diagnostic governance design point, not as a generally validated or efficient automatic memory writer: agent memory write paths should be evaluated as risk-controlled evidence-governance systems, while broader external coverage and downstream harm evidence are still needed before stronger claims.
