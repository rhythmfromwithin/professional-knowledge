---
title: "Beyond Routing Weights: Faithful Response-Level Interpretation of Mixture-of-Experts Reward Models via Contribution Contrast"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2608.06400
priority: high
status: unread
interest: medium
next_step: skim
---
# Beyond Routing Weights: Faithful Response-Level Interpretation of Mixture-of-Experts Reward Models via Contribution Contrast
> 原文: [https://arxiv.org/abs/2608.06400](https://arxiv.org/abs/2608.06400)

arXiv:2608.06400v1 Announce Type: new
Abstract: Reward models are central to learning from human preferences, yet identifying what drives their predictions remains challenging. Recent sparse Mixture-of-Experts (MoE) reward models seek to improve interpretability by routing prompts to specialized experts and characterizing experts through examples with high routing weights. However, routing weights only reveal which prompts an expert $\textit{receives}$, not how it $\textit{judges}$ responses, providing only a partial account of expert behavior. We therefore propose $\textbf{Co}$ntribution-$\textbf{Co}$ntrast ($\textbf{CoCo}$) response-level interpretation, which faithfully characterizes experts' roles using chosen-rejected response pairs with the largest contribution contrasts, jointly capturing routing and preference behavior. Across automatic and human evaluations, CoCo yields more coherent, faithful, and specialized interpretations than router-based, score-based, and sparse autoencoder-based alternatives while maintaining competitive reward modeling accuracy. To the best of our knowledge, this is the first systematic study of interpretation methods for MoE reward models.
