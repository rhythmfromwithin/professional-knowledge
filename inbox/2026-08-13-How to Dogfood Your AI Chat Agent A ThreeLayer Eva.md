---
interest: medium
link: https://arxiv.org/abs/2608.09939
next_step: skim
priority: low
slack_ts: '1786674573.671359'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'How to Dogfood Your AI Chat Agent: A Three-Layer Evaluation Framework with
  Goal-Directed NPC Simulation'
---
# How to Dogfood Your AI Chat Agent: A Three-Layer Evaluation Framework with Goal-Directed NPC Simulation
> 原文: [https://arxiv.org/abs/2608.09939](https://arxiv.org/abs/2608.09939)

arXiv:2608.09939v1 Announce Type: new
Abstract: Production teams deploying LLM chat agents face a specific quality assurance gap: existing evaluation tools test individual responses or simulate social interactions, but none systematically verify whether real users can achieve their goals through multi-turn conversation. We introduce a three-layer dogfooding framework that bridges this gap by combining canonical question-bank testing (Layer 1), random-walk multi-turn evaluation (Layer 2), and a goal-directed NPC (Non-Player Character) simulator with five structured goal types and a ten-category failure taxonomy (Layer 3). In a longitudinal case study on a production multi-agent system over roughly three months (257 evaluation runs; a 108-scenario NPC suite), we find that the three layers produce complementary regression signals: cross-layer correlation for response quality is weak within a synchronized run (Spearman rho between -0.15 and 0.14) and negative across the longitudinal series (rho down to -0.46), confirming that canonical correctness does not predict goal-directed conversation success. The NPC simulator achieves 77 percent goal achievement at 0.17 dollars per run (6,272x cheaper than human evaluation), enabling daily CI/CD integration with automated PROMOTE/HOLD/ROLLBACK release decisions. We release full prompt templates, the failure taxonomy, and a Python-first replicability guide so that other teams can adopt the framework for their own LLM chat agents.
