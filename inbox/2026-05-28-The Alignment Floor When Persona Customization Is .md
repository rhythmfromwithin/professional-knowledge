---
title: "The Alignment Floor: When Persona Customization Is Safe"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2605.27382
priority: low
status: unread
interest: medium
next_step: skim
---
# The Alignment Floor: When Persona Customization Is Safe
> 原文: [https://arxiv.org/abs/2605.27382](https://arxiv.org/abs/2605.27382)

arXiv:2605.27382v1 Announce Type: new
Abstract: A key promise of pluralistic AI is behavioral adaptation: persona prompts like "be creative" or "be thorough" let systems respect diverse user values and communication styles. But how much customization can a model absorb before its alignment breaks? We present the first controlled study of the alignment-customization tradeoff, testing seven persona conditions across five tasks on two models with different alignment strengths (1,800 runs). We discover the alignment floor: on a strongly-aligned model (Claude Sonnet), persona prompts have zero effect on sycophancy -- all conditions produce ~15%, a stable platform on which rich personalization is safe. On a weakly-aligned model (Nova Lite), the same personas shift sycophancy from 5% to 50% -- the floor is absent and customization becomes a safety liability. Surprisingly, Agreeableness is not the worst offender; Extraversion (+20pp) and Openness (+15pp) cause greater degradation. The constructive finding is the Skeptic defense: a critical-thinking persona reduces sycophancy to 5% even on the weak model -- the single largest effect in the study. Cross-model transfer of persona effects is near-zero ($\rho = 0.006$), meaning alignment testing must be per-model. We propose the alignment floor as a design principle: measure it before deploying persona customization, and layer safety-oriented personas underneath user-facing ones to enable personalization without compromising alignment.
