---
title: "AirMoE: Statistic-Augmented Over-the-Air MoE for Collaborative Intelligence"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.16562
priority: medium
status: unread
interest: medium
next_step: skim
---
# AirMoE: Statistic-Augmented Over-the-Air MoE for Collaborative Intelligence
> 原文: [https://arxiv.org/abs/2607.16562](https://arxiv.org/abs/2607.16562)

arXiv:2607.16562v1 Announce Type: new
Abstract: Mixture of Experts (MoE) are increasingly deployed over wireless cloud-edge networks, as a single edge device lacks sufficient resources to host large-scale models locally. In this distributed architecture, a cloud-hosted pretrained Large Model (LM) acts as a shared backbone for latent feature extraction, while heterogeneous experts deployed across distributed, wirelessly-connected clients collaboratively form the task head. However, deploying MoE over wireless links exposes two coupled bottlenecks. On the one hand, routing which clients to activate generally overloads bandwidth-limited uplinks due to required raw feature transmission. On the other hand, aggregating the activated experts' outputs over wireless links is hindered by channel noise and poor scalability. To break these bottlenecks, we propose a statistic-augmented over-the-air MoE (AirMoE) paradigm. Specifically, on the routing side, each client queries its local Feature Retrieval Library (FRL) with a cloud-broadcast compact query, retrieves a prototype-induced statistic, and reports it digitally to the cloud, drastically reducing uplink traffic; the cloud then selects the most relevant clients by aligning these statistics with the LM-extracted features via Jensen--Shannon (JS) divergence. On the aggregating side, selected experts simultaneously transmit their outputs over the multiple-access channel, which physically computes the reweighted sum via waveform superposition, with reweighting coefficients realized through channel-aware power control. The two mechanisms are thus decoupled both algorithmically and physically. We further provide theoretical analyses on convergence and iteration complexity. Taking semantic segmentation task as an example, extensive experiments demonstrate that AirMoE outperforms MoE baselines and single-model competitors. Ablations further confirm the effectiveness of each incorporated component.
