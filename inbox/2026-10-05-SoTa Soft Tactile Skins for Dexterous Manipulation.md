---
title: "SoTa: Soft Tactile Skins for Dexterous Manipulation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.02338
priority: medium
status: unread
interest: medium
next_step: skim
---
# SoTa: Soft Tactile Skins for Dexterous Manipulation
> 原文: [https://arxiv.org/abs/2610.02338](https://arxiv.org/abs/2610.02338)

arXiv:2610.02338v1 Announce Type: new
Abstract: A growing body of work suggests that tactile sensing gives robot policies contact information that complements vision in dexterous manipulation. However, visuo-tactile robot data remains scarce: dexterous demonstrations require teleoperating robots, which limits dataset scale. Human demonstrations are far cheaper to collect and offer a path to scale this data, but only if human and robot hands carry tactile sensors with corresponding signals. This requires sensors that conform to different hand geometries, cover the full hand, and share a common layout across embodiments. We present SoTa, a low-cost capacitive tactile skin that provides full-hand coverage on humans and robots while preserving a shared layout of 202 taxels across corresponding finger and palm regions. Our multilayer design with fabric electrodes enables in-house fabrication of thin, soft skins with customizable geometry for under $10 in materials per skin. The sensor retains over 97% of its initial response span after 10,000 loading-unloading cycles with traces retaining continuity through 1,280 tight-fist folding cycles. The shared taxel layout supports human-robot co-training with a common tactile encoder and no learned cross-sensor mapping. Across three contact-rich manipulation tasks, tactile observations improve in-distribution success over vision-only policies. With a fixed robot demonstration budget, adding human demonstrations more than doubles mean success across eight evaluation conditions, from 22.8% to 45.9%, improving success in all five out-of-distribution conditions. We plan to open-source the resources needed to fabricate and operate these skins.
