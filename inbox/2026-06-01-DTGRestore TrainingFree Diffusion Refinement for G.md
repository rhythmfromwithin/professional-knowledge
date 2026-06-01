---
title: "DTG-Restore: Training-Free Diffusion Refinement for Generative Video Super-Resolution"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.30431
priority: medium
status: unread
interest: medium
next_step: skim
---
# DTG-Restore: Training-Free Diffusion Refinement for Generative Video Super-Resolution
> 原文: [https://arxiv.org/abs/2605.30431](https://arxiv.org/abs/2605.30431)

arXiv:2605.30431v1 Announce Type: new
Abstract: Recent progress in video diffusion models has enabled remarkable generative fidelity, yet leveraging these priors for restoration remains limited by the strong coupling between conditional and unconditional branches in standard classifier-free guidance. We introduce a training-free framework that enhances distorted and low-resolution videos by decoupling these signals in time. Our proposed Decoupled Time Guidance (DTG) evaluates the unconditional branch at a cleaner diffusion timestep, providing a lookahead prior that preserves geometry while suppressing replication of warped content. This temporal bias is annealed throughout sampling, allowing the model to transition from structure correction to detail refinement without retraining. Combined with any off-the-shelf restoration module in a plug-and-play manner, our approach improves perceptual coherence and restores plausible structure in AIgenerated and real-world videos alike. To facilitate evaluation, we curate GenWarp480, a benchmark of 4,400 distorted 480p videos synthesized from diverse text-to-video models. GenWarp480 focuses on characteristic generative degradations such as warped faces, body misalignments, and spatial artifacts, providing a purpose-built testbed for assessing robustness to generative errors. Extensive experiments demonstrate that our method achieves significant improvements in structural fidelity and temporal stability without any model training.
