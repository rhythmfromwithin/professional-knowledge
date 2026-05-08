---
title: "Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.04209
priority: low
status: unread
interest: medium
next_step: skim
---
# Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions
> 原文: [https://arxiv.org/abs/2605.04209](https://arxiv.org/abs/2605.04209)

arXiv:2605.04209v1 Announce Type: new
Abstract: We present Sparse Backdoor, a supply-chain attack that plants a \emph{provably undetectable} backdoor in pre-trained image classifiers, including convolutional networks and Vision Transformers. The attack injects a structured sparse perturbation along a randomly chosen direction into a small subset of columns at each fully connected layer, propagating a trigger signal to an adversary-chosen target class, and masks the perturbation with an independent isotropic Gaussian dither. The dither serves a single technical purpose: it induces a clean reference distribution anchored at the pre-trained weights, against which undetectability can be formalized. Under a mild margin condition on the pre-trained classifier, we show that the dithered reference is functionally equivalent to the original classifier. We prove that distinguishing the backdoor-injected model from this reference is at least as hard as Sparse PCA detection, which is computationally infeasible under standard hardness assumptions. The guarantee holds against any probabilistic polynomial-time distinguisher with white-box access to the parameters.
