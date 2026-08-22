---
interest: medium
link: https://arxiv.org/abs/2608.20186
next_step: skim
priority: low
slack_ts: '1787362751.516809'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Decoding silent reading from non-invasive EEG
---
# Decoding silent reading from non-invasive EEG
> 原文: [https://arxiv.org/abs/2608.20186](https://arxiv.org/abs/2608.20186)

arXiv:2608.20186v1 Announce Type: cross
Abstract: Non-invasive decoding of inner speech faces a fundamental data problem: a corpus pairing brain activity with a person's spontaneous inner monologue cannot be collected, and the available proxy paradigms (cued repetitive and retrospectively reported generative inner speech) are slow to acquire, poorly time-locked, and subject compliance is unverifiable. We therefore treat silent reading as a scalable proxy task and ask how much lexical and semantic information a contrastive decoder can extract from it. We report an open-vocabulary analysis of approximately 240,000 word presentations recorded from a single densely-sampled participant across 393 runs (ca. 49 h) of 19-channel dry-electrode EEG. Words from continuous narrative text were presented in rapid serial visual presentation, with typography randomised on every trial to partially decorrelate word identity from low-level visual form. A convolutional EEG encoder, optionally followed by a causal transformer, was trained with a CLIP-style contrastive objective to align short EEG windows with hidden-state embeddings of the presented word taken from a large language model. Decoding, evaluated as word-grouped top-10 retrieval against permutation baselines, was reliably above chance, extended to mid-frequency and rare words, and scaled log-linearly with training-data volume with no sign of saturation. Removing occipital and posterior-temporal electrodes reduced the word-level gain by roughly one third but left context tracking unchanged. Control analyses separate word-level decoding from narrative context tracking and from a non-neural positional prior introduced by the transformer's positional embedding. These results establish that open-vocabulary word-level information is recoverable from EEG during silent reading, and that decoding is data-limited rather than saturated.
