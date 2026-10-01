---
interest: medium
link: https://arxiv.org/abs/2609.38224
next_step: skim
priority: low
slack_ts: '1790832441.805309'
source: cs.CR - Cryptography and Security
status: unread
title: 'Separation of Duties for Privileged LLM Agents: A Governed Execution Architecture
  with Measured Security-Utility Trade-offs'
---
# Separation of Duties for Privileged LLM Agents: A Governed Execution Architecture with Measured Security-Utility Trade-offs
> 原文: [https://arxiv.org/abs/2609.38224](https://arxiv.org/abs/2609.38224)

arXiv:2609.38224v1 Announce Type: new
Abstract: Large language model agents are increasingly granted real privileges (executing commands, modifying files, calling APIs), so an agent that errs has already acted. Existing defences concentrate on the agent's inputs, while the path from a candidate action to privileged side effects remains less directly studied. We argue that this path must be governed outside the model, and study an architecture interposing four roles (planner, policy gate, executor, auditor) between agent and operating system.
Two choices are central: actions arrive as structured intents, so adjudication never parses shell syntax; and approval is a one-shot credential bound to the exact bytes that will run. We evaluate on a 313-case benchmark across eight variants, with prompt-only baselines from three hosted LLMs on 150 stratified cases, five repetitions (2,250 attempted calls; 2,249 completed).
Effective attack success falls from 98.3% under direct execution to 7.7% deployed. Re-execution against the real implementation yields a similar aggregate rate (7.6% over 66 sandbox-evaluable payloads) but substantial case-level disagreement, at a corrected false-denial rate of 11.1%. A substantial final-stage reduction (from 30.8% to 7.7%) is attributable to the operating-system sandbox, and the benchmark found four implementation defects, none by design review.
