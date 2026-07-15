---
title: "Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.09992
priority: medium
status: unread
interest: medium
next_step: skim
---
# Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving
> 原文: [https://arxiv.org/abs/2607.09992](https://arxiv.org/abs/2607.09992)

arXiv:2607.09992v1 Announce Type: new
Abstract: Modern ML serving increasingly lets learned, unbounded components (routers, latency-SLO admitters, admit ladders) decide a tenant's quality of service; when one is wrong, the assured SLO can silently break, and the Kubernetes layers beneath (Kueue, DRA, the Gateway-API Inference Extension) only add cross-layer surprises. Rather than trust the learner to be right, we bound the damage a wrong one can do: a small trusted guard wraps the untrusted learner -- learned proposes, the guard disposes. A tenant's assured-SLO obligation splits into two parts with different epistemics. Its safety projection (per-request dispatch feasibility and a per-class, per-window service floor) is a controllable obligation the guard enforces at runtime, regardless of an arbitrarily-wrong learned admitter, by reservation and priority dispatch. Its aggregate obligation (a tail-latency percentile) is a statistical residual with no per-request enforcement point; a cheap deterministic screen for it is optimistically unsound not only near saturation but well below it. On real 2xV100 the guard holds assured-class miss 0.0 (reps 10, worst upper Wilson CI 0.0053) across every miscalibration of a learned admitter under two shed policies that fail in opposite directions. Against a real, deployed GAIE Flow Control on a serving simulator, a mislabelling router flips the same assured requests from miss 0.0 to 1.0; our guard reserves by the true class, so the label cannot break its floor. We characterize when a cheap static screen can be trusted and when it cannot. As a Frontiers-style submission we evaluate the stance on commodity 2xV100 and a serving simulator, and scope datacenter scale, real-model Flow Control, and a closed worst-case theorem as the agenda.
