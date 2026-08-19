---
title: "Deep Analog: Open-Set Film Emulation with Reference-Conditioned 3D LUTs"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.14702
priority: medium
status: unread
interest: medium
next_step: skim
---
# Deep Analog: Open-Set Film Emulation with Reference-Conditioned 3D LUTs
> 原文: [https://arxiv.org/abs/2608.14702](https://arxiv.org/abs/2608.14702)

arXiv:2608.14702v1 Announce Type: new
Abstract: Film emulation reproduces the look of an analog film stock on a new digital photograph. We target its open-set form -- matching any reference film frame from a single example -- with a 3D lookup table (LUT) predicted from that reference. Real-time image enhancement predicts per-image weights over a fixed bank of 3D LUTs and blends them. We show this is a gated mixture of experts and inherits its failure: trained end-to-end against reconstruction, the gate collapses onto a single expert, so a bank of K LUTs delivers the capacity of one. An entropy term, the enhancement-setting analogue of mixture-of-experts load balancing, restores utilization and recovers about 1 dB PSNR. The deeper constraint survives: a fixed LUT basis is closed-set, freezing the achievable looks at training time. We therefore discard the basis and predict a single 3D LUT as a residual from a reference image (StyleLUTNet), trained by self-supervision on procedurally generated color transforms. The conditional design removes the gate and generalizes open-set to unseen film stocks without paired data or retraining. Around this color backbone we build Deep Analog, a film-emulation pipeline that adds histogram-based tone matching and a physics-informed optical renderer -- multi-scale grain and per-channel halation driven by parameters an inverse network regresses from the reference. On 350 self-supervised pairs the color stage reaches 22.05 dB PSNR / 0.925 SSIM and the full pipeline 21.72 dB / 0.923; the color path runs in 5.2 ms at 1080p (192 FPS) and exports a portable .cube LUT for standard editing tools. A second degeneracy in conditional LUT training -- residual-scale collapse -- shares the root cause and yields a general principle: auxiliary regularization must stay subordinate to reconstruction.
