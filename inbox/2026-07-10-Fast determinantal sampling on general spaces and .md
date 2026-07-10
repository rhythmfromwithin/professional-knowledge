---
title: "Fast determinantal sampling on general spaces and diffusion geometry"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.06644
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fast determinantal sampling on general spaces and diffusion geometry
> 原文: [https://arxiv.org/abs/2607.06644](https://arxiv.org/abs/2607.06644)

arXiv:2607.06644v1 Announce Type: new
Abstract: Determinantal point processes have recently emerged as a kernel-based alternative to standard independent sampling for constructing efficient minibatches, coresets, and other compact representations of large-scale datasets. In particular, sampling mechanisms based on DPPs are believed to demonstrate better approximation properties compared to classical i.i.d. samplers, even at the scale of the exponent. One of the key strengths of DPP based samplers is that they can be deployed over very general spaces, in contrast to more classical sampling methods beyond i.i.d. which tend to work in very well-structured settings, principally Euclidean spaces. In this work, we establish explicit rate guarantees for determinantal sampling in spaces that extend far beyond known Euclidean setups, focusing on spectral kernels obtained from eigenspaces of naturally associated Laplacian and other Markov diffusion operators. This includes, in particular, Riemannian manifolds and weighted networks. In determinantal sampling from compact Riemannian manifolds, we establish sampling rates that automatically pick up the intrinsic dimensionality $d\_{\text{int}}$ of the underlying manifold. In the setting of networks, we investigate DPP-based samplers on the celebrated k-nearest neighbour graphs, as well as weighted random geometric graphs, and demonstrate a similar improved dependence on the intrinsic dimensionality of the data. Overall, our approach achieves guarantees of $\big(\text{sample size}\big)^{-\frac{1}{2}-\frac{1}{2d\_{\text{int}}}}$ that match known rates on Euclidean spaces of comparable dimension. In terms of techniques, we connect to the celebrated Weyl's Law for manifold spectra, and leverage tools from the theory of Markov diffusions and Dirichlet forms as well as certain ingredients from the theory of pseudodifferential operators, which could be of independent interest in this area.
