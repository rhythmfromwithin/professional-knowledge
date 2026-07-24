---
title: "When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.19523
priority: high
status: unread
interest: medium
next_step: skim
---
# When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play
> 原文: [https://arxiv.org/abs/2607.19523](https://arxiv.org/abs/2607.19523)

arXiv:2607.19523v1 Announce Type: new
Abstract: Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks, but its effect on behavioral diversity in sequential decision-making remains under-explored. We study this question in a controlled suite of deterministic board games based on tic-tac-toe variants, where optimal actions are exactly computable and diversity can be measured directly. Across state-level evaluation, arena gameplay, and training trajectories, we find that reasoning-mode generation frequently suppresses action diversity without uniformly improving action accuracy. Furthermore, standard SFT improves accuracy but often induces premature diversity collapse, which exceeds what is minimally required by the accuracy-diversity tradeoff. We then show that action augmentation, which trains on all optimal actions per state rather than a single demonstrated action, would partially mitigates this effect. Our results identify narrow-support imitation as a source of policy collapse in LLM decision-making and suggest that preserving action support during SFT is important for maintaining exploratory behavior.
