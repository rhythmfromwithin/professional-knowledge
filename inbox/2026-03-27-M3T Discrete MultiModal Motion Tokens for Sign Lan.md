---
title: "M3T: Discrete Multi-Modal Motion Tokens for Sign Language Production"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.23617
priority: medium
status: unread
interest: medium
next_step: skim
---
# M3T: Discrete Multi-Modal Motion Tokens for Sign Language Production
> 原文: [https://arxiv.org/abs/2603.23617](https://arxiv.org/abs/2603.23617)

arXiv:2603.23617v1 Announce Type: new
Abstract: Sign language production requires more than hand motion generation. Non-manual features, including mouthings, eyebrow raises, gaze, and head movements, are grammatically obligatory and cannot be recovered from manual articulators alone. Existing 3D production systems face two barriers to integrating them: the standard body model provides a facial space too low-dimensional to encode these articulations, and when richer representations are adopted, standard discrete tokenization suffers from codebook collapse, leaving most of the expression space unreachable. We propose SMPL-FX, which couples FLAME's rich expression space with the SMPL-X body, and tokenize the resulting representation with modality-specific Finite Scalar Quantization VAEs for body, hands, and face. M3T is an autoregressive transformer trained on this multi-modal motion vocabulary, with an auxiliary translation objective that encourages semantically grounded embeddings. Across three standard benchmarks (How2Sign, CSL-Daily, Phoenix14T) M3T achieves state-of-the-art sign language production quality, and on NMFs-CSL, where signs are distinguishable only by non-manual features, reaches 58.3% accuracy against 49.0% for the strongest comparable pose baseline.
