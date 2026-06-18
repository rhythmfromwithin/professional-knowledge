---
interest: medium
link: https://arxiv.org/abs/2606.18429
next_step: skim
priority: medium
slack_ts: '1781759640.027249'
source: cs.CV - Computer Vision
status: unread
title: CAOA -- Completion-Assisted Object-CAD Alignment
---
# CAOA -- Completion-Assisted Object-CAD Alignment
> 原文: [https://arxiv.org/abs/2606.18429](https://arxiv.org/abs/2606.18429)

arXiv:2606.18429v1 Announce Type: new
Abstract: Accurately aligning CAD models to their corresponding objects in indoor RGB-D scans is a central challenge in 3D semantic reconstruction. The task requires estimating a 9-Degree-of-Freedom (DoF) pose-position, rotation, and scale along three axes-but is hindered by noisy and incomplete scans, as well as segmentation errors that cause geometric distortions. We present Completion-Assisted Object-CAD Alignment (CAOA), a method that integrates a semantically and contextually aware point cloud completion module with a symmetry-aware relative pose estimation algorithm, enabling precise alignment of CAD models to scanned objects. Existing completion methods are typically trained and evaluated on synthetic datasets, which often fail to generalize to real-world scans. To bridge this gap, we introduce a synthetic data generation strategy tailored to indoor scenes, significantly reducing the synthetic-to-real domain gap-validated through quantitative comparisons with widely used completion datasets. In addition, we release S2C-Completion, an expert-annotated dataset of over 8,500 object-CAD pairs from Scan2CAD, created for real-world indoor single-object completion and intended as a new benchmark for this task. For object-CAD alignment, we incorporate symmetry information via a symmetry-aware loss, improving robustness to symmetric ambiguities. On the Scan2CAD benchmark, CAOA achieves a 17% accuracy improvement over state-of-the-art methods.
