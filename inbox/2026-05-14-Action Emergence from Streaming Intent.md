---
title: "Action Emergence from Streaming Intent"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.12622
priority: medium
status: unread
interest: medium
next_step: skim
---
# Action Emergence from Streaming Intent
> 原文: [https://arxiv.org/abs/2605.12622](https://arxiv.org/abs/2605.12622)

arXiv:2605.12622v1 Announce Type: new
Abstract: We formalize action emergence as a target capability for end-to-end autonomous driving: the ability to generate physically feasible, semantically appropriate, and safety-compliant actions in arbitrary, long-tail traffic scenes through scene-conditioned reasoning rather than retrieval or interpolation of learned scene-action mappings. We show that previous paradigms cannot deliver action emergence: autoregressive trajectory decoders collapse the inherently multimodal future into a single averaged output, while diffusion and flow-matching generators express multimodality but are not steerable by reasoned intent. We propose Streaming Intent as a concrete way to approach action emergence: a mechanism that makes driving intent (i) semantically streamed through a continuous chain-of-thought that causally derives the intent from scene understanding, and (ii) temporally streamed across clips so that intent commitments remain coherent along the driving horizon. We realize Streaming Intent in a VLA model we call SI (Streaming Intent). SI autoregressively decodes a four-step chain-of-thought and emits an intent token; the decoded intent then drives classifier-free guidance (CFG) on a flow-matching action head, requiring only two denoising steps to generate the final trajectory. On the Waymo End-to-End benchmark, SI achieves competitive aggregate performance, with an RFS score of 7.96 on the validation set and 7.74 on the test set. Beyond aggregate metrics, the model demonstrates -- to our knowledge for the first time in a fully end-to-end VLA -- intent-faithful controllability: for a fixed scene, varying the intent class at inference yields qualitatively distinct yet consistently high-quality plans, arising purely from data-driven learning without any pre-built trajectory bank or hand-coded post-hoc selector.
