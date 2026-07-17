---
interest: medium
link: https://arxiv.org/abs/2607.11941
next_step: skim
priority: medium
slack_ts: '1784258636.689339'
source: cs.CV - Computer Vision
status: unread
title: 'GenDiff: A Dose and Anatomy Aware Diffusion Model with Structural Prior Refinement
  for Low-Dose CT Reconstruction and Generalization'
---
# GenDiff: A Dose and Anatomy Aware Diffusion Model with Structural Prior Refinement for Low-Dose CT Reconstruction and Generalization
> 原文: [https://arxiv.org/abs/2607.11941](https://arxiv.org/abs/2607.11941)

arXiv:2607.11941v1 Announce Type: new
Abstract: Computed tomography (CT) is a critical imaging modality for clinical diagnosis, but reducing radiation dose inevitably introduces severe noise and structured artifacts that degrade image quality. Existing deep learning-based low-dose CT (LDCT) reconstruction methods are typically optimized for fixed dose levels or specific anatomical regions, limiting their robustness and generalization in realistic clinical settings. We propose GenDiff, a generalizable diffusion-based framework for LDCT reconstruction that jointly models continuous radiation dose and anatomical information within a unified reconstruction network. The proposed framework integrates a Dose-Anatomy Encoder to learn acquisition-aware embeddings, a dose- and anatomy-conditioned cold diffusion backbone for iterative refinement, a physics-consistency update to enforce fidelity to the CT forward model, and a Structural Prior Refinement Module (SPRM) that preserves anatomical structures while suppressing dose-dependent artifacts. Extensive experiments on multi-anatomy clinical datasets, including unseen ultra-low-dose conditions as well as out-of-distribution phantom and animal datasets, demonstrate that GenDiff consistently outperforms state-of-the-art convolutional neural network and diffusion-based reconstruction methods. The proposed approach achieves superior reconstruction quality while maintaining strong robustness across different dose levels, anatomical regions, and acquisition domains, making it a promising solution for practical low-dose CT imaging.
