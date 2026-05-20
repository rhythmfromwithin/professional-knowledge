---
title: "GenAI-FDIA: Physics-Informed Generative Models for False Data Injection Attacks"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.18873
priority: low
status: unread
interest: medium
next_step: skim
---
# GenAI-FDIA: Physics-Informed Generative Models for False Data Injection Attacks
> 原文: [https://arxiv.org/abs/2605.18873](https://arxiv.org/abs/2605.18873)

arXiv:2605.18873v1 Announce Type: new
Abstract: Training and evaluating false data injection attack (FDIA) detectors for power systems is constrained by data scarcity. Operational grid measurements are commercially sensitive, and hand-crafted attacks fail to capture complex distributional structures imposed by network physics. We present \textsc{GenAI-FDIA}, a framework benchmarking a pool of $P{=}20$ architectures for physics-compliant FDIA synthesis, spanning Wasserstein GANs, MMD-VAEs, normalising flows, diffusion models, and cross-family hybrids. These are evaluated across three IEEE testbeds (14-bus DC, 30-bus DC, and 14-bus AC) under a 60/20/20 chronological split using data-driven Bad Data Detection (BDD) threshold calibration. Our empirical results verify that these models generate high-fidelity attacks, with all architectures achieving evasion rates of $\epsilon\_{\text{BDD}} \ge 86.6\%$ on the 14-bus network; additionally, limiting an attacker's topological knowledge induces a measurable degradation in stealthiness ($p \le 0.0022$). Crucially, we identify a previously unreported failure mode: applying affine physics projections directly in normalised feature spaces critically displaces the attack vector, collapsing BDD evasion from ${\sim}55\%$ to $<\!2\%$ on the 30-bus testbed. We resolve this via a novel inference-time harmoniser, restoring full stealthiness ($\epsilon\_{\text{BDD}}{=}100\%$) across all physics-informed variants without retraining. Finally, we isolate a covariance-collapse phenomenon ($\kappa \approx {-}0.076$) within advanced hybrid architectures and rectify it through 50-epoch warm-up schedules ($\kappa \to 0.785$, $\Delta\text{MMD}={-}3.1\%$). Ultimately, \textsc{GenAI-FDIA} delivers a robust recovery blueprint applicable to any physics-constrained generative model deployed for power-system security.
