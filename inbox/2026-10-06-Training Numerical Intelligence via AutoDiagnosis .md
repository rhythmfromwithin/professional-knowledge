---
title: "Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2610.03872
priority: high
status: unread
interest: medium
next_step: skim
---
# Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery
> 原文: [https://arxiv.org/abs/2610.03872](https://arxiv.org/abs/2610.03872)

arXiv:2610.03872v1 Announce Type: new
Abstract: AI agents are becoming increasingly capable of generating scientific code, but generating code is not the same as improving the algorithms behind it. For numerical solvers, execution feedback can expose poor performance, but rarely reveals its underlying cause and how to address it. We introduce Auto-Diagnosis and Skill Discovery (ADSD), a framework that links numerical diagnosis to reusable solver self-improvement. ADSD follows a diagnosis-first paradigm that first explains why a solver performs poorly, then uses this diagnosis to guide the discovery of appropriate numerical methods. The resulting knowledge is packaged into reusable solver skills, turning solver improvement from trial-and-error editing into a structured process of diagnosis, discovery, and implementation. Across four challenging numerical domains--power flow equation, AC optimal power flow control, stiff ordinary differential equations, and heterogeneous diffusion PDEs--ADSD consistently improves solver accuracy, robustness, and efficiency. On GOC-500 power flow, for example, ADSD reduces mean solver error by nearly $71\times$, with improvements further transferring to unseen grid topologies and operating regimes.
