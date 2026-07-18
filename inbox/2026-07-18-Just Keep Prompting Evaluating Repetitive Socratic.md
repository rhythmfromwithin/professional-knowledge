---
title: "Just Keep Prompting: Evaluating Repetitive Socratic Prompting in VLMs"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.14099
priority: high
status: unread
interest: medium
next_step: skim
---
# Just Keep Prompting: Evaluating Repetitive Socratic Prompting in VLMs
> 原文: [https://arxiv.org/abs/2607.14099](https://arxiv.org/abs/2607.14099)

arXiv:2607.14099v1 Announce Type: new
Abstract: Deploying Vision-Language Models (VLMs) in real-world settings requires not only strong visual reasoning but also stability under sustained conversational pressure. We introduce Just Keep Prompting (JKP), a multi-turn evaluation framework that measures VLM epistemic stability when users repeatedly challenge, question, or contradict a model's answer. JKP probes models for up to 10 follow-up turns using three strategies: Adversarial Negation (repeated rejection), Pure Socratic Interrogation (repeated calls to reassess certainty), and Context-Aware Socratic Summarization (reflecting the model's prior rationale back before asking for reconsideration). We evaluate GPT-4o, Gemini 2.5 Pro, and Qwen3-VL-30B on a subset of the STAR benchmark across 720 multi-turn runs. Aggregate accuracy changes modestly from Turn 0 to Turn 10, but trajectory-level analysis reveals substantial instability: correct answers regress, wrong answers recover, and many runs exhibit repeated answer flipping. Repeated prompting has bounded upside and often acts as a destabilizer rather than a reasoning aid. The effect is strongly model-dependent: Qwen3-VL-30B achieves the highest final accuracy but becomes confidently wrong under direct contradiction; Gemini 2.5 Pro is comparatively stable but token-expensive; GPT-4o is the most brittle and oscillatory. These findings reveal that multi-turn VLM evaluation captures not just additional reasoning but pressure-response profiles: how models trade off visual grounding, calibration, and conversational compliance under repeated challenge.
