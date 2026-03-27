---
interest: medium
link: https://arxiv.org/abs/2603.19337
next_step: skim
priority: medium
slack_ts: '1774581528.787139'
source: cs.CV - Computer Vision
status: unread
title: Diffusion-Guided Semantic Consistency for Multimodal Heterogeneity
---
# Diffusion-Guided Semantic Consistency for Multimodal Heterogeneity
> 原文: [https://arxiv.org/abs/2603.19337](https://arxiv.org/abs/2603.19337)

arXiv:2603.19337v1 Announce Type: new
Abstract: Federated learning (FL) is severely challenged by non-independent and identically distributed (non-IID) client data, a problem that degrades global model performance, especially in multimodal perception settings. Conventional methods often fail to address the underlying semantic discrepancies between clients, leading to suboptimal performance for multimedia systems requiring robust perception. To overcome this, we introduce SemanticFL, a novel framework that leverages the rich semantic representations of pre-trained diffusion models to provide privacy-preserving guidance for local training. Our approach leverages multi-layer semantic representations from a pre-trained Stable Diffusion model (including VAE-encoded latents and U-Net hierarchical features) to create a shared latent space that aligns heterogeneous clients, facilitated by an efficient client-server architecture that offloads heavy computation to the server. A unified consistency mechanism, employing cross-modal contrastive learning, further stabilizes convergence. We conduct extensive experiments on benchmarks including CIFAR-10, CIFAR-100, and TinyImageNet under diverse heterogeneity scenarios. Our results demonstrate that SemanticFL surpasses existing federated learning approaches, achieving accuracy gains of up to 5.49% over FedAvg, validating its effectiveness in learning robust representations for heterogeneous and multimodal data for perception tasks.
