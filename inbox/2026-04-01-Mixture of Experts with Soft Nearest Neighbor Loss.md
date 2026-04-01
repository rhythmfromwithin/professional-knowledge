---
title: "Mixture of Experts with Soft Nearest Neighbor Loss: Resolving Expert Collapse via Representation Disentanglement"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.26734
priority: low
status: unread
interest: medium
next_step: skim
---
# Mixture of Experts with Soft Nearest Neighbor Loss: Resolving Expert Collapse via Representation Disentanglement
> 原文: [https://arxiv.org/abs/2603.26734](https://arxiv.org/abs/2603.26734)

arXiv:2603.26734v1 Announce Type: new
Abstract: The Mixture-of-Experts (MoE) model uses a set of expert networks that specialize on subsets of a dataset under the supervision of a gating network. A common issue in MoE architectures is ``expert collapse'' where overlapping class boundaries in the raw input feature space cause multiple experts to learn redundant representations, thus forcing the gating network into rigid routing to compensate. We propose an enhanced MoE architecture that utilizes a feature extractor network optimized using Soft Nearest Neighbor Loss (SNNL) prior to feeding input features to the gating and expert networks. By pre-conditioning the latent space to minimize distances among class-similar data points, we resolve structural expert collapse which results to experts learning highly orthogonal weights. We employ Expert Specialization Entropy and Pairwise Embedding Similarity to quantify this dynamic. We evaluate our experimental approach across four benchmark image classification datasets (MNIST, FashionMNIST, CIFAR10, and CIFAR100), and we show our SNNL-augmented MoE models demonstrate structurally diverse experts which allow the gating network to adopt a more flexible routing strategy. This paradigm significantly improves classification accuracy on the FashionMNIST, CIFAR10, and CIFAR100 datasets.
