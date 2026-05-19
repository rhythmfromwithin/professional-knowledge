---
interest: medium
link: https://arxiv.org/abs/2605.16398
next_step: skim
priority: medium
slack_ts: '1779164095.655389'
source: cs.RO - Robotics
status: unread
title: Support-Safe Variational Hybrid Filtering for Contact-Mode and Sparse-Law Recovery
---
# Support-Safe Variational Hybrid Filtering for Contact-Mode and Sparse-Law Recovery
> 原文: [https://arxiv.org/abs/2605.16398](https://arxiv.org/abs/2605.16398)

arXiv:2605.16398v1 Announce Type: new
Abstract: Contact-rich robot dynamics are hybrid: a single observation can match several latent states and contact regimes (free, impact, stick--slip). A standard amortized filter that places no probability on a feasible contact transition will permanently lose the branch the robot actually follows. We introduce VHYDRO, a variational hybrid dynamics learner that prevents this branch loss. At each step, VHYDRO mixes the learned proposal with a feasible transition law before sampling and importance weighting, ensuring that every transition retained by the model-feasible carrier remains covered. VHYDRO jointly infers a continuous latent state and a discrete contact mode, and fits a sparse port-Hamiltonian law to each recovered regime. On top of this, three guarantees connect: support coverage stabilizes filtering, the stabilized filter concentrates the discrete contact posterior on coherent regimes, and mode-pure segments admit sparse port-Hamiltonian recovery. The recovery error separates cleanly into filtering, derivative, mode-impurity, and physics-residual parts. Three empirical findings track the same mechanism. Under heavy occlusion the support-safe filter stays usable while a non-defensive proposal collapses. On ManiSkill demonstrations and on four Sawyer/BridgeData task families the discrete state forms temporally coherent contact-regime segments that the discrete state yields a stronger joint profile across ARI, change-point F1, and segment purity than post-hoc and mode-free baselines. On hybrid systems with known equations the mode-conditioned sparse fit recovers the active physical terms; purely predictive baselines do not.
