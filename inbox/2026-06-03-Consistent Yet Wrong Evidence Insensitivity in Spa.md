---
interest: medium
link: https://arxiv.org/abs/2606.02742
next_step: skim
priority: medium
slack_ts: '1780548661.412289'
source: cs.CV - Computer Vision
status: unread
title: 'Consistent Yet Wrong: Evidence Insensitivity in Spatial Vision-Language Models'
---
# Consistent Yet Wrong: Evidence Insensitivity in Spatial Vision-Language Models
> 原文: [https://arxiv.org/abs/2606.02742](https://arxiv.org/abs/2606.02742)

arXiv:2606.02742v1 Announce Type: new
Abstract: Spatial reasoning is fundamental to robotics, autonomy, and embodied AI, yet modern vision-language models (VLMs) remain unreliable on metric distance queries. A common assumption is that consistent predictions across viewpoints reflect geometric grounding. We test this assumption and find the opposite: leading VLMs often produce view-invariant and consistent answers even when those answers are incorrect, indicating weak coupling between predictions and viewpoint-specific visual evidence.
We introduce \textbf{ViewDiag}, a controlled multi-view evaluation protocol built from Hypersim, ScanNet, and KITTI360, comprising 176 object-pair tracks across 80 scenes with 2--10 views per track. The protocol evaluates models along three axes: metric accuracy, distributional concentration, and a latent feature probe for internal collapse that distinguishes decision collapse from representation collapse. Across diverse models, we observe a consistent pattern of high prediction stability paired with substantial error, clustering in a regime characterized by strong consistency but low accuracy.
\noindent These results challenge the common use of cross-view consistency as a proxy for geometric understanding. Instead, we show that stable predictions may reflect prior-driven collapse rather than evidence-sensitive reasoning. ViewDiag provides a controlled benchmark and diagnostic framework for evaluating spatial VLMs beyond accuracy alone. The code and data can be found \href{https://github.com/SDivakarBhat/Consistent\_Yet\_Wrong.git}{here}
