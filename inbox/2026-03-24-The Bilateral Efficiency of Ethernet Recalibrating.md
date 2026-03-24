---
title: "The Bilateral Efficiency of Ethernet: Recalibrating Metcalfe and Boggs After Fifty Years"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.19406
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Bilateral Efficiency of Ethernet: Recalibrating Metcalfe and Boggs After Fifty Years
> 原文: [https://arxiv.org/abs/2603.19406](https://arxiv.org/abs/2603.19406)

arXiv:2603.19406v1 Announce Type: new
Abstract: In July 1976, Metcalfe and Boggs published their foundational paper on Ethernet in Communications of the ACM. Their efficiency model -- E = (P/C)/(P/C + W\*T) -- measures the fraction of Ether time carrying good forward packets under contention. For fifty years this model has defined how the networking community thinks about Ethernet performance. We argue that the model, while correct for its intended purpose, measures only the forward channel and is silent on the question that matters for modern distributed systems: bilateral transaction efficiency -- the fraction of link time that produces committed agreements between sender and receiver.
We show that Metcalfe and Boggs themselves understood this distinction intuitively. Their EFTP "end-dally" protocol (Section 7.2.2 of the original paper) is a three-phase bilateral handshake that attempts to achieve mutual knowledge of transfer completion -- precisely the property that their efficiency model cannot capture. We connect this observation to the Open Atomic Ethernet's bilateral transaction primitive, to the back-to-back Shannon channel formulation with Perfect Information Feedback, and to the Two-State Vector Formalism (TSVF) from physics, which provides the theoretical framework for understanding why both boundary conditions -- sender and receiver -- must be specified for a transaction to have definite value.
The correction to Table 1 of Metcalfe and Boggs is not a different set of numbers. It is a different question.
