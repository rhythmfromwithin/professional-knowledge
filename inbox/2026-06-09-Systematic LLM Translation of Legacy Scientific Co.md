---
interest: medium
link: https://arxiv.org/abs/2606.07681
next_step: skim
priority: low
slack_ts: '1780978313.619699'
source: cs.SE - Software Engineering
status: unread
title: 'Systematic LLM Translation of Legacy Scientific Code to Differentiable Frameworks:
  Application to a Land Surface Model'
---
# Systematic LLM Translation of Legacy Scientific Code to Differentiable Frameworks: Application to a Land Surface Model
> 原文: [https://arxiv.org/abs/2606.07681](https://arxiv.org/abs/2606.07681)

arXiv:2606.07681v1 Announce Type: new
Abstract: Differentiable programming offers transformative capabilities for scientific modeling, enabling gradient-based parameter estimation, sensitivity analysis, and data assimilation. Yet, migrating legacy codebases into differentiable frameworks remains a challenge. We present a five-phase LLM-based agentic pipeline that translates legacy Fortran into JAX: static dependency analysis determines module translation order from the full call graph; iterative compile-repair loops correct errors autonomously; and a Fortran reference oracle enforces numerical parity at the module level before integration and gradient verification. We instantiate and evaluate the pipeline on CLM-ml-v2, a 19,000-line Fortran land surface model, and analyze agent behavior across 73 module translation tasks. The resulting differentiable model computes the complete Jacobian in a single backward pass, recovers physical parameters in eight times fewer steps than gradient-free optimization, and achieves a 24 times wall-clock speedup over sequential Fortran at ensemble size N=2,048. Both the translated model and pipeline infrastructure are released as a reusable framework for differentiating other Earth system model components.
