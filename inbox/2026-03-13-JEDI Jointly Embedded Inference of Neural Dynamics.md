---
interest: medium
link: https://arxiv.org/abs/2603.10489
next_step: skim
priority: low
slack_ts: '1773888806.665939'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'JEDI: Jointly Embedded Inference of Neural Dynamics'
---
# JEDI: Jointly Embedded Inference of Neural Dynamics
> 原文: [https://arxiv.org/abs/2603.10489](https://arxiv.org/abs/2603.10489)

arXiv:2603.10489v1 Announce Type: new
Abstract: Animal brains flexibly and efficiently achieve many behavioral tasks with a single neural network. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying neural populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental neural recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While recurrent neural networks (RNNs) directly constrained neural data have been effective in inferring underlying dynamical mechanisms, they are typically limited to single-task domains and struggle to generalize across behavioral conditions. Here, we introduce JEDI, a hierarchical model that captures neural dynamics across tasks and contexts by learning a shared embedding space over RNN weights. This model recapitulates individual samples of neural dynamics while scaling to arbitrarily large and complex datasets, uncovering shared structure across conditions in a single, unified model. Using simulated RNN datasets, we demonstrate that JEDI accurately learns robust, generalizable, condition-specific embeddings. By reverse-engineering the weights learned by JEDI, we show that it recovers ground truth fixed point structures and unveils key features of the underlying neural dynamics in the eigenspectra. Finally, we apply JEDI to motor cortex recordings during monkey reaching to extract mechanistic insight into the neural dynamics of motor control. Our work shows that joint learning of contextual embeddings and recurrent weights provides scalable and generalizable inference of brain dynamics from recordings alone.
