---
title: "Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.07716
priority: high
status: unread
interest: medium
next_step: skim
---
# Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution
> 原文: [https://arxiv.org/abs/2607.07716](https://arxiv.org/abs/2607.07716)

arXiv:2607.07716v1 Announce Type: new
Abstract: Temporal graphs are ubiquitous in real-world applications and Temporal Graph Networks (TGNs) have achieved superior predictive accuracy. Understanding which historical events drive model predictions can enhance trustworthiness of TGNs. Existing explanation methods overlook the memory module, the core component that records and updates node histories, leaving the influence of past events unexplored. To address this, we attribute TGNs predictions through the topology attribution tree and memory backtracking tree. The topology attribution tree captures the influence of neighbors and their memory vectors, then the memory backtracking tree quantifies how historical events shape node memory vectors. We apply the LRP in TGNs, ensuring that the total contribution of events equals the logits of model. Finally, top-k selection may be unfaithful due to the nonlinear mapping from logits to probabilities, we design optimization objectives to identify the important events. Experiments on nine temporal graph datasets, spanning node property prediction, link prediction tasks and graph classification tasks, show that our method provides faithful explanations and outperforms state-of-the-art baselines. The code is available at https://github.com/yazhengliu/MemExplainer
