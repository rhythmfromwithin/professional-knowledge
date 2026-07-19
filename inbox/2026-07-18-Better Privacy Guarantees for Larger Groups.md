---
interest: medium
link: https://arxiv.org/abs/2607.14406
next_step: skim
priority: low
slack_ts: '1784432005.189189'
source: cs.CR - Cryptography and Security
status: unread
title: Better Privacy Guarantees for Larger Groups
---
# Better Privacy Guarantees for Larger Groups
> 原文: [https://arxiv.org/abs/2607.14406](https://arxiv.org/abs/2607.14406)

arXiv:2607.14406v1 Announce Type: new
Abstract: Pujol and Desfontaines asked whether a private histogram can allow more error on larger counts and use that slack to protect members of larger groups more strongly. We study this question for fixed disjoint groups under add-or-remove-one adjacency. The privacy budget $v(n)$ depends on the affected count, is nonincreasing, and must bound both R\'enyi-divergence directions at every order. This is the count-dependent form of zero-concentrated differential privacy (zCDP) studied here. The original strict relative-error condition is impossible at count zero. We therefore make the boundary tolerance explicit by requiring $\mathbb{E}\lvert\widehat{x}\_i-x\_i\rvert < r\max\{x\_i,1\}$, without changing the requirement at any positive count. Our main result determines the best dependence on group size. For the upper bound, we directly specialize an existing shifted-transformation framework. The resulting shifted-log Gaussian mechanism has a certified budget $v(n)=O\_r(n^{-2})$. Conversely, for every fixed $0<1$, any mechanism satisfying the same positive-count utility requirement and count-dependent zCDP must have $v(n)=\Omega\_r(n^{-2})$. Thus the inverse-square rate is optimal under the repaired formulation. A many-count information argument further places the leading coefficient in the large-count-then-small-error limit between $\pi/(4e^2)$ and $1/\pi$, a factor below three. At $r=1$, a data-independent release meets the repaired criterion with zero privacy loss.
