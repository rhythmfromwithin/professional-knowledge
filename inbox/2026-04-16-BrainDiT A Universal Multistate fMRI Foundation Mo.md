---
title: "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2604.12683
priority: low
status: unread
interest: medium
next_step: skim
---
# Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining
> 原文: [https://arxiv.org/abs/2604.12683](https://arxiv.org/abs/2604.12683)

arXiv:2604.12683v1 Announce Type: cross
Abstract: Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. We present \textit{Brain-DiT}, a universal multi-state fMRI foundation model pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Unlike prior fMRI foundation models that rely on masked reconstruction in the raw-signal space or a latent space, \textit{Brain-DiT} adopts metadata-conditioned diffusion pretraining with a Diffusion Transformer (DiT), enabling the model to learn multi-scale representations that capture both fine-grained functional structure and global semantics. Across extensive evaluations and ablations on 7 downstream tasks, we find consistent evidence that diffusion-based generative pretraining is a stronger proxy than reconstruction or alignment, with metadata-conditioned pretraining further improving downstream performance by disentangling intrinsic neural dynamics from population-level variability. We also observe that downstream tasks exhibit distinct preferences for representational scale: ADNI classification benefits more from global semantic representations, whereas age/sex prediction comparatively relies more on fine-grained local structure. Code and parameters of Brain-DiT are available at \href{https://github.com/REDMAO4869/Brain-DiT}{Link}.
