---
title: "MILP-Evo: Closed-Loop Fully Automatic Design of MILP Solvers"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.18252
priority: low
status: unread
interest: medium
next_step: skim
---
# MILP-Evo: Closed-Loop Fully Automatic Design of MILP Solvers
> 原文: [https://arxiv.org/abs/2607.18252](https://arxiv.org/abs/2607.18252)

arXiv:2607.18252v1 Announce Type: cross
Abstract: Machine learning methods have shown that data-driven policies can accelerate mixed-integer linear programming (MILP) solvers, but many such approaches remain difficult to inspect, adapt, and deploy because the learned policy is represented as an external predictor or other opaque model. By contrast, explicit solver logic is easier to understand and integrate, but is usually hand-designed rather than learned from solver feedback. We study whether the automatic design of MILP solver logic can instead be cast as LLM-guided closed-loop search over executable white-box components evaluated directly by end-to-end solver behavior. To this end, we propose a closed-loop program evolution framework for MILP solver auto-design, implemented through PySCIPOpt, and instantiate it on the joint design of a cut selector and a branching rule. Candidate programs are iteratively generated, loaded into SCIP, and evaluated by direct execution on MILP instances, with the resulting feedback guiding performance-based selection, targeted repair, diagnostic reflection, and diversity-aware population maintenance. The method outputs explicit solver components that can be inspected, modified, and deployed within standard solver workflows. Across four benchmark families, we find that LLM-guided program evolution can discover competitive domain-specialized policies in several settings.
