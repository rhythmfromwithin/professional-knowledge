---
title: "Position: Quantum Program Generation Must Prioritize Validity Over Probabilistic Scaling"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.15313
priority: high
status: unread
interest: medium
next_step: skim
---
# Position: Quantum Program Generation Must Prioritize Validity Over Probabilistic Scaling
> 原文: [https://arxiv.org/abs/2607.15313](https://arxiv.org/abs/2607.15313)

arXiv:2607.15313v1 Announce Type: new
Abstract: The scaling hypothesis assumes that increasing model parameters yields emergent reasoning capabilities. This position paper argues that applying this probabilistic paradigm to generic quantum circuit synthesis is a directional error. Unlike natural languages, quantum circuits require strict adherence to mathematical constraints that manifest a significant syntax-semantics gap. Training on unverified quantum programs means that models learn syntax but fail to capture the physical semantics of the Hilbert space. Since the valid subset of circuit designs decays exponentially with the number of qubits, post-hoc filtering is mathematically intractable. We propose a pivot from human-centric copilots to verifier-centric agents. We integrate hierarchical constraints, topological masks, and symbolic proxies directly into generation. Our analysis suggests that scale alone cannot bridge the validity gap. Verification-aware architectures offer a viable path for modular quantum program generation. These considerations point toward generation methods that encode task-specific rules of quantum information, rather than relying on imitation alone.
