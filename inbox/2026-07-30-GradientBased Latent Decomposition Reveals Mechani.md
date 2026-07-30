---
title: "Gradient-Based Latent Decomposition Reveals Mechanisms of Feature Degradation in Weakly Supervised Mammography"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.24835
priority: medium
status: unread
interest: medium
next_step: skim
---
# Gradient-Based Latent Decomposition Reveals Mechanisms of Feature Degradation in Weakly Supervised Mammography
> 原文: [https://arxiv.org/abs/2607.24835](https://arxiv.org/abs/2607.24835)

arXiv:2607.24835v1 Announce Type: new
Abstract: Weakly supervised hierarchical models exhibit a persistent asymmetry: coarse lesion-type features are preserved under reconstruction while fine-grained malignancy cues degrade---a pattern with direct consequences for the clinical reliability of breast cancer screening pipelines. We introduce gradient-based orthogonal latent decomposition for hierarchical Variational Autoencoders~(H-VAEs) to mechanistically explain this asymmetry. The latent space is partitioned into a task-aligned component~($z\_1$), shaped by coarse supervisory gradients, and an orthogonal residual~($z\_{\text{res}}$) capturing remaining representational capacity. On~3,550 mammographic Regions of Interest~(ROIs) from CBIS-DDSM, only~$\sim$4.4\% of latent magnitude aligns with supervisory gradients, leaving~$\sim$95.6\% in the orthogonal residual upon which fine-grained pathology prediction primarily depends. The model achieves Stage-1~AUC~0.866 and Stage 2~AUC~0.552, with a reconstruction stability gap of $\Delta\_{\text{diag}}=5\%$ ($p=0.005$) and a classification gap of $\Delta\_{\text{AUC}}=0.314$ ($p{<}0.001$). Latent ablation confirms that features for both tasks reside heavily in~$z\_{\text{res}}$, structurally explaining why reconstruction degrades pathology stability disproportionately. Comparisons with Multi-Instance Learning~(MIL) and Multi-Task Learning~(MTL) confirm generalization across architectures and modalities. These findings reveal that in high-dimensional spaces, a single coarse supervisory signal isolates only a sparse 1D latent direction, forcing critical fine-grained features into the vulnerable residual subspace.
