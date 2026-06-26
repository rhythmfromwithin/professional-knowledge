---
interest: medium
link: https://arxiv.org/abs/2606.26161
next_step: skim
priority: high
slack_ts: '1782447553.225879'
source: cs.AI - Artificial Intelligence
status: unread
title: Refusal Lives Downstream of Persona in Chat Models
---
# Refusal Lives Downstream of Persona in Chat Models
> 原文: [https://arxiv.org/abs/2606.26161](https://arxiv.org/abs/2606.26161)

arXiv:2606.26161v1 Announce Type: new
Abstract: Linear directions in activation space have been identified for both refusal and persona traits in instruction-tuned chat models, but the two have been studied as separate mechanisms. We show they interact: a compliant persona gates refusal. In Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct, we extract a compliant model-persona direction and a refusal direction and intervene on both. Compliant persona steering suppresses refusal -- in Llama, the refusal rate falls from 97% to 2%. Reintroducing the refusal direction partially restores refusal at late layers but not at early ones. Projecting out the persona direction in a late-layer window restores it to baseline; projecting out a random direction does not. Refusal is therefore gated at the late-layer expression stage, downstream of where it is computed. Treating refusal as a single isolated direction misses its dependence on persona.
