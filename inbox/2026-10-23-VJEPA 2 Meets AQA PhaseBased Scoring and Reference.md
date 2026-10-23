---
title: "V-JEPA 2 Meets AQA: Phase-Based Scoring and Reference-Based Feedback for Mountain Biking"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.30160
priority: medium
status: unread
interest: medium
next_step: skim
---
# V-JEPA 2 Meets AQA: Phase-Based Scoring and Reference-Based Feedback for Mountain Biking
> 原文: [https://arxiv.org/abs/2610.30160](https://arxiv.org/abs/2610.30160)

arXiv:2610.30160v1 Announce Type: new
Abstract: We study mountain-bike action quality assessment (AQA) with weak labels and candidate feedback. The training corpus comprises 95 field-recorded jump clips with binary labels denoting good or poor technique. These are coarse categorical labels, not continuous expert quality scores; phase-boundary and aspect-level annotations are unavailable. Our pipeline summarizes four heuristic phases using frozen V-JEPA 2 video features and two-dimensional pose and motion measurements. A small transformer predicts a binary-label score. A separate reference layer compares phase-specific measurements with those of clips labelled as good technique to propose phase, body-parameter, and direction cues. We detail the measurements, network, and evaluation so that the limits of each output are explicit. In five-fold clip-level cross-validation, the full scorer obtained pooled out-of-fold AUROC 0.768 and average precision 0.812. These are exploratory figures because the reporting fold also selected the neural training epoch and riders were not separated between folds. Removing biomechanical scoring inputs raised AUROC to 0.809. A separate inner-selection run obtained AUROC 0.678, but used about 57 rather than 76 training clips per outer fold, so its difference from the test-selected run does not quantify selection bias. The unsupervised aspect head did not learn distinct factors. On a 17-clip external probe, an earlier checkpoint obtained binary accuracy 0.412 and Spearman association -0.135 with expert scores. Candidate cues had precision 0.118 and recall 1.0 against each of two coaches, with substantial disagreement about direction. These findings do not establish rider-independent scoring or reliable corrective feedback; they identify the empirical work needed to evaluate either use.
