---
title: "Fourier Feature Physics-Informed Neural Networks for Elasto-Plastic Analysis of Geomaterials with a Non-Associative Mohr-Coulomb Model"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.25150
priority: low
status: unread
interest: medium
next_step: skim
---
# Fourier Feature Physics-Informed Neural Networks for Elasto-Plastic Analysis of Geomaterials with a Non-Associative Mohr-Coulomb Model
> 原文: [https://arxiv.org/abs/2607.25150](https://arxiv.org/abs/2607.25150)

arXiv:2607.25150v2 Announce Type: new
Abstract: Elasto-plastic boundary value problems in geotechnical engineering are conventionally solved by the Finite Element Method (FEM), which incurs high computational cost from incremental-iterative procedures. Physics-Informed Neural Networks (PINNs) offer a mesh-free alternative but suffer from spectral bias, failing to resolve the sharp gradients arising at elastic-plastic boundaries and within localized plastic zones. This limitation is particularly consequential for the non-associative Mohr-Coulomb model, whose pressure-dependent yield surface and dilatant flow rule generate narrower plastic zones and steeper stress gradients than pressure-independent criteria. This study proposes a Fourier Feature Physics-Informed Neural Network (FF-PINN) for two-dimensional elasto-plastic problems governed by this model. Random Fourier feature mapping is embedded into the input layer to mitigate spectral bias, supported by a multi-objective loss function enforcing equilibrium, constitutive relations, and Karush-Kuhn-Tucker conditions against high-fidelity FEM data, together with a strain-adaptive sampling strategy. Benchmarked across three test cases, FF-PINN achieves superior accuracy across most predicted fields, with error reductions up to approximately 66 percent in displacement and 27 percent in stress components, and reproduces the plastic failure zone geometry with markedly closer fidelity to FEM. Sensitivity analysis confirms robustness across training data size, collocation density, loss weighting, and noise levels up to 2.0 percent. FF-PINN converges in half the training epochs required by the conventional PINN, halving wall-clock training time while achieving greater predictive accuracy. The framework therefore offers a computationally efficient and physics-consistent alternative to FEM for elasto-plastic geotechnical analysis.
