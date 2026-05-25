---
title: "Latent Cache Flow: Model-to-Model Communication Without Text"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.22863
priority: high
status: unread
interest: medium
next_step: skim
---
# Latent Cache Flow: Model-to-Model Communication Without Text
> 原文: [https://arxiv.org/abs/2605.22863](https://arxiv.org/abs/2605.22863)

arXiv:2605.22863v1 Announce Type: new
Abstract: LLM agents today communicate via text, which incurs considerable latency and information loss due to the need to autoregressively decode the sharer model's state and encode at the receiver model. Recent work such as Cache-to-Cache (C2C; Fu et al., 2026) seeks to exchange KV caches by learning adapters that translate sharer KV matrices to the receiver model. However, the adapters are large and expensive to train, and translate individual tokens, which requires the target context to be identical. This is unsuitable for agent communication, where the LLMs have differing context.
We introduce Latent Cache Flow (LCF). To address efficiency, we observe that keys and values can be jointly translated and compressed, reducing the adapter to about 4% of C2C's size. To address differing context, we design the adapter to transmit a summary of new information that the target model does not have. Our early experiments show that a 13 MB LCF adapter can be more accurate than a 956 MB C2C adapter in shared-context settings; for different contexts, LCF is 23% more accurate and 8.5x faster than text-based communication.
