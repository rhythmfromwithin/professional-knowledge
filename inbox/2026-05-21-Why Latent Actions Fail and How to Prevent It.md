---
title: "Why Latent Actions Fail, and How to Prevent It"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.20223
priority: medium
status: unread
interest: medium
next_step: skim
---
# Why Latent Actions Fail, and How to Prevent It
> 原文: [https://arxiv.org/abs/2605.20223](https://arxiv.org/abs/2605.20223)

arXiv:2605.20223v1 Announce Type: new
Abstract: Latent action models (LAMs) aim to learn action-like representations from unlabeled videos by compressing frame-to-frame changes. The frames of in-the-wild videos, however, contain not only the agent's own state but exogenous state such as background clutter. Since the exogenous state introduces changes unrelated to actions, it hinders reliable latent action learning. This paper investigates this problem analytically by extending a linear LAM framework to explicitly model exogenous state. Our analysis reveals two insights: (1) minimizing the standard reconstruction objective produces latent actions that encode exogenous information from future observation; and (2) learning in a representation space that focuses on endogenous components is a key to mitigating the interference of noise. We further show that previously proposed auxiliary objectives, such as action-supervision, provably encourage latent actions to be consistent across exogenous states. These findings are validated through experiments on both linear and nonlinear LAMs, providing a unified theoretical analysis of how exogenous state hinders latent action learning and why common remedies work.
