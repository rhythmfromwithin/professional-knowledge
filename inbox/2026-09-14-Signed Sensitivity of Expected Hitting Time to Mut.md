---
title: "Signed Sensitivity of Expected Hitting Time to Mutation Rate in the (1+1) EA: Per-State Sign Theorems and Verifiable Certificates for Non-Lumpable Families"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2609.12510
priority: low
status: unread
interest: medium
next_step: skim
---
# Signed Sensitivity of Expected Hitting Time to Mutation Rate in the (1+1) EA: Per-State Sign Theorems and Verifiable Certificates for Non-Lumpable Families
> 原文: [https://arxiv.org/abs/2609.12510](https://arxiv.org/abs/2609.12510)

arXiv:2609.12510v1 Announce Type: new
Abstract: For the (1+1) evolutionary algorithm with standard bit mutation, we study the sensitivity of the expected hitting time $H\_p=\mathbb{E}\_x T$ to the mutation rate. We first point out an easily overlooked formalization pitfall: the improvement event is not monotone in the mutation mask, so the unsigned (total-influence) form of the Margulis-Russo formula does not apply; the correct object is the signed endpoint difference. Second, we give an exact three-dimensional separation: two fitness functions share the entire one-step success-rate curve, yet their expected hitting times are two different exact rational numbers; hence one-step success-rate quantities do not determine the expected hitting time. Building on the runtime derivative $H'\_p=(I-Q\_p)^{-1}Q'\_p H\_p$, we construct computable double-residual sign certificates, prove a per-initial-state sign theorem on OneMax (for every non-optimal initial state, $\partial\_c H<0$ on $0<1$, where $p=c/n$; at $c=1$ only the distance-one state is stationary), and extend the framework to non-lumpable positive linear families: an explicit non-lumpability witness, a block-interval double-residual certificate that covers all states without enumerating them, a uniform sign bound $\partial\_c\mathbb{E}T\le -9n/16$ over the whole interval $c\in[1/4,1/2]$ for an explicit family at all even scales $n\ge 8$, and a heterogeneous instance certificate $H'\_x\le -1/6$ on 57 of 63 states across $c=1$. All finite verifications use exact rational arithmetic. A bounded systematic literature search did not uncover this exact combination, although the underlying tools are well established; we therefore make no novelty claim beyond the stated combination.
