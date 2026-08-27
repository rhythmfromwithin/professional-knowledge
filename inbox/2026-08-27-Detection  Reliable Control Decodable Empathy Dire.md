---
title: "Detection != Reliable Control: Decodable Empathy Directions Yield at Most Partial Shifts in Automated Empathy Scores"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2608.24901
priority: high
status: unread
interest: medium
next_step: skim
---
# Detection != Reliable Control: Decodable Empathy Directions Yield at Most Partial Shifts in Automated Empathy Scores
> 原文: [https://arxiv.org/abs/2608.24901](https://arxiv.org/abs/2608.24901)

arXiv:2608.24901v1 Announce Type: new
Abstract: A decodable "empathy" direction is routinely read as a causal lever, conflating decodability, automated-metric control, and human-perceived change. We test this for two EPITOME-derived facets -- Recognition (cognitive) and Resonance (affective) -- in three instruction-tuned LLMs, scoring every intervention with two LLM judges and a discriminative EPITOME classifier, each gated by an emotional-vs-neutral positive control. The control passes for the affective facet across all automated instruments, but cognitive range is inconsistent across them. Both facets remain decodable after residualizing against a sentence-embedding-derived surface score, and steering can substantially rewrite the text. Yet adding the Resonance direction raises the affective score only partially -- in Qwen by +0.29 (approximately 26% of the natural gap). A direct between-direction contrast confirms the shift is facet-specific in Qwen and Llama (not Gemma); we do not, however, establish a matching human-perceived change. Additive cognitive steering produces no measurable change, but a within-domain control shows the cognitive instrument is too coarse to resolve the differences such steering would produce -- unmeasurable, not a clean null. By contrast, Gemma Recognition ablation lowers the classifier's cognitive score even after adjusting for response length. Detection does not imply reliable control under global interventions, and cognitive-empathy claims warrant an explicit measurement-sensitivity check.
