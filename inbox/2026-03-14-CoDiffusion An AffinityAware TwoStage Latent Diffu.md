---
interest: medium
link: https://arxiv.org/abs/2603.11125
next_step: skim
priority: medium
slack_ts: '1773974641.150479'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable
  Drug-Target Affinity Prediction'
---
# Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction
> 原文: [https://arxiv.org/abs/2603.11125](https://arxiv.org/abs/2603.11125)

arXiv:2603.11125v1 Announce Type: new
Abstract: Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.
