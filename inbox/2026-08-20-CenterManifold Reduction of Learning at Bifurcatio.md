---
interest: medium
link: https://arxiv.org/abs/2605.12763
next_step: skim
priority: low
slack_ts: '1787276737.709359'
source: q-bio.NC - Neurons and Cognition
status: unread
title: 'Center-Manifold Reduction of Learning at Bifurcations: Interference and Rich
  Learning in Recurrent Neural Networks'
---
# Center-Manifold Reduction of Learning at Bifurcations: Interference and Rich Learning in Recurrent Neural Networks
> 原文: [https://arxiv.org/abs/2605.12763](https://arxiv.org/abs/2605.12763)

arXiv:2605.12763v2 Announce Type: replace-cross
Abstract: Rich learning in recurrent neural networks often proceeds through sudden transitions in latent dynamics, but there is little theory predicting how gradient descent behaves during these events. We study the local learning geometry near codimension-one bifurcations through the global empirical Neural Tangent Kernel (GeNTK). Under local center-manifold conditions, and when bifurcation-related sensitivity dominates bounded residual terms, we show that the global parameter-to-state Jacobian \(D\_\theta h\) is approximated by a low-rank normal-form operator. The induced GeNTK and Fisher information matrix therefore become strongly amplified and anisotropic, concentrating toward a rank-one channel for the four scalar codimension-one bifurcations and a rank-two real channel for a Neimark--Sacker bifurcation. Controlled high-dimensional RNN experiments validate this operator reduction. In learned RNNs, the same low-rank concentration coincides with abrupt loss changes and subtask interference, while a local projection predicts the sign of these effects near isolated events. Finally, in an input-driven 15-task LeakyRNN, GeNTK amplification aligns with continuation-detected changes in the MemoryPro dynamics. These results suggest a tractable operator-level description of learning near dynamical transitions, together with scalable diagnostics for amplified low-dimensional learning geometry.
