---
interest: medium
link: https://arxiv.org/abs/2606.13705
next_step: skim
priority: high
slack_ts: '1781500241.203389'
source: cs.LG - Machine Learning
status: unread
title: Can Editing 1 Neuron Fix Repetition Loops in LLMs?
---
# Can Editing 1 Neuron Fix Repetition Loops in LLMs?
> 原文: [https://arxiv.org/abs/2606.13705](https://arxiv.org/abs/2606.13705)

arXiv:2606.13705v1 Announce Type: new
Abstract: Yes. Can it cure doom loops? Probably not.
The Gemma 4 instruction-tuned models share a reproducible failure: on long factual enumeration prompts, such as listing every episode of a TV series, the 88 IAU constellations, or the 151 original Pokemon, they collapse into repetition, either a tight verbatim loop or a list whose entries decay onto a single answer. These loops occur at rates as high as 95% and survive prompt rewording, inference-engine changes, and most sampling adjustments. In this paper we explore whether this behavior is localized enough to remove by weight edits. To localize the cause, we use per-layer ablation and per-neuron attribution, then confirm the strongest candidates with full-generation sweeps. The loops trace to a small set of MLP neurons (or, in the 26B-A4B Mixture-of-Experts model, a few routed experts) which we suppress with static weight edits. These "surgeries" can be as small as a single sign-inverted neuron (in the E2B model). The size of the effective edits grows with model scale, but in all cases, the loop patterns can be addressed at normal generation budgets while preserving general-purpose benchmark scores. However, the edits do not solve everything: we also study longer thinking budgets, where the two larger models most visibly enter doom looping, i.e. a non-convergent regime in which the model self-corrects in circles over a fact it cannot recall, exhausting the budget without committing to a final answer. We show this residual failure is reduced but not eliminated by the same edits, and argue it is fundamentally a knowledge-precision problem rather than a removable circuit; weight surgery can delete a loop, but it cannot supply a missing fact. Our results are both a feasibility demonstration, that is, evidence that a concrete generation pathology can be localized to a few parameters and edited out, and a delineation of where that approach stops.
