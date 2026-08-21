---
interest: medium
link: https://arxiv.org/abs/2608.13570
next_step: skim
priority: high
slack_ts: '1787276735.851379'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Think in Latent, Explain in Language: Self-Explainable Latent Reasoning'
---
# Think in Latent, Explain in Language: Self-Explainable Latent Reasoning
> 原文: [https://arxiv.org/abs/2608.13570](https://arxiv.org/abs/2608.13570)

arXiv:2608.13570v1 Announce Type: new
Abstract: Latent reasoning has emerged as a powerful alternative to text-based Chain-of-Thought (CoT), offering significant gains in computational efficiency by compressing verbose reasoning into compact embeddings. However, compressing reasoning into the latent space renders the thinking opaque, hindering its interpretability. Current methods present a stark trade-off: they either function as unexplainable ''black boxes'' (e.g., Coconut), where the latent reasoning is not human-readable, or rely on separate post-hoc decoders for explainability (e.g., Heima), introducing architectural overhead and decoupling the explanation from the actual reasoning process. In this work, we present a unified framework for Self-Explainable Latent Reasoning (SELR) that trains a single model to perform efficient and inherently explainable latent reasoning. Our core contribution is a novel multi-task training objective that optimizes for two goals simultaneously: (1) an Answer Loss that optimizes the latent reasoning trajectory to produce accurate final answers, and (2) a CoT Loss that explicitly trains the same model to decode its own latent representations back into human-understandable reasoning steps. This design ensures that generated latent representations are both task-effective and semantically interpretable, eliminating the need for external decoders. We validate the effectiveness of SELR on both Large Language Models (LLMs) and Vision-Language Models (VLMs), demonstrating that SELR achieves superior token efficiency and accuracy compared to baselines, while uniquely providing self-contained explainability without auxiliary models. Project page is available at https://jasondayuan.github.io/SELR/.
