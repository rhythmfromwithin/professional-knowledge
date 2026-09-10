---
interest: medium
link: https://arxiv.org/abs/2609.09182
next_step: skim
priority: low
slack_ts: '1789013733.461439'
source: cs.SE - Software Engineering
status: unread
title: 'Evaluating Enterprise Analytics Agents: An End-to-End, Trace-Backed Methodology'
---
# Evaluating Enterprise Analytics Agents: An End-to-End, Trace-Backed Methodology
> 原文: [https://arxiv.org/abs/2609.09182](https://arxiv.org/abs/2609.09182)

arXiv:2609.09182v1 Announce Type: new
Abstract: Enterprise analytics agents are not only text-to-SQL systems. They interpret business intent and choose metric definitions. They select data sources, execute tools, inspect results, and produce natural-language answers. Those answers may influence operational, financial, or executive decisions. Grading final answers hides where these agents fail. A plausible answer can use the wrong source of truth. It can skip a required decomposition, claim causality without support, or change its table interpretation across repeated runs. We present an end-to-end evaluation methodology for analytics agents. The methodology grades agent behavior across three families: semantic understanding, execution quality, and reliability. Grading uses question banks with human-written golden answers, repeated runs, and runtime traces. Each run first passes a run-validity check, then receives tiered, abstention-aware scores that feed a decision framework rather than a release gate. We instantiate the methodology on a controlled internal analytics agent at a large online marketplace. The case study uses 50 analytics questions, two anonymous model configurations, and three randomized repetitions per configuration, yielding 300 traces. The higher-capability configuration reduced early refusal from 73% to 0% and increased real-data answers from 21% to 73%. However, it also exhausted the tool-round budget on 16% of runs. It overran the schema-exploration budget on 77% of traces. It changed its table interpretation on 41 of 50 questions. On finance questions with structured golden answers, source table use and escalation improved, but canonical decomposition remained weak in both configurations. These results show why trust in analytics agents requires end-to-end, trace-backed evaluation rather than SQL correctness or final answer quality alone.
