---
title: "Shared Vulnerabilities in Robustness-Optimized Defenses: One Breach Exposes the Family"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.18339
priority: low
status: unread
interest: medium
next_step: skim
---
# Shared Vulnerabilities in Robustness-Optimized Defenses: One Breach Exposes the Family
> 原文: [https://arxiv.org/abs/2607.18339](https://arxiv.org/abs/2607.18339)

arXiv:2607.18339v1 Announce Type: new
Abstract: Adversarial robustness optimization aims to preserve correct prediction under adversarial perturbations, and has produced substantial robustness gains through methods such as adversarial training and adversarial purification. However, we identify a new security risk: these gains can create shared vulnerabilities across defenses. Once one representative robustness-optimized defense is effectively breached, the broader family may become exposed. Studying this risk requires separating genuine transferability from distortion-induced degradation and from the algorithmic gains of sophisticated attacks. We therefore introduce stricter transfer-only protocols and a deliberately simple adaptive attack, PGDTransfer, to test whether robustness-optimized defenses share transfer-only vulnerability under controlled conditions. We further introduce Adversarial Sensitivity Maps (AdvSMs) to visualize and quantify shared alignment beyond differentiable classifiers, including stochastic and non-differentiable defenses. Across adversarially trained classifiers, purification-based defenses, and LVLMs with robust visual encoders, we identify natural transferability within each robustness family, i.e., transfer that arises even with simple PGD-style optimization rather than specialized transferable-attack design. The risk is already severe for purification: PGDTransfer reaches an average transfer attack success rate of $80.4\%$ across filtering-, compression-, and diffusion-based purifiers under $\epsilon=4/255$, suggesting that purifier defenses may no longer provide reliable protection. As attacks improve, currently stronger robustness families may face the same risk. Future defenses should therefore treat vulnerability diversity and transfer-only isolation as security objectives, rather than optimizing only individual robustness.
