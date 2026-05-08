---
title: "Regularized Centered Emphatic Temporal Difference Learning"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.04100
priority: high
status: unread
interest: medium
next_step: skim
---
# Regularized Centered Emphatic Temporal Difference Learning
> 原文: [https://arxiv.org/abs/2605.04100](https://arxiv.org/abs/2605.04100)

arXiv:2605.04100v1 Announce Type: new
Abstract: Off-policy temporal-difference (TD) learning with function approximation faces a structural tradeoff among stability, projection geometry, and variance control. Emphatic TD (ETD) improves the off-policy projection geometry through follow-on emphasis, but the follow-on trace can have high variance. We revisit this tradeoff through Bellman-error centering. Although centering naturally removes a common drift term from TD errors, we show that a naive centered emphatic extension introduces an auxiliary coupling that can destroy the positive-definiteness of the ETD key matrix. We propose \emph{Regularized Emphatic Temporal-Difference Learning} (RETD), which preserves the follow-on trace and regularizes only the auxiliary centering recursion, corresponding to lifting the lower-right block of the coupled key matrix from \(1\) to \(1+c\). We derive the RETD core matrix, prove convergence under a conservative sufficient regularization condition, and evaluate the method on diagnostic linear off-policy prediction tasks. The experiments show that RETD avoids the instability of naive centered emphatic learning, preserves favorable emphatic geometry, and exhibits a robust intermediate regime for the regularization parameter \(c\) across the diagnostics.
