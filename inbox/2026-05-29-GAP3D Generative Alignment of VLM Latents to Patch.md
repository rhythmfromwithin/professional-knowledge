---
interest: medium
link: https://arxiv.org/abs/2605.28995
next_step: skim
priority: medium
slack_ts: '1780028402.274289'
source: cs.CV - Computer Vision
status: unread
title: 'GAP3D: Generative Alignment of VLM Latents to Patch-Level Embeddings for 3D
  Generation'
---
# GAP3D: Generative Alignment of VLM Latents to Patch-Level Embeddings for 3D Generation
> 原文: [https://arxiv.org/abs/2605.28995](https://arxiv.org/abs/2605.28995)

arXiv:2605.28995v1 Announce Type: new
Abstract: Recent approaches integrating vision-language models (VLMs) as prompt encoders for generative model conditioning typically rely on expensive end-to-end training or map features to compressed representations, discarding the dense spatial structure required for geometry-aware tasks like 3D asset generation. To address this, we propose GAP3D, a modular, diffusion-based approach that aligns VLM-generated latents directly to the complete, patch-level feature space of a pre-trained image encoder, enabling a frozen downstream generative model to utilize a VLM as prompt encoder while maintaining a spatially structured conditioning signal. Evaluated on 3D asset generation, our method bypasses the need for large-scale 3D data by training mainly on general-domain image-text pairs. It also exhibits emergent zero-shot capabilities for multimodal prompts, despite being trained exclusively on text input. Finally, while currently prioritizing high-level semantics over fine-grained detail, GAP3D demonstrates that the representation gap between VLM and image-encoder feature spaces can be partially bridged through diffusion-based alignment, taking the first steps towards a modular integration of foundation models through generative alignment to dense embedding spaces.
