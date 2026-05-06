---
title: "Latent Space Probing for Adult Content Detection in Video Generative Models"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.00874
priority: medium
status: unread
interest: medium
next_step: skim
---
# Latent Space Probing for Adult Content Detection in Video Generative Models
> 原文: [https://arxiv.org/abs/2605.00874](https://arxiv.org/abs/2605.00874)

arXiv:2605.00874v1 Announce Type: new
Abstract: The rapid proliferation of AI-powered video generation systems has introduced significant challenges in content moderation, particularly with respect to adult and sexually explicit material. Existing detection methods operate on either prompts or decoded pixel-space outputs. Therefore, both approaches are blind to the rich internal representations formed during generation. In this paper, we propose a novel latent space probing framework that intercepts the denoised latent representations produced by the CogVideoX video diffusion model during inference and attaches lightweight classifiers to perform real-time adult content detection. To support this work, we construct a large-scale binary dataset of 11039 ten-second video clips (5086 violating, 5953 non-violating) sourced from adult websites and YouTube respectively. We introduce two lightweight probing classifier architectures. We train and evaluate it on the dataset. Our work demonstrates that latent-space signals encode strong discriminative features for harmful content detection, achieving 97.29% F1 on our held-out test set with an overhead in the 4-6ms range. Our results suggest that probing the latent space results in improvements in both detection performance as well as cost.
