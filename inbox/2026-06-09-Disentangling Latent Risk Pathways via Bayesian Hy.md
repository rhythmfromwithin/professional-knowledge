---
interest: medium
link: https://arxiv.org/abs/2606.07677
next_step: skim
priority: medium
slack_ts: '1780978310.111599'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Disentangling Latent Risk Pathways via Bayesian Hypergraph Inference
---
# Disentangling Latent Risk Pathways via Bayesian Hypergraph Inference
> 原文: [https://arxiv.org/abs/2606.07677](https://arxiv.org/abs/2606.07677)

arXiv:2606.07677v1 Announce Type: new
Abstract: Electronic health records (EHR) pose large-scale multi-disease modeling problems in which many outcomes are rare and strongly influenced by shared risk factors. While modern approaches achieve strong predictive performance, they often treat diseases independently or rely on black-box architectures, offering limited insight into how risk factors organize disease risk and little principled uncertainty quantification. We introduce a Bayesian hypergraph inference framework that reframes multi-disease modeling around latent, risk-factor-modulated disease pathways. Risk factors act on hyperedges, latent disease subsets with shared risk patterns, allowing diseases to participate in multiple distinct pathways and enabling interpretable, higher-order structure beyond pairwise associations. A repulsion prior encourages parsimonious and identifiable structure, while posterior inference provides calibrated uncertainty over both disease groupings and risk-factor influence. To enable scalable inference on large EHR datasets, we develop a structured variational inference algorithm that preserves logical dependencies among hyperedge existence, disease membership, and pathway-level effects. Experiments on simulated data and UK Biobank demonstrate stable and interpretable disease pathway structure, well-calibrated uncertainty, improved estimation for rare diseases, and competitive predictive performance.
