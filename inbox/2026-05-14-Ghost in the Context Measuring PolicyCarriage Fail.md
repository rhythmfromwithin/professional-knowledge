---
title: "Ghost in the Context: Measuring Policy-Carriage Failures in Decision-Time Assembly"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.12535
priority: low
status: unread
interest: medium
next_step: skim
---
# Ghost in the Context: Measuring Policy-Carriage Failures in Decision-Time Assembly
> 原文: [https://arxiv.org/abs/2605.12535](https://arxiv.org/abs/2605.12535)

arXiv:2605.12535v1 Announce Type: new
Abstract: LM agents do not act on raw interaction history; they act on a bounded decision state assembled by truncation, summarization, reordering, and rewriting. If directive-bearing state is dropped, weakened, or rebound during that step, an agent can cross a policy boundary without prompt override, model changes, or persistent-memory compromise. We study this failure mode over local Llama 3.1 8B, Qwen 2.5 7B, and Mistral 7B using judged exact constraint respect and direct audits of assembled-state visibility. We evaluate SafeContext, a control layer that pins control state, reuses retained control prefixes, and optionally injects reminders under pressure while keeping model weights fixed. Unmitigated risk is systematic, but absolute exact respect remains low. Against truncation, SafeContext yields small gains; against a strong structured-compaction policy, most aggregate lift disappears, leaving residual benefit mainly in overflow eviction and selected aliasing slices. Replay-only does not explain the effect. A larger-model extension on Qwen 14B and Llama 70B shows the same failure object under larger models, although sign and magnitude remain policy-conditional. Decision-time context assembly is therefore a measurable part of the control path that can be partially hardened.
