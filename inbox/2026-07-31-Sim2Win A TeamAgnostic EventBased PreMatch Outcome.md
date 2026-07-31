---
title: "Sim2Win: A Team-Agnostic, Event-Based Pre-Match Outcome Prediction and Tactical Profiling System for Football"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.26061
priority: high
status: unread
interest: medium
next_step: skim
---
# Sim2Win: A Team-Agnostic, Event-Based Pre-Match Outcome Prediction and Tactical Profiling System for Football
> 原文: [https://arxiv.org/abs/2607.26061](https://arxiv.org/abs/2607.26061)

arXiv:2607.26061v1 Announce Type: new
Abstract: Pre-match tactical decision-making in professional football relies heavily on subjective expert analysis and identity-based scouting systems that cannot generalize to unseen teams. This paper presents Sim2Win, a team-agnostic, event-based pre-match tactical recommendation framework that reframes match outcome prediction as a tactical decision-support problem. Using StatsBomb open event data from eleven competitions spanning 178 teams and 1,411 team-match records, Sim2Win constructs five-match rolling tactical profiles, engineers four interpretable tactical feature ratios, clusters team behaviors into eight playstyles via K-Means, and trains thirteen classifiers to estimate win, draw, and loss probabilities from tactical matchup representations.
The system operates without team names or identity features, enabling generalization to teams never seen during training. A rigorous Leave-One-Competition-Out (LOCO) evaluation demonstrates that Sim2Win achieves a mean ROC-AUC of 0.704 and mean accuracy of 55.4% on completely unseen teams, outperforming ELO, Pi-Rating, and GAP baselines on all 21 ROC-AUC comparisons and 19 of 21 accuracy comparisons. Among all evaluated models, CatBoost achieved the strongest in-distribution performance with 60.90% accuracy.
These findings suggest that behavioral tactical representations provide transferable predictive signal under distribution shift and offer a viable alternative to identity-dependent football prediction systems.
