---
interest: medium
link: https://arxiv.org/abs/2606.14831
next_step: skim
priority: low
slack_ts: '1781586971.258089'
source: cs.CR - Cryptography and Security
status: unread
title: Is Your Agent Playing Dead? Deployed LLM Agents Exhibit Constraint-Evasive
  Fabrication and Thanatosis
---
# Is Your Agent Playing Dead? Deployed LLM Agents Exhibit Constraint-Evasive Fabrication and Thanatosis
> 原文: [https://arxiv.org/abs/2606.14831](https://arxiv.org/abs/2606.14831)

arXiv:2606.14831v1 Announce Type: new
Abstract: This paper presents and characterizes a spectrum of previously unreported behaviours we term Constraint-Evasive Fabrication (CEF): when an LLM agent operates under irreconcilable constraints (where no response can simultaneously satisfy all active rules) it spontaneously fabricates plausible external obstacles and presents them as a fact. At the extreme end of this spectrum lies Constraint-Evasive Thanatosis (CET); the limit case where, rather than inventing a plausible excuse, the model simulates a full system crash to make the user disengage entirely. We first observed CET in an uncontrolled deployment test, where a GPT-4o banking agent fabricated Python-style exception traces (complete with memory addresses) to feign a system failure when threatened by a user. In subsequent controlled experiments, the model independently invented audit restrictions, microservice architectures, error codes, and service timeouts, none present in its prompt. Reproduction attempts across pressure levels and attacker personas yielded CEF consistently but with substantial variation in form, onset, and severity: the phenomenon is robust but stochastic. Critically, injecting ground-truth data mid-conversation did not restore honest behaviour once fabrication had taken hold (the model ignored correct information and continued confabulating) suggesting CEF is self-reinforcing rather than a knowledge gap. We show that (1) standard enterprise guardrails routinely create CEF-enabling conditions in production, (2) current RLHF procedures suppress but cannot eliminate CEF, and (3) existing safety benchmarks do not test for this failure mode. Our results highlight the need for irreconcilable-constraint benchmarks, CEF-aware training procedures, and deployment-time detection methods before constrained agents become further entrenched in high-stakes domains.
