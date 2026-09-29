---
interest: medium
link: https://arxiv.org/abs/2609.30288
next_step: skim
priority: high
slack_ts: '1790659452.881849'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Manifold Projection and Iterative Autoencoder Refinement for Masked Language
  Modeling
---
# Manifold Projection and Iterative Autoencoder Refinement for Masked Language Modeling
> 原文: [https://arxiv.org/abs/2609.30288](https://arxiv.org/abs/2609.30288)

arXiv:2609.30288v1 Announce Type: new
Abstract: In Transformer-based masked language models, attention is the primary mechanism for context mixing, but there are other ways to mix data across tokens. Recent attention-free mixers replace attention with fixed or hypernetwork-generated MLPs, alternating their dynamic, content-dependent weighting for computational simplicity. We build an alternative that gets the same property from a low-rank bottleneck autoencoder. We replace attention with a stack of autoencoder-based mixing modules, one operating over local neighborhoods, one over the full sequence, and one across attention heads, each compressing and reconstructing its input through a bottleneck, and its width is a hyperparameter rather than a training effect. In masked positions, we introduce an iterative refinement procedure that has two distinct steps. A pulling step that pulls an embedding representation toward a weighted average of its neighbors, and a correcting step that projects the result back to the learned manifold via an autoencoder. Our architecture achieves a significant portion of attention's performance at about $1.9 \times$ fewer FLOPs when pretrained on C4 and evaluated with parameter-matched BERT baselines. Our model equals parameter-matched BERT and TinyBERT baselines on the rarest-token frequency bucket using a frequency-aware training schedule that samples rare tokens more than uniformly for the masking tasks.
