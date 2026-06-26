---
interest: medium
link: https://arxiv.org/abs/2606.26199
next_step: skim
priority: low
slack_ts: '1782447551.035549'
source: cs.CR - Cryptography and Security
status: unread
title: 'MIRAGE: Protecting against Malicious Image Editing via False Moderation'
---
# MIRAGE: Protecting against Malicious Image Editing via False Moderation
> 原文: [https://arxiv.org/abs/2606.26199](https://arxiv.org/abs/2606.26199)

arXiv:2606.26199v1 Announce Type: new
Abstract: The proliferation of AI-powered image editing systems raises serious concerns because it allows personal images to be arbitrarily manipulated at scale, with minimal effort, and a lower barrier to entry. Prior work on image immunization adds imperceptible perturbations to an image to protect against unauthorized manipulations. However, these methods usually require access to the model weights and the image manipulating prompt. This significantly limits their use, especially against powerful commercial image-editors such as GPT-Image, Gemini Flash Image (Nano Banana), and Grok Imagine. To address this, we take a system-level view of the problem and identify a previously unexplored attack surface common to all major commercial image editing systems: pre-generation safety moderation.Rather than disrupting the generative model itself, we propose to immunize images by causing these moderation classifiers to flag images as policy-violating, triggering an automatic refusal regardless of the editing prompt. We operationalize this by adding adversarial perturbations to align our image to policy-violating concepts in the representation space of an ensemble of open-source embedding and moderation models. We call our method MIRAGE, which stands for Moderation Induced Resistance Against Generative Editing. We evaluate MIRAGE against multiple closed-source image editing APIs and demonstrate success rates of more than 88%. Our approach is simple, prompt-agnostic, and effective, offering a practical path towards protecting personal images from unauthorized AI-powered editing.
