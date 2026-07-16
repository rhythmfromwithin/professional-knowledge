---
interest: medium
link: https://arxiv.org/abs/2607.12065
next_step: skim
priority: medium
slack_ts: '1784172060.668019'
source: cs.RO - Robotics
status: unread
title: 'Enabling 24-hour Agricultural Robotics: Unsupervised Day-to-Night Cross-Modal
  Image Translation for Nighttime Visual Navigation'
---
# Enabling 24-hour Agricultural Robotics: Unsupervised Day-to-Night Cross-Modal Image Translation for Nighttime Visual Navigation
> 原文: [https://arxiv.org/abs/2607.12065](https://arxiv.org/abs/2607.12065)

arXiv:2607.12065v1 Announce Type: new
Abstract: While visual navigation has been extensively studied in agricultural robotics, most existing systems assume daytime conditions. In fact, deploying autonomous robots at night offers significant advantages, including 24-hour crop and soil monitoring, fruit harvesting, and nocturnal pest detection. Modern vision-based systems, however, rely heavily on large-scale well-annotated image datasets, which remains challenging to obtain for nighttime operation scenarios. To address this, we propose an unsupervised image translation framework that converts daytime plant-row RGB images into near-infrared (NIR) nighttime counterparts without requiring pixel-to-pixel supervision. This enables the direct reuse of daytime semantic labels for training nighttime perception models. In particular, by incorporating a pre-trained Contrastive Language-Image Pre-training (CLIP) model, the proposed framework is designed to preserve semantic consistency during day-to-night translation. Additionally, a visibility mask is introduced to account for the limited effective range of NIR illumination in nighttime scenes. We conduct comparative evaluations with state-of-the-art image translation baselines and demonstrate higher image qualities, as supported by improved performance in downstream semantic segmentation for nighttime visual navigation. For evaluation, we utilize AgriNight--a novel dataset comprising 428 daytime and 549 nighttime images collected using night-vision-equipped mobile robots in agricultural fields and manually annotated with pixel-wise semantic labels--and introduce it as the first benchmark for nighttime agricultural visual navigation. We also perform real-time autonomous navigation experiments with a physical robot operating at night. The data and code are available at: https://github.com/mamorobel/AgriNight.
