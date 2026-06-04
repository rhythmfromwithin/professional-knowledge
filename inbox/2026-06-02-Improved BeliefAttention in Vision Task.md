---
interest: medium
link: https://arxiv.org/abs/2606.00077
next_step: skim
priority: medium
slack_ts: '1780548655.089549'
source: cs.CV - Computer Vision
status: unread
title: Improved Belief-Attention in Vision Task
---
# Improved Belief-Attention in Vision Task
> 原文: [https://arxiv.org/abs/2606.00077](https://arxiv.org/abs/2606.00077)

arXiv:2606.00077v1 Announce Type: new
Abstract: Recently, Belief-Attention \cite{Guoqiang25BeliefAttention} has been proposed by first performing an orthogonal projection of the softmax-based weighted summation of $V$ vectors with respect to the original $V$ vectors and then taking the perpendicular component as the residual signal in Transformer for performance improvement. In this paper, we first conduct an ablation study showing the projected component also carries information about the token correlation, which should not be ignored. We then propose to extend Belief-Attention by making use of both the perpendicular and projected components. In particular, the projected component goes through certain activation function and then a linear mapping before merging with the considered token. Conceptually speaking, the neural block for the projected component can be viewed as a two-layer feedforward network (FFN) within the new attention block. It is also noted that standard attention captures the token correlation via the inner-product matrix $QK^T$. We propose to introduce an additional inner-product matrix $ZZ^T$ to $QK^T$ to capture richer token correlation. We refer to the new module as Belief2-Attention. It can be easily shown that Belief2-Attention is more expressive than standard Attention. We then verify the effectiveness of Belief2-Attention for vision tasks of image classification and segmentation.
