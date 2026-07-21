---
title: "Toward a mechanistic understanding of inference in visual cortex and diffusion models"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2607.15693
priority: low
status: unread
interest: medium
next_step: skim
---
# Toward a mechanistic understanding of inference in visual cortex and diffusion models
> 原文: [https://arxiv.org/abs/2607.15693](https://arxiv.org/abs/2607.15693)

arXiv:2607.15693v1 Announce Type: new
Abstract: We describe a model of perceptual inference in primary visual cortex (V1) equivalent to a minimal diffusion model whose function can be readily understood from its parameters. The model is based on sparse coding with a non-factorial prior over latent variables in the form of an unconstrained, pairwise interaction matrix, extending standard sparse coding inference to a general recurrent dynamical system. We efficiently train these recurrent dynamics using a denoising score-matching objective and implicit differentiation. After training on natural images, the learned interaction matrix mirrors the structure of horizontal connections in superficial layers of V1 that link neurons of similar orientation tuning. This model exhibits exceptionally good denoising performance, restoring image features such as extended contours amid extreme visual ambiguity, nearly matching the behavior of standard, black-box diffusion architectures in generalization regime. Owing to the model's simplicity, the network's Jacobian can be decomposed directly in terms of the interaction matrix between latent variables, revealing mechanistically how the recurrent dynamics assign high probability over a continuous family of natural structural deformations. Intriguingly, within this circuit, a large fraction of latent variables learn to disconnect from visual input altogether, essentially forming a hierarchical representation that appears to enforce global consistency among image features. Together, the model and results bridge two distinct domains: for neuroscience, it generates concrete, testable hypotheses regarding functional connectivity in recurrent neural circuits during perceptual inference tasks; for machine learning, it elucidates the internal mechanisms learned by diffusion models that allow them to generate infinitely many novel images from a finite training set.
