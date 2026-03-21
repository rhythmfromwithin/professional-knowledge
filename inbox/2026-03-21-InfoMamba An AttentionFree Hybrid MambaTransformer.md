---
title: "InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.18031
priority: high
status: unread
interest: medium
next_step: skim
---
# InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model
> 原文: [https://arxiv.org/abs/2603.18031](https://arxiv.org/abs/2603.18031)

arXiv:2603.18031v1 Announce Type: new
Abstract: Balancing fine-grained local modeling with long-range dependency capture under computational constraints remains a central challenge in sequence modeling. While Transformers provide strong token mixing, they suffer from quadratic complexity, whereas Mamba-style selective state-space models (SSMs) scale linearly but often struggle to capture high-rank and synchronous global interactions. We present a consistency boundary analysis that characterizes when diagonal short-memory SSMs can approximate causal attention and identifies structural gaps that remain. Motivated by this analysis, we propose InfoMamba, an attention-free hybrid architecture. InfoMamba replaces token-level self-attention with a concept bottleneck linear filtering layer that serves as a minimal-bandwidth global interface and integrates it with a selective recurrent stream through information-maximizing fusion (IMF). IMF dynamically injects global context into the SSM dynamics and encourages complementary information usage through a mutual-information-inspired objective. Extensive experiments on classification, dense prediction, and non-vision tasks show that InfoMamba consistently outperforms strong Transformer and SSM baselines, achieving competitive accuracy-efficiency trade-offs while maintaining near-linear scaling.
