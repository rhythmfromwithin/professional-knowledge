---
title: "SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.12040
priority: low
status: unread
interest: medium
next_step: skim
---
# SIR-Bench: Evaluating Investigation Depth in Security Incident Response Agents
> 原文: [https://arxiv.org/abs/2604.12040](https://arxiv.org/abs/2604.12040)

arXiv:2604.12040v1 Announce Type: new
Abstract: We present SIR-Bench, a benchmark of 794 test cases for evaluating autonomous security incident response agents that distinguishes genuine forensic investigation from alert parroting. Derived from 129 anonymized incident patterns with expert-validated ground truth, SIR-Bench measures not only whether agents reach correct triage decisions, but whether they discover novel evidence through active investigation. To construct SIR-Bench, we develop Once Upon A Threat (OUAT), a framework that replays real incident patterns in controlled cloud environments, producing authentic telemetry with measurable investigation outcomes. Our evaluation methodology introduces three complementary metrics: triage accuracy (M1), novel finding discovery (M2), and tool usage appropriateness (M3), assessed through an adversarial LLM-as-Judge that inverts the burden of proof -- requiring concrete forensic evidence to credit investigations. Evaluating our SIR agent on the benchmark demonstrates 97.1% true positive (TP) detection, 73.4% false positive (FP) rejection, and 5.67 novel key findings per case, establishing a baseline against which future investigation agents can be measured.
