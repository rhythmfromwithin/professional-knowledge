---
title: "A Causal Energy Prior for Learning Directed Acyclic Graphs"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.33225
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Causal Energy Prior for Learning Directed Acyclic Graphs
> 原文: [https://arxiv.org/abs/2611.33225](https://arxiv.org/abs/2611.33225)

arXiv:2611.33225v1 Announce Type: new
Abstract: Bayesian learning of directed acyclic graphs (DAGs) has long relied on non- or weakly informative priors, on the assumption that the information needed for an informative one is rarely available. In genetics and systems biology, annotation databases now make it possible to assemble a prior DAG before learning from data. Existing informative priors are local: they score a DAG arc by arc and cannot encode how interventions propagate along its paths. Thus, we propose the local-global energy prior (LGE), a Gibbs distribution over DAGs whose energy combines a local divergence from the prior DAG, the Structural Hamming Distance, and a causal one, the Structural Intervention Distance. We derive rules to calibrate its decay and the weight of the two divergences from the prior DAG alone. We quantify how much prior mass stays on the true DAG, and how much data overturn the prior, when the prior DAG is partially incorrect. In simulations, LGE improves both the structural accuracy of maximum a posteriori DAGs and the fit of the corresponding Bayesian networks to the true distribution over non- and weakly informative priors, even when half of the arcs of the prior DAG are wrong. We also showcase LGE on a gene regulatory network learned from single-cell kidney data.
