---
interest: medium
link: https://arxiv.org/abs/2610.07120
next_step: skim
priority: low
slack_ts: '1791524737.749889'
source: cs.HC - Human-Computer Interaction
status: unread
title: Towards semantic reconstruction of individual words from fnirs using clip loss
---
# Towards semantic reconstruction of individual words from fnirs using clip loss
> 原文: [https://arxiv.org/abs/2610.07120](https://arxiv.org/abs/2610.07120)

arXiv:2610.07120v1 Announce Type: new
Abstract: Semantic reconstruction maps neural activity to a word-embedding space, recovering the meaning of a perceived word instead of selecting it from a fixed vocabulary. Functional near-infrared spectroscopy (fNIRS) carries semantic information suitable for this mapping. However, most fNIRS decoders are trained with a squared-error objective that fits each word independently and ignores the geometry of the embedding space. To address this limitation, we evaluate a contrastive loss based on the contrastive-language-image-pretraining (CLIP) loss, as an alternative to mean-squared-error (MSE) for reconstructing perceived words from fNIRS. We compare the two objectives by training a bidirectional long short-term memory (Bi-LSTM) decoder to map fNIRS signals to word embeddings. We use GloVe-50 and T5 word embeddings as targets, across three fNIRS datasets recorded under a shared paradigm pairing each word image with its spoken name. Performance is measured with a pairwise matching score and open-vocabulary top-$k$ retrieval. The Bi-LSTM trained with CLIP is the most consistent decoder across experiments. T5 produces higher matching scores, whereas every significant retrieval result uses GloVe-50. These results support the use of contrastive objectives as a promising direction for fNIRS semantic decoding and motivate validation on larger datasets.
