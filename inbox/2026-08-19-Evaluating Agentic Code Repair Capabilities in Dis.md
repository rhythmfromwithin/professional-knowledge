---
interest: medium
link: https://arxiv.org/abs/2608.14863
next_step: skim
priority: low
slack_ts: '1787103728.793299'
source: cs.SE - Software Engineering
status: unread
title: Evaluating Agentic Code Repair Capabilities in Distributed Systems
---
# Evaluating Agentic Code Repair Capabilities in Distributed Systems
> 原文: [https://arxiv.org/abs/2608.14863](https://arxiv.org/abs/2608.14863)

arXiv:2608.14863v1 Announce Type: new
Abstract: LLM-based coding agents have advanced rapidly on single-process SWE tasks, with frontier models now clustering in the high-70s on SWE-bench Verified. Distributed-system debugging, however, remains an under-explored regime: bugs span processes, nodes, and protocol interactions, with root causes rarely recoverable from source alone and brute-force exploration intractable across non-deterministic interleavings. This leaves two gaps in LLM and agent evaluation: no code-repair benchmark targets distributed-system bugs, and no controlled study isolates how much externally provided debugging context changes agent success on them. We introduce DDBench, a code-repair benchmark of 60 historical bugs mined from 13 open-source distributed systems, partitioned into three difficulty tiers.
DDBench evaluates every case under two matched conditions: a symptom-only condition where the agent receives only the bug symptom and repository, and a context-augmented condition where it additionally receives a bounded debugging context (logs, traces, runtime state, and targeted code-investigation notes), isolating the effect of debugging context from model capability. The evaluation of ten LLMs on DDBench reveals several findings. First, distributed debugging exercises a reasoning dimension that single-process benchmarks do not surface: models' pass rates span 61 pp, and pairwise bootstrap separates 9 of 15 top-tier model pairs at p < 0.05 on DDBench's hardest case-set. Second, bounded debugging context lifts aggregate pass rate by +18.1 pp, and the lift is asymmetric: weaker models gain pass rate, while stronger models gain efficiency. Third, debugging context requires careful curation, as even faithful debugging context can sometimes mislead LLMs.
