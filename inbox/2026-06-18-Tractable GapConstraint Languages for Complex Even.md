---
interest: medium
link: https://arxiv.org/abs/2606.18878
next_step: skim
priority: low
slack_ts: '1781847255.389869'
source: cs.DB - Databases
status: unread
title: Tractable Gap-Constraint Languages for Complex Event Recognition
---
# Tractable Gap-Constraint Languages for Complex Event Recognition
> 原文: [https://arxiv.org/abs/2606.18878](https://arxiv.org/abs/2606.18878)

arXiv:2606.18878v1 Announce Type: cross
Abstract: For strings $u, D \in \Sigma^\*$, a subsequence embedding of $u$ in $D$ is a function $e \colon \{1, 2, \ldots, |u|\} \to \{1, 2, \ldots, |D|\}$ with $e(i) < e(i+1)$ for every $i \in \{1, 2, \ldots, |u|-1\}$ and the $i$-th symbol of $u$ equals the $e(i)$-th symbol of $D$. A gap-constraint for $u$ is a triple $(i, j, L)$ with $1 \leq i < j \leq |u|$ and $L$ is a regular language over $\Sigma$. An embedding $e$ satisfies a gap-constraint $(i, j, L)$ if the factor of $D$ strictly between positions $e(i)$ and $e(j)$ is a word from $L$. We investigate the subsequence matching problem with gap-constraints, which is relevant in the context of complex event recognition (CER): given $u, D \in \Sigma^\*$ and a set $C$ of gap-constraints, find an embedding of $u$ in $D$ that satisfies all gap-constraints from $C$.
In general, subsequence matching is NP-complete and the only known tractable variants restrict the interval structure of the gap-constraints. In this work, we show that we can solve subsequence matching with gap-constraints with an arbitrary interval structure rather efficiently (in fact, optimally under SETH) in time $O(|D| (|u| + |C|))$ if the gap-constraint languages satisfy a property which we dub left-convexity: whenever $u v w \in L$ and $v \in L$, then also $uv \in L$. Left-convex languages are sufficiently expressive to model interesting real-world scenarios considered in CER, e.g., length constraints $L = \{w \mid a \leq |w| \leq b\}$ for $a, b \in \mathbb{N}$. We also show how our algorithm can be used in order to efficiently enumerate all satisfying embeddings, which is particularly relevant for possible applications in CER. Finally, we show how non-left-convex languages can lead to intractability, i.e., if in addition to length constraints we allow $\{aa, \epsilon\}$ as the only non-left-convex constraint language, then the problem is NP-complete again.
