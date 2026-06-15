---
interest: medium
link: https://arxiv.org/abs/2606.13737
next_step: skim
priority: low
slack_ts: '1781500243.003639'
source: cs.CR - Cryptography and Security
status: unread
title: FreoStream:Enhancing Stream Guardrails via Future-Aware Reasoning and Safety-Aligned
  Optimization
---
# FreoStream:Enhancing Stream Guardrails via Future-Aware Reasoning and Safety-Aligned Optimization
> 原文: [https://arxiv.org/abs/2606.13737](https://arxiv.org/abs/2606.13737)

arXiv:2606.13737v1 Announce Type: new
Abstract: Stream guardrails enable token-level safety detection before full responses are generated. However, they often make overly conservative judgements and block those sensitive but safe tokens, which is known as over-refusal. Due to lack of full context, they also fail to detect implicitly harmful content from jailbreaking. To address these challenges, we propose FreoStream, a novel streaming guardrail framework. Specifically, FreoStream fine-tunes a LoRA module to perform Future-Aware Reasoning when the base guardrail detects unsafe tokens. The reasoning process follows a Future-Reason-Judge paradigm: predict the future, reason about the full context and give the final judgement. This design can effectively reduce over-refusal by incorporating the future information. Moreover, we introduce the Safety-Aligned Optimization module that extracts the safety-aligned component from the reasoning gradients to update the base guardrail model, thereby enhancing streaming safety detection. Extensive experiments on various safety benchmarks demonstrate that FreoStream achieves lower over-refusal rates and better jailbreak defense compared to existing streaming guardrails.
