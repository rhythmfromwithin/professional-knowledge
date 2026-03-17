---
interest: medium
link: https://arxiv.org/abs/2603.07217
next_step: skim
priority: low
slack_ts: '1773715518.702449'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'A Miniature Brain Transformer: Thalamic Gating, Hippocampal Lateralization,
  Amygdaloid Salience, and Prefrontal Working Memory in Attention-Coupled Latent Memory'
---
# A Miniature Brain Transformer: Thalamic Gating, Hippocampal Lateralization, Amygdaloid Salience, and Prefrontal Working Memory in Attention-Coupled Latent Memory
> 原文: [https://arxiv.org/abs/2603.07217](https://arxiv.org/abs/2603.07217)

arXiv:2603.07217v1 Announce Type: new
Abstract: We present a miniature brain transformer architecture that extends the attention-coupled latent memory framework with four additional brain-region analogues: a thalamic relay, an amygdaloid salience module, a prefrontal working-memory (PFC) buffer, and a cerebellar fast-path, all coupled by inhibitory callosal cross-talk between lateralized hippocampal banks. We evaluate on a two-domain benchmark -- MQAR (Multi-Query Associative Recall; episodic domain) and modular arithmetic (+1 mod 10; rule-based domain) -- using a seven-variant additive ablation. The central empirical finding is a surprise: inhibitory callosal coupling alone never lateralizes the banks (variants 1-5 maintain D\_sep ~ 0.25 and P\_ct ~ 0.25 for all 30 epochs). Functional lateralization requires the synergy of PFC and inhibition: only when the PFC buffer is added (variant 6) does a sharp, discontinuous phase transition fire -- at epoch 11 for the PFC-only variant and epoch 10 for the full model -- collapsing P\_ct from 0.25 to ~0.002 and more than doubling D\_sep from 0.251 to 0.501 in a single gradient step. The PFC buffer acts as a symmetry-breaker: its slowly drifting domain context creates the initial asymmetry that the inhibitory feedback loop then amplifies irreversibly. The cerebellar fast-path accelerates the transition by one epoch (epoch 10 vs. epoch 11) with no asymptotic change, confirming its convergence-acceleration role. The result constitutes a novel, falsifiable prediction -- no lateralization without working memory context -- and a principled, neurobiologically motivated blueprint for hierarchical persistent memory in sequence models.
