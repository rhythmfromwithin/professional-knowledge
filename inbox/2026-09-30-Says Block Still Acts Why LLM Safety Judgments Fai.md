---
title: "Says Block, Still Acts: Why LLM Safety Judgments Fail to Govern Action in LLM Agents"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.35870
priority: low
status: unread
interest: medium
next_step: skim
---
# Says Block, Still Acts: Why LLM Safety Judgments Fail to Govern Action in LLM Agents
> 原文: [https://arxiv.org/abs/2609.35870](https://arxiv.org/abs/2609.35870)

arXiv:2609.35870v1 Announce Type: new
Abstract: Large language model agents can correctly judge that an action should be blocked while still preferring to take it. We ask why this judgment-action disconnect arises, and whether explicit safety judgment causally governs subsequent action preference. Across three open-weight language models, safety-predictive information remains recoverable from action states, arguing against a simple information-loss account. Instead, the disconnect is better explained by weak coupling between judgment- and action-side causal control: interventions that reliably shift explicit safety judgments toward BLOCK produce much smaller changes in action preference than action-native interventions. This asymmetry persists within a shared judgment-to-action trajectory, where strong upstream control of judgment does not translate into comparably strong downstream control of action preference. Beyond individual intervention directions, judgment- and action-control subspaces overlap only partially, while effective action control remains available in directions orthogonal to the judgment-control subspace. Together, these results distinguish information availability from causal control: an LLM agent can retain the information needed to recognize an action as unsafe without the variables supporting that judgment reliably governing its action preference. For agent safety, this suggests that improving safety recognition or self-critique alone may be insufficient unless safety-relevant computations are also causally coupled to action selection.
