---
title: "Detect Early, Escalate Rarely: Anytime Detection of AI-Generated Video from the Compressed Bitstream"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.19476
priority: medium
status: unread
interest: medium
next_step: skim
---
# Detect Early, Escalate Rarely: Anytime Detection of AI-Generated Video from the Compressed Bitstream
> 原文: [https://arxiv.org/abs/2607.19476](https://arxiv.org/abs/2607.19476)

arXiv:2607.19476v1 Announce Type: new
Abstract: Detectors for AI-generated video are evaluated offline. A clip is decoded to pixels and scored once, increasingly by a large vision-language model. Detection, however, is deployed online. We recast the task as streaming perception and score the motion field the codec already wrote into the bitstream. Reading that field is a parse, not a pixel-domain forward pass. Because the running aggregate is monotone, one end-calibrated threshold is anytime-valid at the data-dependent decision time. Recalibrating at each prefix is not. Escalation is priced in closed form. A compute budget maps to a deferral window, on a frontier monotone exactly where the deferral condition holds. On matched GenVidBench the codec stage reaches full-length AUC 0.64 at five orders of magnitude less compute than a pixel CNN, on CPU. Its gate holds the stopping-time false-positive rate at target while the real data match its calibration, and drifts above it under distribution shift. Deferring 15% of clips lifts accuracy from 0.75 to 0.78 at $7\times$ less compute (paired: McNemar $p<10^{-6}$). The stage-1 ordering replicates on AIGVDBench. We introduce no new detector. The contribution is the reframing, two guarantees, and the measured frontiers. Code, configurations, and evaluation splits: https://github.com/KurbanIntelligenceLab/streamdet.
