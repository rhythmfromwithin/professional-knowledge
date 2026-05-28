---
title: "Personalized Observation Normalization for Federated Reinforcement Learning in Simulation Environments with Heterogeneity"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.27385
priority: high
status: unread
interest: medium
next_step: skim
---
# Personalized Observation Normalization for Federated Reinforcement Learning in Simulation Environments with Heterogeneity
> 原文: [https://arxiv.org/abs/2605.27385](https://arxiv.org/abs/2605.27385)

arXiv:2605.27385v1 Announce Type: new
Abstract: Federated reinforcement learning (FedRL) enables multiple agents to collaboratively train a global policy without sharing raw data, making it ideal for privacy-sensitive applications. However, FedRL faces challenges in heterogeneous environments where differing state-transition dynamics lead to non-identical input distributions and imbalanced parameter updates during aggregation. Therefore, this paper develops a personalized observation normalization (PON) method, allowing each agent to locally normalize raw state inputs using a continuously updated running mean and variance. This design ensures consistent scaling of local feature without overshadowing across agents during aggregation. Furthermore, we demonstrate that sharing normalization parameters across agents is ineffective due to the diverse local input distributions, which highlights the necessity of personalized statistics. Experiments on heterogeneous MuJoCo tasks show that our developed PON accelerates training and achieves superior performance compared to baseline methods.
