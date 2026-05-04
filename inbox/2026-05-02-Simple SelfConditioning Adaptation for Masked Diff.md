---
interest: medium
link: https://arxiv.org/abs/2604.26985
next_step: skim
priority: high
slack_ts: '1777866890.659729'
source: cs.LG - Machine Learning
status: unread
title: Simple Self-Conditioning Adaptation for Masked Diffusion Models
---
# Simple Self-Conditioning Adaptation for Masked Diffusion Models
> 原文: [https://arxiv.org/abs/2604.26985](https://arxiv.org/abs/2604.26985)

arXiv:2604.26985v1 Announce Type: new
Abstract: Masked diffusion models (MDMs) generate discrete sequences by iterative denoising under an absorbing masking process. In standard masked diffusion, if a token remains masked after a reverse update, the model discards its clean-state prediction for that position. Thus, still-masked positions must be repeatedly inferred from the mask token alone. This design choice limits cross-step refinement. To address this limitation, this paper proposes a simple, yet effective, post-training adaptation for MDMs that conditions each denoising step on the model's own previous clean-state predictions. The resulting method, called Self-Conditioned Masked Diffusion Models (SCMDM), requires minimal architectural change, does not introduce a recurrent latent-state pathway, does not rely on an auxiliary reference model, and adds no extra denoiser evaluations during sampling. This is an important departure from partial self-conditioning approaches which requires expensive model training from scratch. In particular, the paper shows that partial self-conditioning, including the commonly used 50% dropout strategy for training self-conditioned models from scratch, is suboptimal in the post-training regime. Instead, once the model's self-generated clean-state estimates become informative, the specialization to refinement is preferable to mixing conditional and unconditional objectives. SCMDM is evaluated across multiple domains, demonstrating consistent improvement over vanilla MDM baselines, achieving nearly a 50% reduction in generative perplexity on OWT-trained models (42.89 to 23.72), alongside strong improvements in discretized image synthesis quality, small molecular generation, and enhanced fidelity in genomic distribution modeling.
