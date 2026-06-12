---
interest: medium
link: https://arxiv.org/abs/2606.12586
next_step: skim
priority: low
slack_ts: '1781239679.912559'
source: cs.CR - Cryptography and Security
status: unread
title: 'Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic
  Systems'
---
# Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems
> 原文: [https://arxiv.org/abs/2606.12586](https://arxiv.org/abs/2606.12586)

arXiv:2606.12586v1 Announce Type: new
Abstract: Vision-Language Agentic Systems (VLAS) connect visual perception to planning, tool use, and physical actions. This means backdoor-type triggers can propagate through both decision pipelines and their connected interfaces, thus making visual backdoors a system-level threat. Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended. In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior. To quantify this leakage, we introduce Neighbor Leakage Rate (NLR). Our experiments show that at a 3% poisoning ratio, icon and text triggers remain robust to common visual transformations, but their neighboring variants leak heavily, with NLR reaching 0.996 (icon) and 0.944 (text). Using textual triggers as a controlled probe, we show that standard fine-tuning learns a broad activation region rather than an exact trigger condition, causing neighboring strings to invoke the malicious behavior even when the exact trigger is absent. Adding edit-distance-one hard-negative samples during training substantially narrows this activation region and reduces leakage, including in image-editing and embodied-manipulation workflows, where leaked triggers can propagate into executable programs and action sequences.
