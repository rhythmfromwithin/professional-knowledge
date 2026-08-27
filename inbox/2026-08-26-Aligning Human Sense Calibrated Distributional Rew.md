---
interest: medium
link: https://arxiv.org/abs/2608.21425
next_step: skim
priority: medium
slack_ts: '1787820595.434849'
source: cs.CV - Computer Vision
status: unread
title: 'Aligning Human Sense: Calibrated Distributional Reward Learning for Video
  Generation'
---
# Aligning Human Sense: Calibrated Distributional Reward Learning for Video Generation
> 原文: [https://arxiv.org/abs/2608.21425](https://arxiv.org/abs/2608.21425)

arXiv:2608.21425v1 Announce Type: new
Abstract: Video generation is central to AI-powered content creation. Aligning generated videos with human preferences is a key criterion for evaluating generation quality. Despite significant progress in visual quality, three key challenges remain. First, the reliability of reward signals is constrained by the quality of human preference data, which is often affected by subjective noise and bias. Second, standard scalar reward models collapse multi-aspect human preferences into a single value, leading to the loss of dynamic trade-offs across multiple preference dimensions. Third, in policy optimization, the widely adopted KL divergence imposes primarily local constraints and may fail to capture the global structure of human preferences. To address these challenges, we propose a unified preference-aware learning framework for video generation. First, we introduce elite-guided filtering to calibrate preference data and construct reliable supervision for reward model training. We then model video quality as a multidimensional reward distribution to capture the uncertainty inherent in human preferences, and use the Wasserstein distance to align the learned reward distribution with the empirical human preference distribution. Finally, we introduce Wasserstein-based distributional alignment into GRPO, guiding policy optimization to better match the global structure of human preferences over videos. Experiments on reward modeling and video generation demonstrate that our approach improves the reliability of reward signals and the perceptual consistency of generated videos. Our code is available at https://github.com/alignhs26/ahs.
