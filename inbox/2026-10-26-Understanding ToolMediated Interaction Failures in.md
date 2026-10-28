---
interest: medium
link: https://arxiv.org/abs/2610.31698
next_step: skim
priority: low
slack_ts: '1793164453.459859'
source: cs.SE - Software Engineering
status: unread
title: 'Understanding Tool-Mediated Interaction Failures in Agentic GUI Software:
  An Empirical Study'
---
# Understanding Tool-Mediated Interaction Failures in Agentic GUI Software: An Empirical Study
> 原文: [https://arxiv.org/abs/2610.31698](https://arxiv.org/abs/2610.31698)

arXiv:2610.31698v1 Announce Type: new
Abstract: Large language model (LLM) agents increasingly complete tasks through live graphical user interfaces (GUIs). Because the model cannot directly operate the GUI, these systems often rely on tools to capture screenshots or UI trees, translate model outputs into GUI actions, and report whether the interface changed. We study failures where this tool-mediated interaction makes the agent's view of the task diverge from the live GUI. We construct Malva, a defect library with 335 confirmed real-world failures from 40 open-source applications. These failures fall into 11 defect patterns rooted in state representation, state transition, and synchronization problems. They are widespread: 90% of the studied applications contain more than one defect type. They are also often silent: incorrectness appears in 86.6% of failures, including 119 cases that produce wrong behavior without a fail-stop signal. We operationalize this taxonomy with MalvaGuard, a pre-deployment static contract checker that reaches 57.3% precision and 76.8% recall on an additional 20-application corpus.
