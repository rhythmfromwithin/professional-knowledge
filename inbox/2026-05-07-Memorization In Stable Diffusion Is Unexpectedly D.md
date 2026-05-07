---
title: "Memorization In Stable Diffusion Is Unexpectedly Driven by CLIP Embeddings"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.02908
priority: medium
status: unread
interest: medium
next_step: skim
---
# Memorization In Stable Diffusion Is Unexpectedly Driven by CLIP Embeddings
> 原文: [https://arxiv.org/abs/2605.02908](https://arxiv.org/abs/2605.02908)

arXiv:2605.02908v1 Announce Type: new
Abstract: Understanding how textual embeddings contribute to memorization in text-to-image diffusion models is crucial for both interpretability and safety. This paper investigates an unexpected behavior of CLIP embeddings in Stable Diffusion, revealing that the model disproportionately relies on specific embeddings. We categorize input tokens as , , and with corresponding embeddings $\mathbf{v}^{\mathbf{sot}}, \mathbf{v}^{\mathbf{pr}}, \mathbf{v}^{\mathbf{eot}}, \mathbf{v}^{\mathbf{pad}}$. We discover that $\mathbf{v}^{\mathbf{pr}}$ contribute minimally to generation in memorized cases. In contrast, $\mathbf{v}^{\mathbf{pad}}$ strongly affect memorization due to their structural duplication of $\mathbf{v}^{\mathbf{eot}}$, the only embedding explicitly optimized during CLIP training. This duplication unintentionally amplifies the influence of $\mathbf{v}^{\mathbf{eot}}$, causing the model to over-rely on it, thereby driving memorization. Based on these observations, we propose two simple yet effective inference-time mitigation strategies: (1) Replacing the tokenizer's default from to the ! token before embedding, and masking the $\mathbf{v}^{\mathbf{eot}}$; (2) Partial masking of $\mathbf{v}^{\mathbf{pad}}$. Both suppress memorization without degrading quality, and are readily deployable without prior detection.
