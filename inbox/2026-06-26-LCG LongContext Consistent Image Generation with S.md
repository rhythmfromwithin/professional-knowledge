---
interest: medium
link: https://arxiv.org/abs/2606.26171
next_step: skim
priority: medium
slack_ts: '1782447550.575179'
source: cs.CV - Computer Vision
status: unread
title: 'LCG: Long-Context Consistent Image Generation with Sparse Relational Attention'
---
# LCG: Long-Context Consistent Image Generation with Sparse Relational Attention
> 原文: [https://arxiv.org/abs/2606.26171](https://arxiv.org/abs/2606.26171)

arXiv:2606.26171v1 Announce Type: new
Abstract: Recent image generation models achieve impressive quality in single-image synthesis, but often fail to maintain consistency across sequential outputs, as required in comics, storyboards, and visual narratives. We propose Long-Context Generation (LCG), a framework for long-context multi-image text-to-image generation, to improve consistency and scalability in long-context multi-image generation. LCG employs the Sparse Relational Attention (SRA) mechanism to selectively attend to core features across extended visual contexts, ensuring that the propagation of semantic and layout information remains computationally tractable. To enforce semantic alignment, we introduce the Routing Consistency Constraint (RCC), which leverages identity-aware masks to align structural patterns across generation branches, effectively mitigating drift in appearance even in complex multi-character scenes. To support training and evaluation in this setting, we construct the Long-Context Consistency Dataset (LCCD), a large-scale synthetic dataset comprising character-centric multi-image sequences spanning varied situational contexts. LCCD contains 600K training sequences and a separate 1K test set, with each sequence containing 6 to 20 images. The experiments demonstrate that LCG outperforms the compared baselines in prompt alignment and character consistency for long-context image generation, including multi-character scenes.
