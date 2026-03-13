---
title: "4DEquine: Disentangling Motion and Appearance for 4D Equine Reconstruction from Monocular Video"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.10125
priority: medium
status: unread
interest: medium
next_step: skim
---
# 4DEquine: Disentangling Motion and Appearance for 4D Equine Reconstruction from Monocular Video
> 原文: [https://arxiv.org/abs/2603.10125](https://arxiv.org/abs/2603.10125)

arXiv:2603.10125v1 Announce Type: new
Abstract: 4D reconstruction of equine family (e.g. horses) from monocular video is important for animal welfare. Previous mainstream 4D animal reconstruction methods require joint optimization of motion and appearance over a whole video, which is time-consuming and sensitive to incomplete observation. In this work, we propose a novel framework called 4DEquine by disentangling the 4D reconstruction problem into two sub-problems: dynamic motion reconstruction and static appearance reconstruction. For motion, we introduce a simple yet effective spatio-temporal transformer with a post-optimization stage to regress smooth and pixel-aligned pose and shape sequences from video. For appearance, we design a novel feed-forward network that reconstructs a high-fidelity, animatable 3D Gaussian avatar from as few as a single image. To assist training, we create a large-scale synthetic motion dataset, VarenPoser, which features high-quality surface motions and diverse camera trajectories, as well as a synthetic appearance dataset, VarenTex, comprising realistic multi-view images generated through multi-view diffusion. While training only on synthetic datasets, 4DEquine achieves state-of-the-art performance on real-world APT36K and AiM datasets, demonstrating the superiority of 4DEquine and our new datasets for both geometry and appearance reconstruction. Comprehensive ablation studies validate the effectiveness of both the motion and appearance reconstruction network. Project page: https://luoxue-star.github.io/4DEquine\_Project\_Page/.
