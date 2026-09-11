---
interest: medium
link: https://arxiv.org/abs/2609.10643
next_step: skim
priority: high
slack_ts: '1789100121.250479'
source: cs.LG - Machine Learning
status: unread
title: 'Zero-shot rib design: merging training-free generative prior with topology
  optimization'
---
# Zero-shot rib design: merging training-free generative prior with topology optimization
> 原文: [https://arxiv.org/abs/2609.10643](https://arxiv.org/abs/2609.10643)

arXiv:2609.10643v1 Announce Type: new
Abstract: Natural load-bearing patterns such as leaf venation, trabecular bone, and spider webs achieve high stiffness per unit mass, yet classical topology optimizers rarely reach such geometries, and few let engineers express structural design intent through natural language. This work treats a frozen text-to-image diffusion model as a training-free source of design knowledge and distills it into the physics loop of density-based topology optimization via score distillation sampling, so that a text prompt becomes an explicit, machine-interpretable representation of engineer intent. The prompt-induced generative gradient and the finite element sensitivity are combined at every iteration, letting physics decide which prompt-induced features survive. In 245 primary SDS runs spanning four geometric domains and two physics regimes, 38 of 49 prompt--domain combinations achieved statistically significant compliance reductions (up to $-31.5\%$ mechanical and $-23.0\%$ thermoelastic), outperforming gradient-based baselines. Cross-domain morphological analysis identifies a recurring structural signature of improvement: in most domains the generative prior suppresses dead-end branches in the rib skeleton, with endpoint--compliance correlation $r = +0.56$ to $+0.99$. A Heaviside projection with $\beta$-continuation resolves a pronounced intermediate-density tendency in this diffusion--physics coupling ($42.6\%$ to $<3\%$), and an automated skeleton-based pipeline converts optimized density fields into \rev{candidate geometry ready for computer-aided design. By retargeting the generative prior across domains, loading conditions, and physics objectives through a change of text prompt, with each new problem's physics setup specified separately, the framework uses a pretrained generative model as a reusable, training-free prior for engineering design.
