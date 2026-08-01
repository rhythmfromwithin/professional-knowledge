---
interest: medium
link: https://arxiv.org/abs/2607.27292
next_step: skim
priority: medium
slack_ts: '1785555399.760609'
source: cs.CV - Computer Vision
status: unread
title: 'VETO: Towards Protecting Images From Frontier AI Editing'
---
# VETO: Towards Protecting Images From Frontier AI Editing
> 原文: [https://arxiv.org/abs/2607.27292](https://arxiv.org/abs/2607.27292)

arXiv:2607.27292v1 Announce Type: new
Abstract: The rise of powerful, accessible image-editing models such as FLUX.2 has brought high-fidelity editing within broad reach. Their capabilities now extend beyond localized modifications to extracting and recontextualizing objects and identities in entirely new scenes. By allowing prompt and generation tokens to attend directly to reference-image tokens, modern models blur the boundary between conventional editing and text-to-image synthesis. This expanded generative freedom also broadens the space of potential misuse, as harmful transformations are no longer confined to a predictable set of localized edits. Existing anti-edit defenses are designed to disrupt the semantic bottleneck of the reference-image encoding in legacy diffusion pipelines. However, newer editors distill reference information through joint-attention blocks, thereby often circumventing these protections. We therefore introduce VETO, a subtle anti-edit cloak that disrupts this inner mechanism through which modern models read the source image. Additionally, as existing editing benchmarks leave comprehensive recontextualizations largely untested, we introduce VetoBench, which evaluates defenses not only on conventional localized edits but also on broader contextual shifts. Across two contemporary editing models and three benchmarks, VETO consistently outperforms existing defenses while providing a stronger protection-fidelity trade-off.
