---
interest: medium
link: https://arxiv.org/abs/2605.00052
next_step: skim
priority: medium
slack_ts: '1777952335.989439'
source: cs.CV - Computer Vision
status: unread
title: 'Two-View Accumulation as the Primary Training Lever for Hybrid-Capture Gaussian
  Splatting: A Variance-Decomposition View of When Gradient Surgery Helps'
---
# Two-View Accumulation as the Primary Training Lever for Hybrid-Capture Gaussian Splatting: A Variance-Decomposition View of When Gradient Surgery Helps
> 原文: [https://arxiv.org/abs/2605.00052](https://arxiv.org/abs/2605.00052)

arXiv:2605.00052v1 Announce Type: new
Abstract: Hybrid-capture novel view synthesis combines images at substantially different camera distances (e.g., aerial drone and ground-level views). Standard 3D Gaussian Splatting (3DGS), trained for 30K iterations with one rendered view per optimizer step, under-fits the minority regime by 1-3 dB on five hybrid-capture benchmarks. We isolate the lever that closes this gap.
Among compute-matched alternatives -- vanilla 60K iterations, magnitude corrections (GradNorm), direction-aware near/far gradient surgery, projective preconditioning, confidence-gated sample-level surgery, and a random two-view-per-step control -- the simplest structural change wins: rendering two views per optimizer step. The pairing rule (geometry-defined near/far, random, or active loss-disparity) does not change PSNR beyond seed variance on any of the five scenes; the structural change of having two views per step does.
We propose a variance-decomposition framework that predicts and explains this finding: under bimodal camera regimes, between-regime gradient variance turns out to be small relative to within-regime variance in 3DGS, so structured and random pairings are variance-equivalent in expectation, and the variance halving from two-view accumulation itself is the dominant effect. We verify the framework on five scenes whose camera-altitude bimodality coefficients span [0.55, 1.00], and we report the negative result that direction-aware projection, magnitude correction, confidence gating, and an active loss-disparity pairing all fall within seed variance of random two-view pairing. The two-view structural lever transfers cleanly to the Scaffold-GS and Pixel-GS backbones.
We position this work as an honest characterization of which training-side axes do and do not move PSNR for hybrid-capture 3DGS, together with the framework that explains why.
