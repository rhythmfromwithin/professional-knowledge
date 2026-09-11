---
interest: medium
link: https://arxiv.org/abs/2609.10723
next_step: skim
priority: medium
slack_ts: '1789100106.824569'
source: cs.CV - Computer Vision
status: unread
title: 'AcFlow: Controlling Text-to-Image Diffusion Transformers via Learned Conditional
  Activation Flow'
---
# AcFlow: Controlling Text-to-Image Diffusion Transformers via Learned Conditional Activation Flow
> 原文: [https://arxiv.org/abs/2609.10723](https://arxiv.org/abs/2609.10723)

arXiv:2609.10723v1 Announce Type: new
Abstract: Text-to-image diffusion transformers (DiTs) are powerful generators, yet direct prompting provides limited control interface for style intensity and can fail to suppress unwanted concepts. To enable these controls, we introduce AcFlow, an inference-time controller that transports intermediate layer image-token activations through a learned concept-conditioned velocity field while keeping the base DiT frozen. A textual concept description specifies the desired intervention, while the integration horizon provides a continuous control parameter. The field produces token-varying, activation-dependent updates. With parameters shared across concepts within each task family, the field supports fine-grained descriptions and generalizes to concepts unseen during training without per-concept fitting. On style control, AcFlow achieves the best style--content trade-off among the evaluated baselines in the high-style-alignment regime. At a fixed operating point, AcFlow attains style--content alignment of 0.5365/0.2860, compared with 0.4397/0.2684 for the baseline with the highest style alignment. Qualitative results demonstrate suppression of diverse concepts, including cases where direct prompting fails. Our analyses support the learned velocity field as an adaptive control mechanism, with update directions varying across tokens and depend on their activation states. Our code is available at https://github.com/Nove1yst/AcFlow.
