---
interest: medium
link: https://arxiv.org/abs/2611.07159
next_step: skim
priority: low
slack_ts: '1794029941.192259'
source: cs.CR - Cryptography and Security
status: unread
title: 'Beyond Proof of Possession: A Relational Theory of Authority'
---
# Beyond Proof of Possession: A Relational Theory of Authority
> 原文: [https://arxiv.org/abs/2611.07159](https://arxiv.org/abs/2611.07159)

arXiv:2611.07159v1 Announce Type: new
Abstract: Proof-of-Possession (PoP) establishes that an executor controls an artifact (key, token, credential, or capability), but such control alone determines neither the executor's relational profile nor the causal history of an execution occurrence. We separate PoP from Proof of Relationship (PoR), the semantic property that one execution occurrence validly continues another, and from authorization, which is occurrence-sensitive. The foundational change is in the semantic domain of authorization: from holders and authority-bearing artifacts to execution occurrences situated in causal histories. We give authorization models an observation-based occurrence verdict and a separate transition-admissibility relation; kernel inclusion yields a partial order on observation-kernel classes. Building on Provenance Identity Continuity (PIC) and Proof-of-Continuity (PoC), we classify executors by authorization-relevant equivalence relations whose quotients form relational profile spaces, with positive predicates over profile transitions forming a distributive lattice. This adds relational attenuation to authority attenuation: along a valid causal history, $C\_{i+1}\subseteq C\_i$ and $\rho\_{i+1}\Rightarrow\rho\_i$. We prove dual monotonicity, combined closure, and origin relational closure. Two occurrences of the same authenticated executor, with the same profile and possession evidence, need not be authorization-equivalent, and within a valid PIC lineage a deputy's independent authority cannot be imported outside the origin context. Finally, we prove that the executor-dependent decision factors through the relational profile and is invariant under sound mechanisms establishing it: successor-side PoP is a possible evidence mechanism, not a necessary premise of authorization. Under explicit Witness Assumptions, a boundary-witnessed checkpoint construction realizes the premises without successor-side PoP.
