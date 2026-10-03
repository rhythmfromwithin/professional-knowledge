---
interest: medium
link: https://arxiv.org/abs/2609.38375
next_step: skim
priority: medium
slack_ts: '1791003464.666729'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Lower Bounds for Linear-Oracle Online Learning
---
# Lower Bounds for Linear-Oracle Online Learning
> 原文: [https://arxiv.org/abs/2609.38375](https://arxiv.org/abs/2609.38375)

arXiv:2609.38375v1 Announce Type: new
Abstract: Can a constant number of linear minimizations per round improve on the $T^{3/4}$ regret rate of online Frank-Wolfe on general convex sets? Weibel et al. conjectured that fixed-coefficient methods cannot. We prove their conjecture and extend the lower bound to every deterministic learner in an oracle-only model. The learner receives an initial feasible point and a diameter bound, and must remain feasible on every domain consistent with its oracle replies. For $T$ rounds, at most $b$ calls between decisions, diameter bound $D$, and gradient norm bound $L$, we construct an instance in dimension $d=2b(T-1)+1$ with regret at least $2^{-1/4}LDb^{-1/4}T^{3/4}$. The adversary fixes the domain, initial point, deterministic tie rule and linear losses before play. The vertices form a path on which every point available before a decision has zero current loss, while the final vertex has negative loss on every round. For constant $b$, the result matches the known upper rate for dimension-independent guarantees. For one-call fixed schedules with a nonzero coefficient on the newest gradient, a second construction gives regret at least $3LDT^{3/4}/4$ with unique minimizers at every issued query. Exact-arithmetic certificates for the tuned schedule of Weibel et al. closely match their finite-horizon numerical worst cases, with unique oracle replies.
