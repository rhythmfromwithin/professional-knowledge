---
title: "DuoGesture: Neuro-Inspired and Biomechanically Informed Dual-Stream Co-Speech Gesture Generation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.26236
priority: medium
status: unread
interest: medium
next_step: skim
---
# DuoGesture: Neuro-Inspired and Biomechanically Informed Dual-Stream Co-Speech Gesture Generation
> 原文: [https://arxiv.org/abs/2605.26236](https://arxiv.org/abs/2605.26236)

arXiv:2605.26236v1 Announce Type: new
Abstract: Co-speech gesture generation requires both semantic expressivity and biomechanically plausible rhythmic motion. Existing holistic gesture models mix lexically grounded semantic gestures with frequent prosody-aligned beat gestures. This limits semantic grounding, speech-motion alignment, and kinematic smoothness. We propose \emph{DuoGesture}, a neuro-inspired and biomechanically informed dual-stream approach that decomposes co-speech gesture synthesis into coupled semantic and beat streams. The two streams are coordinated by a \emph{Semantic Variational Information Bottleneck}, a stochastic frame-level gate that learns when semantic gestures should override rhythmic beat motion. The semantic stream is controlled by \emph{Motion-Grounded Semantic Conditioning}, which replaces purely linguistic word embeddings with motion-language representations to provide motion-aligned semantic priors for long-tailed lexical triggers of gestures. The beat stream is further regularised by an \emph{Inertial Beat Prior}, an anthropometry-weighted arm-chain module that reduces jitter and improves rhythmic consistency without constraining semantic frames. Objective evaluations and subjective experiments show that DuoGesture outperforms strong holistic baselines, while component ablations confirm the complementary roles of semantic grounding, stochastic stream selection, and biomechanical regularisation.
