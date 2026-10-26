---
title: "Democratizing LLM Training with the Edge: Challenges, Systems, and the Road Ahead"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.32215
priority: medium
status: unread
interest: medium
next_step: skim
---
# Democratizing LLM Training with the Edge: Challenges, Systems, and the Road Ahead
> 原文: [https://arxiv.org/abs/2610.32215](https://arxiv.org/abs/2610.32215)

arXiv:2610.32215v1 Announce Type: new
Abstract: The growing computational power of modern GPU data centers has let a few industrial giants train and deploy large language models (LLMs) on massive amounts of data. Yet the sheer scale of these models and their training data makes centralized development increasingly hard to sustain, and at the same time shuts out smaller institutions that hold relevant private data but lack comparable infrastructure. In this paper, we organize our positions on distributed LLM training around the pretraining and fine-tuning paradigms, covering federated learning, split learning, and decentralized approaches, and we assess their readiness for geo-distributed settings with heterogeneous hardware and unreliable connectivity. We then present a {\em unified} system architecture built around a cloud-hosted parameter server that coordinates heterogeneous clients over outbound gRPC connections, reusing one communication, compression, and fault-tolerance stack for both pretraining and a family of fine-tuning methods. We validate the design with real geo-distributed experiments on GPT-2 Medium and Llama3-1B pretraining across multiple university sites, showing stable convergence under realistic conditions. Finally, we chart the road ahead, identifying open problems that span frontier model support, elastic fault tolerance, adaptive compression, federated alignment, privacy and trust, incentive design, and system--algorithm co-design, all of which must be addressed to make democratized LLM training a reality.
