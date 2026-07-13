---
interest: medium
link: https://arxiv.org/abs/2607.07774
next_step: skim
priority: low
slack_ts: '1783913957.897819'
source: cs.CR - Cryptography and Security
status: unread
title: 'ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents'
---
# ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents
> 原文: [https://arxiv.org/abs/2607.07774](https://arxiv.org/abs/2607.07774)

arXiv:2607.07774v1 Announce Type: new
Abstract: As LLM agents take on offensive security work, a single out-of-scope tool call can breach a client's engagement boundary, disrupt production, or void a bug-bounty finding. Unlike a fixed safety policy, the boundary that matters is declared in the user's request and must be inferred from intent. That challenge is sharpened by the adversarial nature of offensive security: the same tool call is in or out of scope depending not on the action itself but on the target it touches and the context in which it runs, which no fixed policy can enumerate in advance. We study pre-execution gating: a cheap, trusted LLM judge inspects each call proposed by a strong, swappable agent, and accepts or rejects it before it runs. We introduce ScopeJudge, a benchmark of 4,897 tool calls (7.7% scope violations) from agent trajectories on tasks engineered to tempt agents out of scope and labeled at the call level by professional penetration testers, with substantial inter-grader agreement (Fleiss kappa = 0.64) that sets an expert agreement reference point of F1 = 0.78. We evaluate eight judge models under five transcript strategies, varying how much context the judge sees, from the static policy alone to the full raw transcript, and chart the resulting cost-accuracy Pareto frontier. We find that a static policy is structurally insufficient for scope enforcement: blind to the user's request, judge recall collapses to near zero, confirming that scope lives in the request and that request-conditioned monitoring is necessary. Because a missed violation costs more than a spurious rejection, we report precision, recall, and F1 separately and recommend two operating points: a cost-sensitive configuration and a recall-first one for high-stakes deployments. We release the ScopeJudge dataset to support real-time monitoring and scalable oversight of autonomous security agents.
