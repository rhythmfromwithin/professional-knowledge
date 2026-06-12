---
interest: medium
link: https://arxiv.org/abs/2606.12562
next_step: skim
priority: medium
slack_ts: '1781239682.694979'
source: cs.CV - Computer Vision
status: unread
title: 'HairPort: In-context 3D-aware Hair Import and Transfer for Images'
---
# HairPort: In-context 3D-aware Hair Import and Transfer for Images
> 原文: [https://arxiv.org/abs/2606.12562](https://arxiv.org/abs/2606.12562)

arXiv:2606.12562v1 Announce Type: new
Abstract: Transferring hairstyles between images is an important but challenging task in computer graphics, computer vision, and visual effects. It enables users to explore new looks without physically altering their hair, with applications in virtual try-on systems, augmented reality, and entertainment. Most prior works operate best under small pose gaps, and they fall short under large viewpoint and scale differences, where missing hair content must be synthesized rather than transferred. We propose HairPort, a 3D-aware hairstyle transfer framework that attempts to solve these issues by explicitly separating hair removal from transfer and enforcing geometric consistency before synthesis. We introduce a Bald Converter, which produces realistic bald versions of faces through LoRA-based in-context adaptation of FLUX.1 Kontext. To train our Bald Converter, we introduce a new dataset, Baldy, containing 6,000 paired bald and original images across diverse identities and conditions. We also use a 3D-Aware Transfer Pipeline that reconstructs and re-renders the reference hairstyle from the target viewpoint before compositing it onto the source image. Being 3D aware, our method supports large pose and scale discrepancies between the source and target. Finally, a conditional flow-matching generator synthesizes the transferred result from the bald source and geometry-aligned reference guidance. Together, our method enables accurate, pose-consistent, and identity-preserving hairstyle transfer, outperforming existing methods both qualitatively and quantitatively.
