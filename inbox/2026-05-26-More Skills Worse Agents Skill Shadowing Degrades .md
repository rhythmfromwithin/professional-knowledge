---
interest: medium
link: https://arxiv.org/abs/2605.24050
next_step: skim
priority: low
slack_ts: '1779941827.083719'
source: cs.SE - Software Engineering
status: unread
title: More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding
  Skill Libraries
---
# More Skills, Worse Agents? Skill Shadowing Degrades Performance When Expanding Skill Libraries
> 原文: [https://arxiv.org/abs/2605.24050](https://arxiv.org/abs/2605.24050)

arXiv:2605.24050v1 Announce Type: new
Abstract: Skill libraries allow LLM agents to load task-specific instructions on demand, letting non-expert users solve domain-specific tasks through natural language without knowing which skills exist or how they work. However, performance degrades as libraries grow -- by up to 21\% when scaling from a small set of helpful skills to a 202-skill library. In this work, we formulate this performance degradation as the pass rate drop between loading a library of known-helpful skills and the full library. Moreover, we propose to decompose the pass rate drop by conditioning on the skill(s) invocation -- which skills the agent selects during a trajectory -- into two effects: \emph{skill shadowing}, where the agent selects wrong skills more often as the library expands, and \emph{context overhead}, where the enlarged context degrades execution even when selection is correct. We derive upper bounds on both effects to characterize their magnitudes of impacts to the pass rate drop. Our empirical estimates of the effects and their upper bounds both show that the \emph{skill shadowing} effect grows with library size and significantly contributes to the performance degradation, whereas the \emph{context overhead} effect remains small and indistinguishable from zero. This observed asymmetry establishes that the skill selection failure, not the enlarged context, is the primary bottleneck when expanding the skill libraries.
