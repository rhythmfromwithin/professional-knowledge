---
title: "Sparse Goodness: How Selective Measurement Transforms Forward-Forward Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.13081
priority: high
status: unread
interest: medium
next_step: skim
---
# Sparse Goodness: How Selective Measurement Transforms Forward-Forward Learning
> 原文: [https://arxiv.org/abs/2604.13081](https://arxiv.org/abs/2604.13081)

arXiv:2604.13081v1 Announce Type: new
Abstract: The Forward-Forward (FF) algorithm is a biologically plausible alternative to backpropagation that trains neural networks layer by layer using a local goodness function to distinguish positive from negative data. Since its introduction, sum-of-squares (SoS) has served as the default goodness function. In this work, we systematically study the design space of goodness functions, investigating both which activations to measure and how to aggregate them. We introduce top-k goodness, which evaluates only the k most active neurons, and show that it substantially outperforms SoS, improving Fashion-MNIST accuracy by 22.6 percentage points. We further introduce entmax-weighted energy, which replaces hard top-k selection with a learnable sparse weighting based on the alpha-entmax transformation, yielding additional gains. Orthogonally, we adopt separate label feature forwarding (FFCL), in which class hypotheses are injected at every layer through a dedicated projection rather than concatenated only at the input. Combining these ideas, we achieve 87.1 percent accuracy on Fashion-MNIST with a 4x2000 architecture, representing a 30.7 percentage point improvement over the SoS baseline while changing only the goodness function and the label pathway. Across controlled experiments covering 11 goodness functions, two architectures, and a sparsity spectrum analysis over both k and alpha, we identify a consistent principle: sparsity in the goodness function is the most important design choice in FF networks. In particular, adaptive sparsity with alpha approximately 1.5 outperforms both fully dense and fully sparse alternatives.
