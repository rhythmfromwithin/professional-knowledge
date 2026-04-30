---
interest: medium
link: https://arxiv.org/abs/2604.22778
next_step: skim
priority: high
slack_ts: '1777521054.948849'
source: cs.LG - Machine Learning
status: unread
title: 'The Spectral Lifecycle of Transformer Training: Transient Compression Waves,
  Persistent Spectral Gradients, and the Q/K--V Asymmetry'
---
# The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry
> 原文: [https://arxiv.org/abs/2604.22778](https://arxiv.org/abs/2604.22778)

arXiv:2604.22778v1 Announce Type: new
Abstract: We present the first systematic study of weight matrix singular value spectra \emph{during} transformer pretraining, tracking full SVD decompositions of every weight matrix at 25-step intervals across three model scales (30M--285M parameters). We discover three phenomena: \textbf{(1)~Transient Compression Waves:} stable rank compression propagates as a traveling wave from early to late layers, creating a dramatic gradient that peaks early then \emph{reverses} -- late layers eventually over-compress past early layers. \textbf{(2)~Persistent Spectral Gradients:} the power-law exponent~$\alpha$ develops a permanent depth gradient forming a non-monotonic inverted-U in deeper models, with peaks shifting toward earlier layers as depth increases. \textbf{(3)~Q/K--V Functional Asymmetry:} value/output projections compress uniformly while query/key projections carry the full depth-dependent dynamics. The dissociation between transient compression and persistent spectral shape reveals that \emph{rank and spectral shape encode fundamentally different information about training}. We formalize this as a two-timescale dynamical model and derive scaling laws ($\Delta\alpha \propto L^{0.26}$, $R^2{=}0.99$). We validate on nine models across three families (custom, GPT-2, Pythia; 30M--1B parameters; 8--36 layers), demonstrate that $\alpha$ predicts layer importance ($\rho{=}0.69$--$0.84$, $p{<}0.02$), and show that spectral-guided pruning outperforms Last-N heuristics by $1.1{\times}$--$3.6{\times}$ across seven models in two families (GPT-2 124M--774M, Pythia 160M--1B), with worst-vs-best gaps up to $23.7{\times}$ confirming the causal role of spectral structure.
