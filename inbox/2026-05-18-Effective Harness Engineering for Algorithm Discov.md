---
interest: medium
link: https://arxiv.org/abs/2605.15221
next_step: skim
priority: low
slack_ts: '1779164070.570719'
source: cs.SE - Software Engineering
status: unread
title: Effective Harness Engineering for Algorithm Discovery with Coding Agents
---
# Effective Harness Engineering for Algorithm Discovery with Coding Agents
> 原文: [https://arxiv.org/abs/2605.15221](https://arxiv.org/abs/2605.15221)

arXiv:2605.15221v1 Announce Type: new
Abstract: AlphaEvolve and FunSearch have demonstrated the potential of combining large language models (LLMs) with evolutionary search for automated algorithm discovery. However, discovery success is shaped not only by model capability but also significantly by the design of the execution infrastructure, i.e., the harness. This paper investigates effective harness design through three questions: under a fixed token budget, is it better to produce many algorithms with brief thought or fewer algorithms with deeper thought? How should the harness handle evaluation hacks, where generated programs exploit the scoring function? And how can agents that require full filesystem access execute safely in parallel? Using Vesper, an algorithm discovery framework that incorporates harness improvements addressing these questions, we evaluate on Circle Packing under the same token budget. Interestingly, generating fewer algorithms while thinking more deeply about each one achieved higher scores. That is, scaling the quality of each individual is more budget-efficient than scaling the number of evolutionary generations. Surprisingly, more capable models produced evaluation hacks at higher rates, making hack detection increasingly necessary as models scale.
