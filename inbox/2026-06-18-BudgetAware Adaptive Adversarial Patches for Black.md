---
interest: medium
link: https://arxiv.org/abs/2606.18318
next_step: skim
priority: medium
slack_ts: '1781759639.864449'
source: cs.CV - Computer Vision
status: unread
title: Budget-Aware Adaptive Adversarial Patches for Black-Box Object Detection
---
# Budget-Aware Adaptive Adversarial Patches for Black-Box Object Detection
> 原文: [https://arxiv.org/abs/2606.18318](https://arxiv.org/abs/2606.18318)

arXiv:2606.18318v1 Announce Type: new
Abstract: Adversarial patches pose a practical threat to modern object detectors. Prior work shows vulnerability, but three gaps limit actionable insight: (i) few \emph{score-based black-box} attacks \emph{jointly} optimize patch \emph{location, texture, and size} under tight query budgets; (ii) success is rarely tied to the patch's \emph{visual footprint}; and (iii) evaluations often conflate EOT robustness with plain-view suppression. We present \method{}, a query-efficient, budget-adaptive black-box attack that couples a lightweight \emph{Contextual Thompson-Sampling} placer with NES-style pixel updates, growing the patch only when progress stalls. Reporting is anchored by a \emph{strict plain-image} suppression test; EOT is audited but never used as a substitute for success, and optional appearance/printability weights expose strength--visibility trade-offs. Across YOLOv5, Faster R-CNN, and YOLOS, \method{} achieves strong suppression on CNN-based detectors and substantial suppression on the transformer-based detector, using compact patches and exposing clear query--footprint trade-offs relative to fixed-size and heuristic baselines. A print--capture pilot further shows transfer across unseen physical objects and viewpoints.
