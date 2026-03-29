---
interest: medium
link: https://arxiv.org/abs/2603.22472
next_step: skim
priority: medium
slack_ts: '1774754587.499909'
source: cs.RO - Robotics
status: unread
title: 'Wake Up to the Past: Using Memory to Model Fluid Wake Effects on Robots'
---
# Wake Up to the Past: Using Memory to Model Fluid Wake Effects on Robots
> 原文: [https://arxiv.org/abs/2603.22472](https://arxiv.org/abs/2603.22472)

arXiv:2603.22472v1 Announce Type: new
Abstract: Autonomous aerial and aquatic robots that attain mobility by perturbing their medium, such as multicopters and torpedoes, produce wake effects that act as disturbances for adjacent robots. Wake effects are hard to model and predict due to the chaotic spatio-temporal dynamics of the fluid, entangled with the physical geometry of the robots and their complex motion patterns. Data-driven approaches using neural networks typically learn a memory-less function that maps the current states of the two robots to a force observed by the "sufferer" robot. Such models often perform poorly in agile scenarios: since the wake effect has a finite propagation time, the disturbance observed by a sufferer robot is some function of relative states in the past. In this work, we present an empirical study of the properties a wake-effect predictor must satisfy to accurately model the interactions between two robots mediated by a fluid. We explore seven data-driven models designed to capture the spatio-temporal evolution of fluid wake effects in four different media. This allows us to introspect the models and analyze the reasons why certain features enable improved accuracy in prediction across predictors and fluids. As experimental validation, we develop a planar rectilinear gantry for two spinning monocopters to test in real-world data with feedback control. The conclusion is that support of history of previous states as input and transport delay prediction substantially helps to learn an accurate wake-effect predictor.
