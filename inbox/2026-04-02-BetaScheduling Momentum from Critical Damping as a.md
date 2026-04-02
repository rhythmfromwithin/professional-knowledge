---
title: "Beta-Scheduling: Momentum from Critical Damping as a Diagnostic and Correction Tool for Neural Network Training"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.28921
priority: high
status: unread
interest: medium
next_step: skim
---
# Beta-Scheduling: Momentum from Critical Damping as a Diagnostic and Correction Tool for Neural Network Training
> 原文: [https://arxiv.org/abs/2603.28921](https://arxiv.org/abs/2603.28921)

arXiv:2603.28921v1 Announce Type: new
Abstract: Standard neural network training uses constant momentum (typically 0.9), a convention dating to 1964 with limited theoretical justification for its
optimality. We derive a time-varying momentum schedule from the critically damped harmonic oscillator: mu(t) = 1 - 2\*sqrt(alpha(t)), where alpha(t) is
the current learning rate. This beta-schedule requires zero free parameters beyond the existing learning rate schedule. On ResNet-18/CIFAR-10,
beta-scheduling delivers 1.9x faster convergence to 90% accuracy compared to constant momentum. More importantly, the per-layer gradient attribution
under this schedule produces a cross-optimizer invariant diagnostic: the same three problem layers are identified regardless of whether the model was
trained with SGD or Adam (100% overlap). Surgical correction of only these layers fixes 62 misclassifications while retraining only 18% of parameters.
A hybrid schedule -- physics momentum for fast early convergence, then constant momentum for the final refinement -- reaches 95% accuracy fastest
among five methods tested. The main contribution is not an accuracy improvement but a principled, parameter-free tool for localizing and correcting
specific failure modes in trained networks.
