---
title: "Jigsaw-CRL: Recovering Global Latent Causal Order from Fragmented Multi-Client Interventions"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.28991
priority: medium
status: unread
interest: medium
next_step: skim
---
# Jigsaw-CRL: Recovering Global Latent Causal Order from Fragmented Multi-Client Interventions
> 原文: [https://arxiv.org/abs/2608.28991](https://arxiv.org/abs/2608.28991)

arXiv:2608.28991v1 Announce Type: new
Abstract: Causal representation learning (CRL) aims to recover latent causal variables and their structural relations from high-dimensional observations. Existing CRL methods typically assume that all environments are defined over the same latent variables, or at least share a common latent representation space. We study a fragmented multi-client setting, where multiple clients interact with the same global latent causal system but each client only accesses and intervenes on a subset of the latent variables. In this regime, marginalizing unused latent variables induces bidirected edges, so a single client no longer admits a node-wise latent causal graph, and the global latent causal order must be recovered by assembling client-specific structural fragments. We propose \textbf{Jigsaw-CRL}, a framework for recovering global latent causal order from such fragmented interventions. Under soft interventions, differences between precision matrices across environments exhibit a low-rank structure governed by latent ancestor relations. This enables recovery, for each client, of a block partition, the corresponding block-level ancestral order, and latent subspaces, and then assembly of these fragments into the global node-level latent causal order. We establish identifiability guarantees, develop practical algorithms, and validate the framework on synthetic data. Our codes are available on https://anonymous.4open.science/r/code-for-Jigsaw-CRL-7B26
