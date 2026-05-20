---
interest: medium
link: https://arxiv.org/abs/2605.15309
next_step: skim
priority: medium
slack_ts: '1779250485.042499'
source: cs.CV - Computer Vision
status: unread
title: 'One Pass Is Not Enough: Recursive Latent Refinement for Generative Models'
---
# One Pass Is Not Enough: Recursive Latent Refinement for Generative Models
> 原文: [https://arxiv.org/abs/2605.15309](https://arxiv.org/abs/2605.15309)

arXiv:2605.15309v1 Announce Type: new
Abstract: Despite remarkable progress, image generation is far from solved. The dominant metric, FID, conflates sample fidelity with mode coverage and is close to being saturated. Yet a model can still exhibit mode collapse while achieving a low FID, since a handful of sharp, near-duplicate images can outscore a model that faithfully covers the full data distribution. We argue that precision and recall are essential complements to FID, and that because FID is already saturated, the more meaningful goal is to improve diversity and coverage. Achieving high recall requires a model that explicitly prioritizes mode coverage, unlike most generative models, which optimize sample fidelity. We introduce RTM, which replaces the single-pass latent mapping in style-based generators with an iterative refinement process, and show that this consistently improves both quality and diversity. Integrated with Implicit Maximum Likelihood Estimation (IMLE), which optimizes mode coverage by design, RTM achieves the highest precision and recall among current state-of-the-art approaches while maintaining competitive FID, with improvements across CIFAR-10, CelebA-HQ at 256x256, and nine few-shot benchmarks. RTM also improves StyleGAN2 and StyleGAN2-ADA on CIFAR-10 and AFHQ-v1 at 512x512, demonstrating that the benefit is not specific to IMLE. Unlike flow-matching baselines that achieve competitive FID at the expense of coverage, recursive refinement improves both quality and diversity simultaneously.
