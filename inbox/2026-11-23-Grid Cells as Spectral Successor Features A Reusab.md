---
interest: medium
link: https://arxiv.org/abs/2611.26504
next_step: skim
priority: low
slack_ts: '1795512705.716939'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Grid Cells as Spectral Successor Features: A Reusable Basis for Continual
  Reinforcement Learning'
---
# Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning
> 原文: [https://arxiv.org/abs/2611.26504](https://arxiv.org/abs/2611.26504)

arXiv:2611.26504v1 Announce Type: cross
Abstract: Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but their effectiveness depends on the choice of base features. Taking the identification of entorhinal grid cells with eigenvectors of the successor representation as a design principle, we build this basis from eigenvectors of the transition matrix of a fixed reference policy. With such a basis, the successor features at a state-action pair are a linear combination of the base features at that same pair, which is not true in general, and the coefficients are known in closed form: each successor feature is its base feature multiplied by $\theta\_i = 1/(1-\gamma\lambda\_i)$, where $\lambda\_i$ is its eigenvalue. The long-term return is thus predicted from the same features as the immediate reward, no successor-feature network or replay buffer is needed, and adapting to a new task reduces to a linear regression on the reward. The agent acts greedily on the action values of the reference policy, which is one step of policy improvement over it and suffices to reach a single goal. In a two-goal gridworld, with the uniform random walk as reference policy, whose eigenvectors are the low-frequency Laplacian eigenvectors, agents built this way maintain near-maximal return across every change of goal, whereas SimpleSF and DQN lose most of their return at each change.
