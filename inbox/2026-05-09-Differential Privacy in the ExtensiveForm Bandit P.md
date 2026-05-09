---
title: "Differential Privacy in the Extensive-Form Bandit Problem"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.05266
priority: low
status: unread
interest: medium
next_step: skim
---
# Differential Privacy in the Extensive-Form Bandit Problem
> 原文: [https://arxiv.org/abs/2605.05266](https://arxiv.org/abs/2605.05266)

arXiv:2605.05266v1 Announce Type: new
Abstract: We consider the extensive-form bandit problem, where on each trial the learner (a user coordinated by a server) plays an extensive-form game against an oblivious adversary, observing the information sets it finds itself in as well as the resulting payoff/loss. We give an algorithm for this problem that satisfies $\epsilon$-local differential privacy and attains a regret of $\tilde{O}(\sqrt{A\ln(S)T}/\epsilon)$, where $A$ is the total number of actions that the learner can possibly take, $S$ is the number of the learner's possible reduced strategies, and $T$ is the number of trials. On each trial, the time complexity of our algorithm is, up to a factor logarithmic in the maximum number of actions at an infoset, equal to the time required for the server to transmit the reduced strategy to the user. We note that local differential privacy is the strongest version of differential privacy and, to the best of our knowledge, this is the first work to study differential privacy of any form in the extensive-form bandit problem.
