---
interest: medium
link: https://arxiv.org/abs/2607.16363
next_step: skim
priority: medium
slack_ts: '1784863620.867109'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'MTSSL: Meta-Thresholding Semi-Supervised Learning'
---
# MTSSL: Meta-Thresholding Semi-Supervised Learning
> 原文: [https://arxiv.org/abs/2607.16363](https://arxiv.org/abs/2607.16363)

arXiv:2607.16363v1 Announce Type: new
Abstract: A large body of Semi-supervised Learning~(SSL) algorithms encounter the threshold $\tau$ to select pseudo-labels. The value of $\tau$ across different SSL algorithms can vary depending on the learning perspective, yet they may achieve similar performance. It motivates us to establish a unified theoretical framework to explain the role of $\tau$ in SSL. We statistically explained that the unsupervised loss is affected independently by correct and incorrect pseudo-labels, while $\tau$ adjusts their numbers to balance the corresponding error term. This inherent trade-off indicates that SSL can reach the same loss with varying $\tau$, precise optimal values of $\tau$ during training may be unnecessary. With this, we treat $\tau$ as an updatable parameter and optimize it via differentiation; the new policy is named \textbf{Meta-Thresholding Semi-Supervised Learning (MTSSL)}. Extensive experiments demonstrate the superior performance of MTSSL. We observe that the accuracy curves of SSL algorithms can overlap completely even when the values of $\tau$ differ significantly, which supports our theoretical framework and indicates that the selection of $\tau$ can be relaxed in the future design of SSL algorithms.
