---
interest: medium
link: https://arxiv.org/abs/2603.02333
next_step: skim
priority: high
slack_ts: '1773369794.439019'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Characterizing Memorization in Diffusion Language Models: Generalized Extraction
  and Sampling Effects'
---
# Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects
> 原文: [https://arxiv.org/abs/2603.02333](https://arxiv.org/abs/2603.02333)

arXiv:2603.02333v1 Announce Type: new
Abstract: Autoregressive language models (ARMs) have been shown to memorize and occasionally reproduce training data verbatim, raising concerns about privacy and copyright liability. Diffusion language models (DLMs) have recently emerged as a competitive alternative, yet their memorization behavior remains largely unexplored due to fundamental differences in generation dynamics. To address this gap, we present a systematic theoretical and empirical characterization of memorization in DLMs. We propose a generalized probabilistic extraction framework that unifies prefix-conditioned decoding and diffusion-based generation under arbitrary masking patterns and stochastic sampling trajectories. Theorem 4.3 establishes a monotonic relationship between sampling resolution and memorization: increasing resolution strictly increases the probability of exact training data extraction, implying that autoregressive decoding corresponds to a limiting case of diffusion-based generation by setting the sampling resolution maximal. Extensive experiments across model scales and sampling strategies validate our theoretical predictions. Under aligned prefix-conditioned evaluations, we further demonstrate that DLMs exhibit substantially lower memorization-based leakage of personally identifiable information (PII) compared to ARMs.
