---
title: "On the Computational Complexity of Structural Generalization"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.19573
priority: high
status: unread
interest: medium
next_step: skim
---
# On the Computational Complexity of Structural Generalization
> 原文: [https://arxiv.org/abs/2607.19573](https://arxiv.org/abs/2607.19573)

arXiv:2607.19573v1 Announce Type: new
Abstract: Structural generalization has been measured repeatedly by several benchmarks, yet it has never been formally defined. We give a definition that translates the two premises (compositional structure and unbounded generalization) into mathematical language. The definition itself is neutral: a compiler that hard-codes the rules satisfies it just as well. But structural generalization becomes a scientific question only insofar as the capacity can autonomously emerge from finite data. This question pits the computational lower bound $\mathrm{NC}^1$ against the learnable ceiling $\mathrm{TC}^0$ of pure Transformers. Under a Montagovian instantiation, each compositional rule splits into two projections: a syntactic face ($F\_\gamma$) and a semantic face ($G\_\gamma$). Tree evaluation on the $G\_\gamma$ side is an instantiation of BFVP, which is $\mathrm{NC}^1$-complete (Buss, 1987). A pure Transformer must learn both faces at once, but Kraus et al. (2026) prove that its learnable class $\subseteq \mathrm{TC}^0$. Under the standard assumption $\mathrm{TC}^0 \neq \mathrm{NC}^1$, a pure Transformer cannot learn structural generalization. Neuro-symbolic systems achieve the best benchmark scores precisely because they inject $G\_\gamma$, sidestepping the genuinely hard half. Benchmark scores cannot distinguish "learned" from "given." This is what this paper sets out to make clear.
