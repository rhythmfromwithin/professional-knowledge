---
interest: medium
link: https://arxiv.org/abs/2607.14413
next_step: skim
priority: medium
slack_ts: '1784519284.317749'
source: cs.DC - Distributed Computing
status: unread
title: Settling The Round Complexity of Byzantine Agreement Against a Full-Information,
  Adaptive Adversary
---
# Settling The Round Complexity of Byzantine Agreement Against a Full-Information, Adaptive Adversary
> 原文: [https://arxiv.org/abs/2607.14413](https://arxiv.org/abs/2607.14413)

arXiv:2607.14413v1 Announce Type: new
Abstract: We prove that every randomized synchronous Byzantine Agreement protocol in the full-information, strongly adaptive adversary model, secure against $t$ corrupt parties, has worst-case expected round complexity \[
\Omega\!\left(\frac{t^2}{n\log(n+1)}\right). \] This improves upon the seminal $\Omega(\frac{t}{\sqrt{n\log n}})$ bound of [Bar-Joseph, Ben-Or 98]. Our result matches the recent upper bound of $O\left(\min\left\{\frac{t^2\log n}{n},\frac{t}{\log n}\right\}\right)$ of [Dufoulon, Pandurangan 25], up to a $\log^2 n$ factor in the $t\ll n$ regime. Our proof takes inspiration from the recent works of [Etesami, Mahloujifar, Mahmoody 20] and [Haitner, Karidi-Heller 26]. Specifically, we prove a multi-round concentration lemma showing that any transcript event of probability $p$ can be forced with probability one by corrupting $O(\sqrt{n\log(\frac1p)})$ parties in expectation. From there, tools from [Chor, Merritt, Shmoys 89] allow us to lower-bound the probability of the protocol not concluding in $R$ rounds by $\frac{1}{n^{O(R)}}$, using a crash schedule involving at most $R$ parties. The combination of these techniques yields the desired bound.
