---
interest: medium
link: https://arxiv.org/abs/2611.25043
next_step: skim
priority: high
slack_ts: '1795243599.549599'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Closing the Analyze-to-Design Gap: An Authorization-Bounded Agent for Self-Driving
  Laboratories'
---
# Closing the Analyze-to-Design Gap: An Authorization-Bounded Agent for Self-Driving Laboratories
> 原文: [https://arxiv.org/abs/2611.25043](https://arxiv.org/abs/2611.25043)

arXiv:2611.25043v1 Announce Type: new
Abstract: Artificial intelligence (AI) agents are increasingly integrated into self-driving laboratories (SDLs) to plan experiments and interpret results. However, analytical reasoning alone does not make a laboratory autonomous: autonomy in an SDL is achievable only when the agent can be trusted to act on physical hardware unsupervised and knows when to defer to a human. Here, we present an architecture that integrates an agent at the Analyze-Design interface of the Design-Make-Test-Analyze (DMTA) cycle, enabling agent-driven measurement selection and data interpretation while ensuring that state-changing operations are authorized, validated, and auditable. We demonstrate this architecture on a liquid chromatography-mass spectrometry (LC-MS) instrument in an oxidant-screening campaign for synthesizing an organic dye. Within human-defined campaign limits, the agent submitted measurement jobs, interpreted mass spectrometry (MS) and diode-array detection (DAD) data, flagged failed experiments, and produced an oxidant ranking. This ranking matched that obtained from scripted peak integration, and organic chemists confirmed the agent's spectral interpretations and failure assignments. In a simulated environment that replays the archived LC-MS data, where the agent chose which wells to inject under varying injection limits, it measured the highest-yielding condition at about its seventh injection, against 14.5 on average for a random order, and identified it in every campaign with a limit of eight or more injections. An agent can therefore close the analysis-to-design gap while its actions stay bounded and verifiable, which is a step toward greater autonomy for SDLs.
