---
interest: medium
link: https://arxiv.org/abs/2603.11032
next_step: skim
priority: low
slack_ts: '1773715532.561419'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Uncovering statistical structure in large-scale neural activity with Restricted
  Boltzmann Machines
---
# Uncovering statistical structure in large-scale neural activity with Restricted Boltzmann Machines
> 原文: [https://arxiv.org/abs/2603.11032](https://arxiv.org/abs/2603.11032)

arXiv:2603.11032v1 Announce Type: new
Abstract: Large-scale electrophysiological recordings now allow simultaneous monitoring of thousands of neurons across multiple brain regions, revealing structured variability in neural population activity. Understanding how these collective patterns emerge from microscopic neural interactions requires models that are scalable, predictive, and interpretable. Statistical physics provides principled frameworks to address this complexity, including maximum-entropy models that offer transparent descriptions of collective neural activity but remain largely limited to pairwise interactions and modest system sizes. Here, we use Restricted Boltzmann Machines (RBMs) to model the activity of $\sim1500$-$2000$ simultaneously recorded neurons from the Allen Institute Visual Behavior Neuropixels dataset, spanning multiple cortical and subcortical regions of the mouse brain. RBMs extend the maximum-entropy framework through latent variables, enabling the capture of higher-order dependencies while allowing explicit extraction of effective interaction networks. Recent advances in efficient Markov Chain sampling and training enable accurate learning of these models at this scale. RBMs reproduce the complex statistics of neural recordings with high accuracy. Generated samples match empirical pairwise and higher-order correlations, as well as global statistics such as the distribution of population activity. The inferred parameters provide direct access to effective neuronal interactions, revealing coordination patterns in population activity. These couplings display clear anatomical structure: neurons within visual cortical areas show stronger interactions, consistent with visually driven behavior, while cross-area couplings are weaker. Despite being trained on temporally shuffled data, Markov Chain Monte Carlo simulations also reproduce the global relaxation dynamics of neural activity.
