---
interest: medium
link: https://arxiv.org/abs/2609.31655
next_step: skim
priority: medium
slack_ts: '1790832417.121159'
source: cs.CV - Computer Vision
status: unread
title: 'One Evaluation, Any Operating Point: Hypernetwork-Amortized MeanFlow for 3D
  MRI Reconstruction'
---
# One Evaluation, Any Operating Point: Hypernetwork-Amortized MeanFlow for 3D MRI Reconstruction
> 原文: [https://arxiv.org/abs/2609.31655](https://arxiv.org/abs/2609.31655)

arXiv:2609.31655v1 Announce Type: new
Abstract: Generative priors reconstruct accelerated 3D MRI well but pay heavily at deployment: tens of network evaluations per volume, and protocol-specific hyperparameter tuning. A third hidden cost is the scanner's fixed sampling pattern. We treat the whole operating point as an input. A 3D MeanFlow patch network (a one-step flow model) is fine-tuned end-to-end through a warm-started, five-iteration differentiable conjugate-gradient projection. A small hypernetwork maps the operating point (data-consistency weight, acceleration, and the Cartesian sampling pattern itself) to the network's per-channel modulation. Three findings follow. (i) Learning the acquisition is worth more than any other operating point: on clinical knee data, the learned mask gains up to +2.34 dB over the protocol's variable-density mask. This gain requires the solver: with a feed-forward reconstructor the same learned mask hurts at 4x (-1.7 dB), but with the data-consistency projection it adds +4.6 dB. (ii) One evaluation is highly effective: it beats a 20-step patch-diffusion prior by up to +3.1 dB on brain and +2.9 dB on knee. Three to five evaluations extend the front to +6 dB while using a quarter of the prior's network calls. (iii) Fully sampled targets are optional: trained self-supervised on a split of acquired samples, the reconstructor matches its supervised twin at 4x on real data. Finally, we report what failed and why: subject-adaptive acquisition from measured energy, combining self-supervision with learned acquisition, and amortising the data-consistency weight.
