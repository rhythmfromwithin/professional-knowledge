---
interest: medium
link: https://arxiv.org/abs/2609.04501
next_step: skim
priority: low
slack_ts: '1788840721.317359'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'EyeMakeYou: Identity-, Task-, and Subjective-State-Conditioned Diffusion for
  High-Frequency Gaze Synthesis'
---
# EyeMakeYou: Identity-, Task-, and Subjective-State-Conditioned Diffusion for High-Frequency Gaze Synthesis
> 原文: [https://arxiv.org/abs/2609.04501](https://arxiv.org/abs/2609.04501)

arXiv:2609.04501v1 Announce Type: new
Abstract: Eye movement biometrics (EMB) is an emerging behavioral modality for user authentication, particularly in virtual- and augmented-reality systems, where gaze dynamics contain distinctive subject-specific features. However, robust EMB systems require diverse, high-quality gaze recordings that are expensive to collect and often unavailable at the scale needed for model development. Generative models can mitigate data scarcity, but existing methods either synthesize generic gaze behavior or personalize signals primarily by identity, without jointly representing the user's task and subjective state. Consequently, generated signals may appear visually realistic while failing to retain the behavioral properties required for biometric applications. To address this limitation, we propose EyeMakeYou, a multi-conditional denoising diffusion framework for subject-specific, high-frequency gaze synthesis. EyeMakeYou generates 5-s, 1000-Hz bivariate gaze-velocity sequences from an identity-removed reference trajectory and conditions the denoising process on an identity embedding, a task embedding, and self-reported ratings of overall difficulty, mental tiredness, and eye tiredness. Its objective combines diffusion noise prediction and identity preservation with multi-resolution spectral, drift-consistency, and event-weighted local-smoothness losses. Experiments on GazeBase show that EyeMakeYou achieves higher median spatial accuracy and greater real--synthetic similarity in the embedding feature space than the existing generative approaches, while retaining selected task-dependent associations between subjective reports and oculomotor features. These findings support conditional diffusion as a practical approach for augmenting gaze datasets for biometric and interactive applications.
