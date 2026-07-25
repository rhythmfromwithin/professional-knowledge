---
title: "Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.21005
priority: low
status: unread
interest: medium
next_step: skim
---
# Weight-norm Criticality: A Mechanism for Loss Spikes Induced by the Normalization and Weight Decay
> 原文: [https://arxiv.org/abs/2607.21005](https://arxiv.org/abs/2607.21005)

arXiv:2607.21005v1 Announce Type: cross
Abstract: Most explanations of training instability focus on \emph{learning-rate criticality}, typically characterized by the Edge of Stability, beyond which optimization becomes unstable. We argue that, in practical deep neural network training, there is an additional and often overlooked \emph{weight-norm criticality}. This criticality is induced by the interaction between normalization (which introduces scale-invariant components) and weight decay (which persistently shrinks parameter norms). As the weight decay coefficient increases, the norms of scale-invariant weights are progressively driven toward zero. Meanwhile, the sharpness of the loss landscape increases rapidly, destabilizing the optimization dynamics and resulting in abrupt loss spikes. This perspective provides a rationale for why weight penalties can improve generalization yet cannot be made arbitrarily strong: excessive decay drives scale-invariant weight norms past a critical boundary and destabilizes training. Our work provides a new mechanistic understanding of loss spikes through the lens of \emph{weight-norm criticality}. Moreover, \emph{weight-norm criticality} yields testable predictions that we validate empirically in networks with scale-invariant components, providing empirical support for the proposed mechanism.
