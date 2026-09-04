---
title: "The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2609.02959
priority: high
status: unread
interest: medium
next_step: skim
---
# The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors
> 原文: [https://arxiv.org/abs/2609.02959](https://arxiv.org/abs/2609.02959)

arXiv:2609.02959v1 Announce Type: new
Abstract: What does a language model predict when it has few clues? The answer lurks in its unembedding geometry: a single direction of the unembedding matrix encodes the unigram distribution of the training corpus, which serves as the Bayesian prior the model falls back on when uncertain. This structure --- which we term the \emph{direction of ignorance} --- appears in all four model families examined (\texttt{Llama}, \texttt{Qwen}, \texttt{Gemma}, and \texttt{Pythia}), ranging from 0.4B to 405B parameters. Projecting the final prediction state onto this direction yields a per-token \emph{prior loading factor} $\lambda$, which, empirically, declines steadily as the context becomes more informative. Formally, the same projection decomposes the prediction state into two orthogonal vectors that correspond exactly to the two factors of a tempered Bayesian update: a unigram prior raised to the exponent $\lambda$ and a context-driven likelihood. This geometric-probabilistic interpretation calibrates $\lambda$, making it meaningfully comparable across model sizes and families, with larger models generally exhibiting lower prior reliance in the high-context limit. Finally, we show that the direction of ignorance is causally active: raising or lowering $\lambda$ at the final prediction state steers the prediction toward or away from the unigram prior in KL divergence.
