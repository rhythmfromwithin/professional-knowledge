---
title: "LAWS: Learning from Actual Workloads Symbolically -- A Self-Certifying Parametrized Cache Architecture for Neural Inference, Robotics, and Edge Deployment"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.04069
priority: low
status: unread
interest: medium
next_step: skim
---
# LAWS: Learning from Actual Workloads Symbolically -- A Self-Certifying Parametrized Cache Architecture for Neural Inference, Robotics, and Edge Deployment
> 原文: [https://arxiv.org/abs/2605.04069](https://arxiv.org/abs/2605.04069)

arXiv:2605.04069v1 Announce Type: cross
Abstract: We introduce LAWS (Learning from Actual Workloads Symbolically), a self-certifying inference caching architecture that builds a growing library of certified expert functions from deployment observations. Each expert covers a region of input space defined by a node in the Probabilistic Language Trie (PLT) of the base model and carries a formal error bound holding uniformly over all inputs. The central result is a self-certification theorem: for any input x, the LAWS approximation error is bounded by epsilon\_fit + 2\*Lambda(W)\*C\_E, where Lambda(W) is the model Lipschitz constant, C\_E is the maximum embedding diameter, and epsilon\_fit is the expert training error -- all checkable at deployment time without ground truth. We prove that LAWS generalizes both Mixture-of-Experts and KV prefix caching as special cases and is strictly more expressive than any fixed-K MoE or finite cache. Further results include a monotone hit rate theorem (any-match routing ensures coverage only increases), an expert library growth rate of O(2^H log N) where H is workload entropy, a fleet learning convergence theorem with Omega(K) speedup for K-unit fleets, and an over-the-air update bandwidth bound. We conjecture that LAWS is acquisition-optimal among stationary online caching algorithms and that the effective Lipschitz constant on the training distribution grows polynomially rather than exponentially in depth. Applications are developed for LLM inference, robotic control, and multi-agent edge deployment.
