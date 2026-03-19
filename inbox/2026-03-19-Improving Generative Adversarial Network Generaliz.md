---
interest: medium
link: https://arxiv.org/abs/2603.15648
next_step: skim
priority: medium
slack_ts: '1773888850.549019'
source: cs.CV - Computer Vision
status: unread
title: Improving Generative Adversarial Network Generalization for Facial Expression
  Synthesis
---
# Improving Generative Adversarial Network Generalization for Facial Expression Synthesis
> 原文: [https://arxiv.org/abs/2603.15648](https://arxiv.org/abs/2603.15648)

arXiv:2603.15648v1 Announce Type: new
Abstract: Facial expression synthesis aims to generate realistic facial expressions while preserving identity. Existing conditional generative adversarial networks (GANs) achieve excellent image-to-image translation results, but their performance often degrades when test images differ from the training dataset. We present Regression GAN (RegGAN), a model that learns an intermediate representation to improve generalization beyond the training distribution. RegGAN consists of two components: a regression layer with local receptive fields that learns expression details by minimizing the reconstruction error through a ridge regression loss, and a refinement network trained adversarially to enhance the realism of generated images. We train RegGAN on the CFEE dataset and evaluate its generalization performance both on CFEE and challenging out-of-distribution images, including celebrity photos, portraits, statues, and avatar renderings. For evaluation, we employ four widely used metrics: Expression Classification Score (ECS) for expression quality, Face Similarity Score (FSS) for identity preservation, QualiCLIP for perceptual realism, and Fr\'echet Inception Distance (FID) for assessing both expression quality and realism. RegGAN outperforms six state-of-the-art models in ECS, FID, and QualiCLIP, while ranking second in FSS. Human evaluations indicate that RegGAN surpasses the best competing model by 25% in expression quality, 26% in identity preservation, and 30% in realism.
