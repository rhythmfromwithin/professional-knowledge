---
title: "Robust Parameter and State Estimation in Multiscale Neuronal Systems Using Physics-Informed Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2603.08742
priority: low
status: unread
interest: medium
next_step: skim
---
# Robust Parameter and State Estimation in Multiscale Neuronal Systems Using Physics-Informed Neural Networks
> 原文: [https://arxiv.org/abs/2603.08742](https://arxiv.org/abs/2603.08742)

arXiv:2603.08742v1 Announce Type: new
Abstract: Inferring biophysical parameters and hidden state variables from partial and noisy observations is a fundamental challenge in computational neuroscience. This problem is particularly difficult for fast - slow spiking and bursting models, where strong nonlinearities, multiscale dynamics, and limited observational data often lead to severe sensitivity to initial parameter guesses and convergence failure in the methods replying on the traditional numerical forward solvers. In this work, we developed a physics-informed neural network (PINN) framework for the joint reconstruction of unobserved state variables and the estimation of unknown biophysical parameters in neuronal models. We demonstrate the effectiveness of the method on biophysical neuron models, including the Morris-Lecar model across multiple spiking and bursting regimes and a respiratory model neuron. The method requires only partial voltage observations over short observation windows and remains robust even when initialized with non-informative parameter guesses. These results suggest that PINN can deliver robust and accurate parameter inference and state reconstruction, providing a promising alternative for inverse problems in multiscale neuronal dynamics, where traditional techniques often struggle.
