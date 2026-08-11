---
title: "Fairis: Fairness-Aware Aggregation with Provable Influence Containment against Fairness Poisoning Attacks in Collaborative Machine Learning"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.06469
priority: low
status: unread
interest: medium
next_step: skim
---
# Fairis: Fairness-Aware Aggregation with Provable Influence Containment against Fairness Poisoning Attacks in Collaborative Machine Learning
> 原文: [https://arxiv.org/abs/2608.06469](https://arxiv.org/abs/2608.06469)

arXiv:2608.06469v1 Announce Type: new
Abstract: Collaborative machine learning among financial institutions must be both group-fair and robust against deliberate adversarial manipulation. Existing fairness-aware aggregation methods remain formally vulnerable to fairness poisoning: a malicious client maximizing group disparity while preserving accuracy evades accuracy-based Byzantine defenses, and in our threat model FairFed's gap-based weighting can be gamed by an adversary who observes the global fairness score. We present Fairis, a server-side reweighting scheme in which each client's update receives the normalized weight $\omega\_k = \bar{w}\_k / \sum\_j \bar{w}\_j$ built from the unnormalized score $\bar{w}\_k = \eta - \mathcal{F}\_k$, with $\mathcal{F}\_k \in [0,1]$ the local Equal Opportunity Difference and $\eta > 1$ a security parameter. We prove three properties, Monotone Weight Reduction (MWR), Demographic Participation, and Non-Gamesmanship, extend MWR to colluding minority coalitions, and show that combining MWR with server-side norm clipping bounds the adversary's displacement of the global model by $\omega\_0 C$, strictly decreasing in its own reported disparity. Assuming honest score reporting, an assumption this paper does not discharge, Fairis is the only rule evaluated that guarantees every client strictly positive weight while provably reducing an adversary's weight monotonically in its bias; clipped FairFed can reach a lower weight but guarantees nothing and zeroes a client outright on Taiwan Credit. Against an adversary stealthy enough to evade accuracy-based defenses, within 0.04 accuracy of benign, Fairis cuts its weight by 41 to 54% below a size-blind control on Taiwan. On routine non-IID partitions no rule dominates, and a uniform-weighting ablation shows that containment tracks how far the adversary's score separates from the honest mean, providing none when the honest population is already unfair.
