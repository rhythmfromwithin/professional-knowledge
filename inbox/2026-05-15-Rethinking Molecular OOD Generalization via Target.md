---
interest: medium
link: https://arxiv.org/abs/2605.13932
next_step: skim
priority: high
slack_ts: '1778990761.041749'
source: cs.LG - Machine Learning
status: unread
title: Rethinking Molecular OOD Generalization via Target-Aware Source Selection
---
# Rethinking Molecular OOD Generalization via Target-Aware Source Selection
> 原文: [https://arxiv.org/abs/2605.13932](https://arxiv.org/abs/2605.13932)

arXiv:2605.13932v1 Announce Type: new
Abstract: Robust prediction of molecular properties under extreme out-of-distribution (OOD) scenarios is a pivotal bottleneck in AI-driven drug discovery. Current scaffold-splitting protocols fail to obstruct microscopic semantic overlap, predisposing models to shortcut learning and overestimating their true extrapolation capability; meanwhile, conventional domain adaptation paradigms suffer under extreme structural shifts, as blindly aligning heterogeneous source libraries injects topological noise and triggers negative transfer. To address these two challenges, scaffold-cluster out-of-distribution performance evaluation benchmark (SCOPE-BENCH), a benchmark built on cluster-level partitioning in an explicit physicochemical descriptor space, is proposed alongside policy optimization for multi-source adaptation (POMA), a framework that formulates knowledge transfer as a retrieve-compose-adapt pipeline: labeled source scaffolds structurally close to the unlabeled target are first identified as proxy targets; a reinforcement learning policy then adaptively selects the optimal source subset from an exponentially large candidate pool; and dual-scale domain adaptation is finally performed at macroscopic topological and microscopic pharmacophore scales. Evaluations show that prediction errors of state-of-the-art 3D molecular models surge by up to 8.0x on SCOPE-BENCH with a mean of 5.9x, while POMA achieves up to an 11.2% reduction in mean absolute error with an average relative improvement of 6.2% across diverse backbone architectures. Code is available at https://anonymous.4open.science/r/Molecular-OOD-Code-73F6.
