---
title: "Scientific Machine Learning of Chaotic Systems Learns Reduced-Order Equations for Neural Populations"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2507.03631
priority: low
status: unread
interest: medium
next_step: skim
---
# Scientific Machine Learning of Chaotic Systems Learns Reduced-Order Equations for Neural Populations
> 原文: [https://arxiv.org/abs/2507.03631](https://arxiv.org/abs/2507.03631)

arXiv:2507.03631v5 Announce Type: replace-cross
Abstract: Extracting interpretable mathematical models from complex dynamical systems is difficult, especially for chaotic dynamics observed with noisy experimental data. We present PEM-UDE, a method that combines prediction-error methodology with universal differential equations to discover governing equations from limited, noise-corrupted observations. Prediction-error feedback smooths the chaotic optimization problem; for noise-free data generated within the model class, it preserves the data-consistent zero-loss set, whereas noise and model misspecification introduce a gain-dependent stability-bias trade-off. Preservation of the zero-loss set is not a guarantee of unique structural identifiability. We test the method on two benchmark chaotic systems, the Rossler attractor and a real electrical circuit, and recover the correct functional forms even when one observed dimension contains noise of five times the signal magnitude. The method also accepts prior knowledge of the system as an initial functional form, which we use to learn neural circuit equations that account for sparse connectivity, a feature missing from conventional neural mass models. Applied to a population of Izhikevich neurons, PEM-UDE yields a multi-scale neural mass model that ties single-neuron parameters to macroscopic network dynamics and predicts a relationship between connection density, dominant oscillation frequency, and synchrony. We test these predictions against three intracranial recording datasets from rat and human cortices. For the neuroscience application, the learned equations are a reduced-order closure for a specified simulated Izhikevich network family; the experimental recordings provide an indirect consistency check of predicted frequency and synchrony trends, not a direct fit of the equations to recordings.
