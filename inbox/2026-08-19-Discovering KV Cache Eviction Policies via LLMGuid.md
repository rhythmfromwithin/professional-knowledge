---
title: "Discovering KV Cache Eviction Policies via LLM-Guided Program Evolution"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.14555
priority: medium
status: unread
interest: medium
next_step: skim
---
# Discovering KV Cache Eviction Policies via LLM-Guided Program Evolution
> 原文: [https://arxiv.org/abs/2608.14555](https://arxiv.org/abs/2608.14555)

arXiv:2608.14555v1 Announce Type: new
Abstract: KV cache compression is critical for long-context inference, yet effective eviction policies remain difficult to design: existing prefill-stage methods often rely on hand-crafted salience heuristics that can be brittle across models, context lengths, and compression ratios. We present CacheCraft, a program-evolution methodology for automatically discovering KV cache eviction policies using an LLM-guided code-evolution engine. CacheCraft discovers FRC (Feature-Rich Compression), a fixed-weight three-signal scorer that combines local attention received, neighborhood attention density, and KV-head maximum salience with chunk-level top-k selection. Without per-model retuning, FRC ranks first among the evaluated single-pass KVPress baselines at every RULER 4k/8k cell with r >= 0.75 across Llama-3.1-8B-Instruct and Qwen3-8B (12 of 20 grid cells), gaining +15.4 points on Llama-4k and +13.9 points on Qwen-8k at 88% compression. A scorer-versus-structure decomposition shows that the scoring family, not chunk selection, is the load-bearing design choice: incorporating the scorer contributes +67.2 RULER points, while improving chunk structure contributes only ~0.1. Beyond FRC itself, CacheCraft provides a transferable recipe for automated eviction-policy discovery: a compact policy interface, a cascade evaluator with strict output invariants, and a diagnostic loop that treats search plateaus and reward-hacking failures as evidence for reformulating the editable interface.
