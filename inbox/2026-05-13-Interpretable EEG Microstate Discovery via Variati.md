---
interest: medium
link: https://arxiv.org/abs/2605.10947
next_step: skim
priority: high
slack_ts: '1778731262.218419'
source: cs.LG - Machine Learning
status: unread
title: 'Interpretable EEG Microstate Discovery via Variational Deep Embedding: A Systematic
  Architecture Search with Multi-Quadrant Evaluation'
---
# Interpretable EEG Microstate Discovery via Variational Deep Embedding: A Systematic Architecture Search with Multi-Quadrant Evaluation
> 原文: [https://arxiv.org/abs/2605.10947](https://arxiv.org/abs/2605.10947)

arXiv:2605.10947v1 Announce Type: new
Abstract: EEG microstate analysis segments continuous brain electrical activity into brief, quasi-stable topographic configurations that reflect discrete functional brain states. Conventional approaches such as Modified K-Means operate directly in electrode space with hard assignment, offering no learned latent representation, no generative decoder, and no mechanism to decode latent configurations into verifiable scalp topographies, limiting both model transparency and interpretability. To address this, we present a Convolutional Variational Deep Embedding (Conv-VaDE) model that jointly learns topographic reconstruction and probabilistic soft clustering in a shared latent space. Conv-VaDE enables generative decoding of cluster prototypes into verifiable scalp topographies, replacing opaque hard partitioning with probabilistic soft assignment. A polarity invariance scheme and a four-dimensional grid search over cluster count (K from 3 to 20), latent dimensionality, network depth, and channel width are conducted to systematically reveal how each architectural design choice shapes the quality, stability, and interpretability of learned EEG microstate representations. The model is evaluated on the LEMON resting-state eyes-closed EEG dataset with ten participants using topographic template formation, clustering stability, and global explained variance (GEV). The architecture search reveals that depth L = 4 appears consistently across all 18 best-performing configurations, yielding a best-case GEV of 0.730 and a silhouette of 0.229 at K = 4 across the model sweeps, where moderately deep networks with compact channel widths and small latent dimensionality dominate across the full K range. These results establish that principled architecture search, rather than model scale, is the key to interpretable and stable EEG microstate discovery via variational deep embedding.
