---
title: "VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.04355
priority: medium
status: unread
interest: medium
next_step: skim
---
# VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2609.04355](https://arxiv.org/abs/2609.04355)

arXiv:2609.04355v1 Announce Type: new
Abstract: Pretrained vision-language-action (VLA) models enable broad manipulation but remain unreliable in tasks demanding precision and repeatability. Applying real-world online reinforcement learning (RL) to VLA post-training enables autonomous trial-and-error improvement beyond demonstrations alone, but exposes two bottlenecks: 1) unreliable value signals can induce policy drift; 2) large-VLA overhead constrains throughput and sample efficiency. To address these challenges, we present VLA-Precision, an efficient real-world online RL framework featuring the Asymmetric Co-Bootstrapping (ACoB) algorithm and the ACoB-Stream architecture. Specifically, ACoB establishes asymmetric co-bootstrapping across timescales: early intervention-guided behavioral learning rapidly improves policy performance while enhancing online experience quality. As autonomous experience accumulates, global return propagation and local preference ranking progressively calibrate value estimates, yielding relative action advantages for reference-regularized policy improvement while suppressing drift. To enable ACoB on large VLAs, we develop ACoB-Stream, a closed-loop experience--policy architecture that establishes invariant-state decoupling and on-demand streaming as design principles, delivering up to 10.9$\times$ improvements in throughput and computational efficiency. Extensive evaluations on nine high-precision chemistry tasks across four categories and four robot embodiments show that VLA-Precision achieves 98.3\% mean success rate in 45.8 min/task, with 27.6 s episodes running at 1.2$\times$ and 1.8$\times$ the speeds of VLA and RL baselines. Resources are available at https://vla-precision.github.io.
