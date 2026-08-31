---
interest: medium
link: https://arxiv.org/abs/2608.27527
next_step: skim
priority: medium
slack_ts: '1788152845.290459'
source: cs.CV - Computer Vision
status: unread
title: 'FVeinSyn: Synthetic Finger Vein Image Generator'
---
# FVeinSyn: Synthetic Finger Vein Image Generator
> 原文: [https://arxiv.org/abs/2608.27527](https://arxiv.org/abs/2608.27527)

arXiv:2608.27527v1 Announce Type: new
Abstract: A major challenge in finger vein recognition is the lack of large-scale public datasets. Existing datasets contain few identities and limited samples per finger, restricting the advancement of deep learning-based methods. To address this, we propose FVeinSyn, a large-scale controllable synthetic data generation framework for finger vein. It explicitly decouples synthesis of vascular topology and imaging appearance to mitigate the limitations caused by insufficient training samples, such as inadequate identity diversity and restricted realism. Specifically: first, a finger vein identity generator models vascular topology under physiological and geometric constraints using stochastic L-systems, producing anatomically valid and identity-distinctive vascular patterns. Then, a cascaded region-aware GAN renders the topological maps into realistic near-infrared images. Finally, an intra-class diversity generator introduces geometric and optical perturbations to simulate realistic intra-class variations. Using FVeinSyn, we generated 500,000 images (10,000 vein identities, 50 samples per identity) and conducted extensive evaluations. Results show that FVeinSyn holds significant advantages in realism, identity diversity, vascular pattern consistency, and intra-class diversity. Models trained with FVeinSyn outperform real-data-only baselines a cross eight public datasets, achieving an average accuracy improvement of 27.43\%. The code is available at: https://github.com/EvanWang98/Synthetic-Finger-Vein-Generator.
