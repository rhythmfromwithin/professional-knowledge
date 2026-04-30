---
interest: medium
link: https://arxiv.org/abs/2604.22771
next_step: skim
priority: high
slack_ts: '1777521054.605699'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model
  Token Distributions'
---
# The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model Token Distributions
> 原文: [https://arxiv.org/abs/2604.22771](https://arxiv.org/abs/2604.22771)

arXiv:2604.22771v1 Announce Type: new
Abstract: Language models cannot be random. This paper introduces Entropic Deviation (ED), the normalised KL divergence between a model's token distribution and the uniform distribution, and measures it systematically across 31,200 generations spanning seven models, two architectures (transformer and state space), nine prompt categories, three temperatures, and five languages. Under semantically neutral prompts (empty strings, random characters, nonsense syllables) transformers still exhibit ED of approximately 0.30, meaning that 88-93% of the non-randomness observed under semantic prompts is intrinsic to the learned weights rather than induced by context. Three transformer families (Gemma, Llama, Qwen) converge on nearly identical ED values despite different training data and vocabularies. A state space model (Mamba2) reveals a qualitatively different regime: twice the ED, three times lower within-sequence variance, and massive sensitivity to temperature (r = -0.78) where transformers are nearly immune (r < 0.05). Cross-lingual experiments with Qwen-32B show a stable gradient across five languages (English, Japanese, Chinese, Polish, Arabic) that does not correlate with token fertility and persists when two languages sharing an identical tokeniser subset are compared. These findings establish a structural lower bound on randomness in pretrained language models, characterise how this bound differs across architectures, and demonstrate that language itself modulates the bound independently of tokenisation.
