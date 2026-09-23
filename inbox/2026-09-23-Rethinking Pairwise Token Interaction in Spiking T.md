---
title: "Rethinking Pairwise Token Interaction in Spiking Transformers"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2609.26297
priority: low
status: unread
interest: medium
next_step: skim
---
# Rethinking Pairwise Token Interaction in Spiking Transformers
> 原文: [https://arxiv.org/abs/2609.26297](https://arxiv.org/abs/2609.26297)

arXiv:2609.26297v1 Announce Type: new
Abstract: Spiking Transformers inherit token interaction mechanisms from conventional Transformers, yet their sparse binary representations fundamentally alter how token-to-token communication is established. In particular, spike-based query-key matching produces highly sparse and input-dependent interaction patterns, coupling information propagation to the instantaneous availability of matching spike events. This motivates a different interaction paradigm in which long-range communication does not rely solely on pairwise spike coincidence. We therefore propose Gated Spike Axial Propagation (GSAP), a spike-native token interaction mechanism that decouples information propagation from context selection. Instead of directly determining communication through query-key matching, GSAP first propagates spike-based context along the horizontal and vertical axes, allowing information to reach distant tokens through structured sequential propagation. A receiver-conditioned gate then determines how much of the propagated context is incorporated at each token, while a lightweight local pathway preserves fine-grained neighborhood information. In this way, GSAP reformulates token interaction as a propagate-then-select process, enabling structured long-range communication while retaining the sparse event-driven nature of spiking representations. Code is available at https://github.com/Fancyssc/GSAP.
