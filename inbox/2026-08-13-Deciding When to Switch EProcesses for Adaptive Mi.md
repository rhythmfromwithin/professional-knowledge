---
title: "Deciding When to Switch: E-Processes for Adaptive Minimax Training for Generative Adversarial Nets"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2608.10096
priority: medium
status: unread
interest: medium
next_step: skim
---
# Deciding When to Switch: E-Processes for Adaptive Minimax Training for Generative Adversarial Nets
> 原文: [https://arxiv.org/abs/2608.10096](https://arxiv.org/abs/2608.10096)

arXiv:2608.10096v1 Announce Type: new
Abstract: Modern data science increasingly gives rise to hypothesis-testing problems that are not naturally formulated in terms of parameters within prespecified statistical models. One important example is the dynamic evaluation of optimization algorithms, where decisions must be made during training about whether further updates remain beneficial or the algorithm should switch to a different phase. This issue is particularly relevant in stochastic min-max optimization. Generative adversarial networks (GANs) provide a canonical example, as their training requires repeated decisions about when to switch between discriminator and generator updates, yet existing methods typically rely on fixed update ratios or heuristic criteria. We formulate this switching problem as sequential hypothesis testing and develop an e-process-based adaptive training procedure. During discriminator updates, one e-process tests the null that the discriminator-induced separation between the empirical data distribution and the generator law remains below a target level. During generator updates, with the discriminator fixed, a second e-process tests the reverse null that this separation remains above a refresh level. Conditional on the observed training sample, we prove that fresh empirical indices and latent draws yield conditional e-values that can be accumulated into e-processes, providing anytime-valid Type I error control under adaptive model updates and data-dependent switching. Across multimodal synthetic distributions and image benchmark datasets, the proposed method matches or outperforms the best fixed-ratio baselines under several widely used GAN objectives.
