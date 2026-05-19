---
title: "SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.15204
priority: high
status: unread
interest: medium
next_step: skim
---
# SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch
> 原文: [https://arxiv.org/abs/2605.15204](https://arxiv.org/abs/2605.15204)

arXiv:2605.15204v1 Announce Type: new
Abstract: Multi-agent orchestration frameworks such as LangChain, LangGraph, and CrewAI route tasks through graph-based pipelines but do not enforce the stage constraints that govern real business processes. We present SDOF, a framework that treats multi-agent execution as a constrained state machine. SDOF operates through two primary defensive layers, implemented by three components: (1) an Online-RLHF Specialized Intent Router trained via Generative Reward Modeling (GRPO) and (2) a StateAwareDispatcher with GoalStage finite-automaton checks and precondition/postcondition SkillRegistry validation for auditable execution control. On a recruitment system backed by the Beisen iTalent platform (6000+ enterprises), 185 expert-curated scenarios trigger 1671 live API calls. Our GSPO-aligned 7B Intent Router achieves higher joint accuracy than zero-shot GPT-4o on this FSM-constrained adversarial routing benchmark (80.9% versus 48.9%). In end-to-end execution, SDOF reaches 86.5% task completion (95% confidence interval 80.8 to 90.7) and blocks all 22 operations in the injection, illegal HR subset. Under a broader message-level blocking audit, SDOF attains precision 100% and recall 88%, expert agreement kappa=0.94. A separate evaluation on 960 SGD-derived dialogues spanning 8 service domains surfaces 201 stage-order conflicts under our FSM mapping, 41 of which arise in the normal split. This arXiv version reports the current validated scope; extended multi-seed training comparisons and deeper workflow evaluations will be released in a subsequent update.
