---
title: "Brief Announcement: Generative Markov Model for Distributed Computing Systems"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.03061
priority: medium
status: unread
interest: medium
next_step: skim
---
# Brief Announcement: Generative Markov Model for Distributed Computing Systems
> 原文: [https://arxiv.org/abs/2606.03061](https://arxiv.org/abs/2606.03061)

arXiv:2606.03061v1 Announce Type: new
Abstract: Emerging distributed computing paradigms, such as the computing continuum, are inherently heterogeneous, stochastic, and complex. Efficiently and effectively utilizing all available resources across the continuum demands a unified formal model of the system. To address this gap, we propose a general framework for modeling distributed computing systems as a generative Markov model, factorized over a structured system state. In our model, the state decomposes into high-dimensional variables, each further factorized over its elements, reflecting the sparse dependency structure inherent to distributed systems. This yields a tractable model enabling simulation, inference, and policy learning over otherwise intractable system states, bridging distributed computing with Markov chain theory and reinforcement learning (RL). We demonstrate our framework through a case study of collaborative AI inference, in which a dedicated server combines resources with those volunteered by service users. Our results show that centralized scheduling becomes a bottleneck at scale, while distributing computation across user devices reduces both latency and server resource consumption. These findings highlight the value of adaptive decision-making in distributed computing systems and demonstrate the framework's utility for modeling, simulation, and optimization.
