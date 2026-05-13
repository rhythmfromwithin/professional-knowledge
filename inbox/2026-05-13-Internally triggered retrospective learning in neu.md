---
title: "Internally triggered retrospective learning in neural networks"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2605.10994
priority: low
status: unread
interest: medium
next_step: skim
---
# Internally triggered retrospective learning in neural networks
> 原文: [https://arxiv.org/abs/2605.10994](https://arxiv.org/abs/2605.10994)

arXiv:2605.10994v1 Announce Type: new
Abstract: Learning in artificial neural networks usually relies on continuous, externally driven weight updates, in which parameters are modified at every step in response to incoming data, error signals or reward feedback. In this setting, routine and informative inputs contribute similarly to parameter adjustment. We introduce a learning approach in which parameter updates are governed by internally generated events arising from the network own representational dynamics. During ongoing activity, synaptic interactions are accumulated as latent traces encoding recent coactivation patterns, without immediately modifying the underlying parameters. In parallel, an internal predictive process estimates the evolving latent state, while a scalar measure of discrepancy between predicted and observed states is continuously computed. When discrepancy exceeds an adaptive threshold derived from recent error statistics, a learning event is triggered, inducing a retrospective update selectively integrating past activity into the current configuration. We performed simulations using a minimal neural network exposed to structured sequential inputs with transient perturbations. We found that learning occurs through sparse, temporally localized events associated with increases in prediction error, leading to stepwise changes in synaptic efficacy and discrete transitions in latent state organization. By selectively reorganizing parameters in response to internally detected discrepancies, our episodic updating may reduce unnecessary parameter drift while preserving informative patterns. Potential applications include systems requiring selective adaptation to rare or informative inputs such as physiological, industrial or environmental monitoring, edge computing under limited energy budgets, autonomous systems operating in dynamic conditions and sequential computational data processing.
