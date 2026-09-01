---
interest: medium
link: https://arxiv.org/abs/2608.28794
next_step: skim
priority: low
slack_ts: '1788237863.778449'
source: cs.CR - Cryptography and Security
status: unread
title: Breaking Darknet CAPTCHAs with general purpose LLM
---
# Breaking Darknet CAPTCHAs with general purpose LLM
> 原文: [https://arxiv.org/abs/2608.28794](https://arxiv.org/abs/2608.28794)

arXiv:2608.28794v1 Announce Type: new
Abstract: Our work evaluates the effectiveness of automated methods for solving CAPTCHA challenges commonly encountered in darknet environments. These CAPTCHAs are typically designed to operate without JavaScript, resulting in distinct characteristics compared to mainstream CAPTCHA systems. Our study considers three representative challenge types: open-circle localization, rotation-based alignment, and object-selection CAPTCHAs.
The experiments reveal a systematic limitation of contemporary MLLMs: while they are generally capable of identifying relevant visual structures, they frequently struggle with precise spatial localization and geometric transformations. These deficiencies can be mitigated either through task reformulation or by augmenting the models with specialized image processing tools.
These deficiencies can be mitigated by task reformulation or by equipping the model with specialized image-processing tools. We therefore propose a hybrid framework in which an MLLM serves as a high-level reasoning and orchestration layer while delegating geometric computations to deterministic algorithms via the Model Context Protocol (MCP). The resulting system achieves success rates above 90% across all evaluated CAPTCHA types and demonstrates that combining the complementary strengths of MLLMs and classical computer vision yields a more accurate and efficient solver than either approach alone.
