---
interest: medium
link: https://arxiv.org/abs/2611.33160
next_step: skim
priority: high
slack_ts: '1795850674.833659'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Context Scaling: A New Frontier of AI Scaling'
---
# Context Scaling: A New Frontier of AI Scaling
> 原文: [https://arxiv.org/abs/2611.33160](https://arxiv.org/abs/2611.33160)

arXiv:2611.33160v1 Announce Type: new
Abstract: Many failures of deployed AI arise not from weak inference but from a mismatch between the state a task depends on and the context available when the system acts. Relevant user state, repository revisions, tool traces, sensor readings, or environment changes may be unavailable, distorted, or poorly selected. We call the effort to reduce this bottleneck context scaling. We frame a model as $P\_\theta(d\mid c)$ within a system governed by three budgets: training $B\_\theta$, decision-time $B\_d$, and context-infrastructure $B\_c$. Pretraining scaling invests in $\theta$; decision-time scaling searches, refines, or verifies decisions under supplied context; context scaling improves the system's capacity to acquire, represent, deliver, evaluate, and persist deployment state for model use. The three programs interact, but only $B\_c$ targets what the system can make available before a decision. This view makes the model-infrastructure pair the unit of analysis. We define effective-context value as a task- and intervention-dependent attribution, separate deployment state from model-visible context, and identify availability, fidelity, selection, and utilization failures. We then organize current mechanisms through a five-operation context lifecycle and propose controlled budget interventions and utility-cost curves for evaluation. The resulting agenda centers on grounded reporting, interaction-data and full-cost infrastructure, and safety and governance for persistent, adaptive systems.
