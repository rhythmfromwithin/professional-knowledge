---
title: "Scalable Perturbation Learning for Online Self-Supervised Echo State Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.06079
priority: low
status: unread
interest: medium
next_step: skim
---
# Scalable Perturbation Learning for Online Self-Supervised Echo State Networks
> 原文: [https://arxiv.org/abs/2607.06079](https://arxiv.org/abs/2607.06079)

arXiv:2607.06079v1 Announce Type: cross
Abstract: Intelligent systems should not only solve tasks but also adapt under real-world constraints. Autonomous adaptation via self-supervised learning, sequential adaptation via online learning, and memory-efficient implementation via perturbation-based learning are important requirements for such systems. However, these requirements are generally in tension for high-dimensional systems, because perturbation-based learning suffers from variance that grows with the dimension of the perturbed variables.
In this study, we focus on echo state networks (ESNs), where this tension naturally arises in large reservoirs. We propose a perturbation-based learning rule for online self-supervised learning in ESNs. The proposed rule is derived from an orthogonal decomposition of the self-supervised learning cost, which separates an input-dependent component from a redundant component determined by the fixed ESN parameters. By perturbing only the input-dependent component, the effective perturbation dimension is reduced from the reservoir dimension to the input dimension.
Thus, the proposed method preserves self-supervised adaptation, online learning, and scalar-feedback perturbation learning, while avoiding reservoir-size-dependent variance growth. This suggests a design principle for scalable and hardware-compatible learning: online learning should be restricted to the dynamically necessary low-dimensional component of the objective.
