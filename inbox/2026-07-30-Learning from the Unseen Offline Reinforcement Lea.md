---
title: "Learning from the Unseen: Offline Reinforcement Learning with Hidden Actions"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.25241
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning from the Unseen: Offline Reinforcement Learning with Hidden Actions
> 原文: [https://arxiv.org/abs/2607.25241](https://arxiv.org/abs/2607.25241)

arXiv:2607.25241v1 Announce Type: new
Abstract: Standard offline reinforcement learning (RL) algorithms typically assume that the actions in the dataset are observed without error. However, in many real-world applications, the true actions are unobserved and only noisy proxies are available, causing existing RL methods to yield biased and potentially misleading conclusions. We study off-policy evaluation in infinite-horizon discounted Markov decision processes with hidden actions. By leveraging the next-state variable as a natural proxy for the unobserved action, we establish identification of the policy value and propose an influence-function-based estimator called LURE (Learning from the Unseen: Robust Estimator). LURE is multiply robust, remaining consistent under several combinations of correctly specified nuisance components, and is asymptotically normal, enabling valid statistical inference. To our knowledge, this is the first work to address offline RL with hidden actions. We demonstrate LURE's effectiveness through simulations and a sepsis management application using the MIMIC-III database.
