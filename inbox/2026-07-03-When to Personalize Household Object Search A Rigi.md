---
interest: medium
link: https://arxiv.org/abs/2607.00022
next_step: skim
priority: medium
slack_ts: '1783050944.468239'
source: cs.RO - Robotics
status: unread
title: 'When to Personalize Household Object Search: A Rigidity-Gated Hybrid Policy'
---
# When to Personalize Household Object Search: A Rigidity-Gated Hybrid Policy
> 原文: [https://arxiv.org/abs/2607.00022](https://arxiv.org/abs/2607.00022)

arXiv:2607.00022v2 Announce Type: new
Abstract: Service robots searching for household objects rely on spatial priors to reduce search cost, yet object locations can vary with resident traits. Collecting longitudinal, trait-specific in-home trajectories is invasive and hard to scale. We study when personalization helps and propose PerSim, a rigidity-gated hybrid policy that combines a trait-conditioned prior with a population-frequency baseline, personalizing only when placement behavior is variable. To scale resident-conditioned dynamics, we employ a human-calibrated simulation pipeline to generate and validate object-placement transitions in diverse home layouts, and train a predictor that injects continuous Big Five vectors to output room-level priors and within-room co-occurrence cues. In a unified human study (N=200), dual-layer validation shows that (i) synthetic transitions are judged behaviorally plausible (mean 3.85/5, p < 1e-6), and (ii) in a blinded A/B comparison, personalization is favored primarily for low-rigidity objects (p=0.005), while the population-frequency baseline remains strong for universally placed items, yielding a decision rule for when to personalize. In an offline objective test, we observe a small but significant improvement on unseen continuous trait vectors over nearest discrete configuration matching (p=0.035), supporting interpolation in five-dimensional trait space. Finally, in a home digital twin we show that PerSim reduces expected search cost by combining room visitation effort with within-room cue checking, demonstrating end-to-end gains beyond isolated prediction metrics.
