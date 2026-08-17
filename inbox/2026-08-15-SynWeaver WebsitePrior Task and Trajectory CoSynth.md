---
interest: medium
link: https://arxiv.org/abs/2608.12429
next_step: skim
priority: low
slack_ts: '1786931070.741259'
source: cs.SE - Software Engineering
status: unread
title: 'SynWeaver: Website-Prior Task and Trajectory Co-Synthesis for Web Agents'
---
# SynWeaver: Website-Prior Task and Trajectory Co-Synthesis for Web Agents
> 原文: [https://arxiv.org/abs/2608.12429](https://arxiv.org/abs/2608.12429)

arXiv:2608.12429v1 Announce Type: new
Abstract: Web agents often struggle to generalize to unseen websites because they lack website-specific supervision. Recent exploration-based data synthesis methods reduce manual annotation, but they still face two key limitations: they often fail to cover the full functionality of a website, and without sufficient website prior knowledge, they tend to propose hallucinated tasks, which in turn limits the diversity and efficiency of downstream trajectory synthesis. We present \textbf{SynWeaver}, a website-prior task-trajectory co-synthesis framework designed to address these challenges. SynWeaver first performs structured website exploration and constructs a website map that covers a broad set of functionally distinct page states and executable interactions on the target website. It then derives page-level and transition-level supervision from this map to train a UI-aware model with website-specific priors, enabling more grounded task proposals. Finally, SynWeaver performs collaborative task-trajectory synthesis, jointly updating the task and execution trajectory when they become inconsistent, and then verifies and repairs the collected results to produce executable, semantically aligned supervision. Experiments on WebArena and WebVoyager demonstrate that SynWeaver consistently outperforms strong synthesis baselines and yields more effective supervision for both in-domain and out-of-domain generalization.
