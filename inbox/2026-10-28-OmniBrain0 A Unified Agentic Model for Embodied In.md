---
interest: medium
link: https://arxiv.org/abs/2610.36013
next_step: skim
priority: high
slack_ts: '1793337890.870719'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'OmniBrain-0: A Unified Agentic Model for Embodied Intelligence'
---
# OmniBrain-0: A Unified Agentic Model for Embodied Intelligence
> 原文: [https://arxiv.org/abs/2610.36013](https://arxiv.org/abs/2610.36013)

arXiv:2610.36013v1 Announce Type: new
Abstract: General-purpose embodied intelligence requires robots to coordinate diverse skills over long horizons, track task progress, and recover from failures. Specialist policies alone do not ensure task-level reliability, while powerful multimodal agents rely on costly reasoning and external experience that compact models struggle to reproduce. We introduce OmniBrain-0, a lightweight unified embodied agent that coordinates manipulation and navigation through a shared high-level decision model, integrating task understanding, planning, progress tracking, and feedback-driven recovery. Our progressive training framework combines embodied pretraining, domain-specialized agent distillation, and multi-teacher on-policy distillation (MOPD). It distills powerful teachers' interaction experience into manipulation and navigation experts, then consolidates their decision capabilities into OmniBrain-0. Unification therefore occurs within the learned decision model rather than only at the tool interface. We further introduce Rubric-Guided Recursive Self-Improvement (RSI), a data flywheel in which a Meta-Agent turns execution evidence into refined rubrics, step-level reminders, and verified trajectories for domain-expert updates before their reconsolidation into OmniBrain-0 through MOPD. We evaluate OmniBrain-0 on LIBERO-Pro, LIBERO-Plus, RoboCasa365, RoboTwin 2.0, and R2R-CE Val-Unseen, as well as multiple real-world manipulation tasks. OmniBrain-0 combines strong cross-domain task performance with substantially lower inference and execution overhead than its closed-source teacher, demonstrating efficient transfer and consolidation of embodied capabilities into a compact unified agent.
