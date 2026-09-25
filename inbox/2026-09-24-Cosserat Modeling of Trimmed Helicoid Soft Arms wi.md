---
interest: medium
link: https://arxiv.org/abs/2609.25264
next_step: skim
priority: medium
slack_ts: '1790310818.108149'
source: cs.RO - Robotics
status: unread
title: Cosserat Modeling of Trimmed Helicoid Soft Arms with a Separated-Section Constitutive
  Law
---
# Cosserat Modeling of Trimmed Helicoid Soft Arms with a Separated-Section Constitutive Law
> 原文: [https://arxiv.org/abs/2609.25264](https://arxiv.org/abs/2609.25264)

arXiv:2609.25264v1 Announce Type: new
Abstract: Cosserat rod models for soft robots usually construct sectional stiffness by summing material properties over a common cross-section. This assumption becomes inaccurate for trimmed helicoid arms, where load-bearing helix domains are separated and connected only through sparse fused crossings. This paper formulates a separated-section constitutive law that evaluates each helix domain in its local frame and pulls its constitutive response back to the backbone, yielding an effective backbone stiffness. Sparse-fusion mechanics captures the additional compliance caused by relative motion between neighboring domains and determines channel-wise reduction profiles $\eta\_c(s/L)$ for bending, torsion, and extension. The resulting effective sectional stiffness is strongly anisotropic: bending and extension are reduced by about one order of magnitude, whereas torsion remains close to the effective backbone stiffness. The resulting sectional law is embedded in a geometrically exact dynamic Cosserat model with GVS discretization and routed-tendon actuation. Across 103 measured configurations, the three datasets give pooled normalized position errors of \SI{7.7}{\percent}, \SI{6.7}{\percent}, and \SI{7.8}{\percent}, while each full-arm solve requires approximately \SI{0.3}{s} on one CPU core (Intel Xeon, Cascade Lake, \SI{2.8}{GHz}), enabling rapid model-based planning, state and load estimation, and morphology--control co-design for architected soft robots.
