---
interest: medium
link: https://arxiv.org/abs/2603.08869
next_step: skim
priority: high
slack_ts: '1773888799.403099'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'One Language, Two Scripts: Probing Script-Invariance in LLM Concept Representations'
---
# One Language, Two Scripts: Probing Script-Invariance in LLM Concept Representations
> 原文: [https://arxiv.org/abs/2603.08869](https://arxiv.org/abs/2603.08869)

arXiv:2603.08869v1 Announce Type: new
Abstract: Do the features learned by Sparse Autoencoders (SAEs) represent abstract meaning, or are they tied to how text is written? We investigate this question using Serbian digraphia as a controlled testbed: Serbian is written interchangeably in Latin and Cyrillic scripts with a near-perfect character mapping between them, enabling us to vary orthography while holding meaning exactly constant. Crucially, these scripts are tokenized completely differently, sharing no tokens whatsoever. Analyzing SAE feature activations across the Gemma model family (270M-27B parameters), we find that identical sentences in different Serbian scripts activate highly overlapping features, far exceeding random baselines. Strikingly, changing script causes less representational divergence than paraphrasing within the same script, suggesting SAE features prioritize meaning over orthographic form. Cross-script cross-paraphrase comparisons provide evidence against memorization, as these combinations rarely co-occur in training data yet still exhibit substantial feature overlap. This script invariance strengthens with model scale. Taken together, our findings suggest that SAE features can capture semantics at a level of abstraction above surface tokenization, and we propose Serbian digraphia as a general evaluation paradigm for probing the abstractness of learned representations.
