---
interest: medium
link: https://arxiv.org/abs/2607.00024
next_step: skim
priority: medium
slack_ts: '1782965356.054269'
source: cs.RO - Robotics
status: unread
title: Decentralized Geometric Control for Cable-Suspended Payload Transport with
  Adaptive Mass Estimation
---
# Decentralized Geometric Control for Cable-Suspended Payload Transport with Adaptive Mass Estimation
> 原文: [https://arxiv.org/abs/2607.00024](https://arxiv.org/abs/2607.00024)

arXiv:2607.00024v1 Announce Type: new
Abstract: Cooperative aerial transport requires controllers that respect nonlinear manifold geometry, operate without centralized coordination, and respect operational safety constraints. To address these demands, we present GPAC, a four-layer hierarchical architecture that enables $N$ quadrotors to transport a cable-suspended payload without a central coordinator or by exchanging cable states or adaptive parameters. The key insight is implicit coordination: each quadrotor independently estimates its effective load share from local cable measurements, so combined forces converge to the correct total, even without knowledge of $N$ or the payload mass; the payload position is reconstructed locally from each agent's own cable geometry, and the only inter-agent communication is a low-rate neighbor-position broadcast for collision avoidance. GPAC operates directly on the full nonlinear configuration manifold and integrates geometric position and attitude control, anti-swing regulation, an extended-state observer for wind rejection, concurrent learning-based mass estimation without persistent excitation, and a priority-ordered control barrier function (CBF)-inspired safety filter that reduces operational risk, with input-to-state safety (ISSf) margins that hold exactly under single-constraint activation. A compatibility result shows that the filter's force modifications keep the desired attitude within the almost-global stability region of the $\mathrm{SO}(3)$ attitude controller. Finally, high-fidelity simulation with flexible cables, onboard sensor fusion, and wind turbulence -- with all control and estimation loops closed through the estimator -- yields a mean payload-tracking RMSE of 33.8 cm (2.8\% coefficient of variation over 13 seeds) at a low per-agent computational cost.
