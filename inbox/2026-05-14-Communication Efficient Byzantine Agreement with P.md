---
title: "Communication Efficient Byzantine Agreement with Predictions"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.12935
priority: medium
status: unread
interest: medium
next_step: skim
---
# Communication Efficient Byzantine Agreement with Predictions
> 原文: [https://arxiv.org/abs/2605.12935](https://arxiv.org/abs/2605.12935)

arXiv:2605.12935v1 Announce Type: new
Abstract: In Byzantine agreement with predictions each process begins with an input value and some (unreliable) prediction bits. Recently, it has been shown that with \emph{classification predictions} -- where the predictions predict each process to be honest or faulty -- Byzantine agreement can be completed more quickly than without predictions, circumventing the traditional $\Omega(f)$ round lower bound. However, existing algorithms either handle limited prediction errors or send too many messages. Moreover, they all exchange $\Omega(n^3)$ bits -- enough to allow the processes to approximately agree on the classifications. In fact, it almost seemed necessary to share a significant number of prediction bits if one wanted to tolerate a high number of incorrect predictions.
In this paper, we show that this high level of communication (and sharing of predictions) is not inherent by developing an unauthenticated algorithm with $\tilde{O}(n^{2.5})$ communication complexity. Furthermore, with authentication, we give an algorithm with optimal $O(n^2\kappa)$ communication complexity (where $\kappa$ is a security parameter). All of our results have optimal round complexity for any number of errors in the predictions.
