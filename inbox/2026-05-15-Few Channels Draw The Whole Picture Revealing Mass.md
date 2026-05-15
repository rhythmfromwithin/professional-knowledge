---
title: "Few Channels Draw The Whole Picture: Revealing Massive Activations in Diffusion Transformers"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.13974
priority: medium
status: unread
interest: medium
next_step: skim
---
# Few Channels Draw The Whole Picture: Revealing Massive Activations in Diffusion Transformers
> 原文: [https://arxiv.org/abs/2605.13974](https://arxiv.org/abs/2605.13974)

arXiv:2605.13974v1 Announce Type: new
Abstract: Diffusion Transformers (DiTs) and related flow-based architectures are now among the strongest text-to-image generators, yet the internal mechanisms through which prompts shape image semantics remain poorly understood. In this work, we study massive activations: a small subset of hidden-state channels whose responses are consistently much larger than the rest. We show that, despite their sparsity, these few channels effectively draw the whole picture, in three complementary senses. First, they are functionally critical: a controlled disruption probe that zeroes the massive channels causes a sharp collapse in generation quality, while disrupting an equally-sized set of low-statistic channels has marginal effect. Second, they are spatially organized: restricting image-stream tokens to massive channels and clustering them yields coherent partitions that closely align with the main subject and salient regions, exposing a structured spatial code hidden inside an apparently outlier-like subspace. Third, they are transferable: transporting massive activations from one prompt-conditioned trajectory into another, shifts the final image toward the source prompt while preserving substantial content from the target, producing localized semantic interpolation rather than unstructured pixel blending. We exploit this property in two use cases: text-conditioned and image-conditioned semantic transport, where massive activations transport enables prompt interpolation and subject-driven generation without any additional training. Together, these results recast massive activations not as activation anomalies, but as a sparse prompt-conditioned carrier subspace that organizes and controls semantic information in modern DiT models.
