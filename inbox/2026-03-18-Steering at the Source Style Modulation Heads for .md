---
interest: medium
link: https://arxiv.org/abs/2603.13249
next_step: skim
priority: high
slack_ts: '1773802313.486039'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Steering at the Source: Style Modulation Heads for Robust Persona Control'
---
# Steering at the Source: Style Modulation Heads for Robust Persona Control
> 原文: [https://arxiv.org/abs/2603.13249](https://arxiv.org/abs/2603.13249)

arXiv:2603.13249v1 Announce Type: new
Abstract: Activation steering offers a computationally efficient mechanism for controlling Large Language Models (LLMs) without fine-tuning. While effectively controlling target traits (e.g., persona), coherency degradation remains a major obstacle to safety and practical deployment. We hypothesize that this degradation stems from intervening on the residual stream, which indiscriminately affects aggregated features and inadvertently amplifies off-target noise. In this work, we identify a sparse subset of attention heads (only three heads) that independently govern persona and style formation, which we term Style Modulation Heads. Specifically, these heads can be localized via geometric analysis of internal representations, combining layer-wise cosine similarity and head-wise contribution scores. We demonstrate that intervention targeting only these specific heads achieves robust behavioral control while significantly mitigating the coherency degradation observed in residual stream steering. More broadly, our findings show that precise, component-level localization enables safer and more precise model control.
