---
interest: medium
link: https://arxiv.org/abs/2609.12099
next_step: skim
priority: medium
slack_ts: '1789360364.497629'
source: cs.CV - Computer Vision
status: unread
title: 'Beyond Argmax: A Mechanistic Study of Semantic Retention in Frozen Foundation-Model
  Composition for Generalized Few-Shot 3D Segmentation'
---
# Beyond Argmax: A Mechanistic Study of Semantic Retention in Frozen Foundation-Model Composition for Generalized Few-Shot 3D Segmentation
> 原文: [https://arxiv.org/abs/2609.12099](https://arxiv.org/abs/2609.12099)

arXiv:2609.12099v1 Announce Type: new
Abstract: Classical classifier-combination work distinguishes score-level fusion from hard decision-level voting. We revisit this distinction where independently pretrained, frozen foundation models are composed at inference time for generalized few-shot 3D segmentation. We ask: how much useful semantic information is lost when heterogeneous sources are collapsed to a single class before they can interact?
We answer with a same-input semantic-retention intervention. Dense RegionPLC and sparse cross-view SAM3 evidence, model weights, masks, geometry, vocabularies, and fusion rules are frozen; only the number of semantic alternatives retained before interaction is varied via a matched top-k ladder. On 156 held-out ScanNet200 scenes, top-1 reaches 28.47 harmonic-mean (HM) IoU while full distribution fusion reaches 34.87 HM (+6.40, 95% CI [+5.24,+7.64]). The pattern replicates on 50 ScanNet++ scenes: 23.02 vs. 26.50 HM (+3.48, 95% CI [+1.64,+5.93]).
The conclusion is robust: full-distribution HM is stable across sparse-source weights 0.3--0.7; alternative operators (max, geometric pooling) also outperform top-1; and a GroundingDINO--SAM2.1 source-replacement diagnostic shows monotonic HM increase from 14.77 to 18.75 with full retention. Calibration diagnostics reveal opposite miscalibration of the two sources, yet correcting calibration does not eliminate the retention advantage.
Across datasets and source stacks, most information is recovered by retaining a compact set of plausible alternatives. The contribution is a controlled diagnosis of premature semantic collapse as a repeatable information bottleneck in heterogeneous frozen-model composition.
