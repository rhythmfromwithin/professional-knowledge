---
title: "Conjunctive Queries with Negation: Beyond Signed-Acyclicity"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.03982
priority: low
status: unread
interest: medium
next_step: skim
---
# Conjunctive Queries with Negation: Beyond Signed-Acyclicity
> 原文: [https://arxiv.org/abs/2610.03982](https://arxiv.org/abs/2610.03982)

arXiv:2610.03982v1 Announce Type: new
Abstract: We study constant-delay enumeration for conjunctive queries with negation ($\texttt{CQ}^{\neg}$). Prior work defined \emph{signed-acyclicity}, which characterizes the class of queries where linear preprocessing time is achievable, but little has been known beyond this. We introduce a new hypergraph width measure for $\texttt{CQ}^{\neg}$, the \emph{signed fractional hypertree width} ($\textsf{sfhw}$), defined by requiring that a single variable order simultaneously handle every subset of the negative atoms. We show that $\textsf{sfhw}$ strictly generalizes signed-acyclicity (recovered when $\textsf{sfhw} = 1$) and fractional hypertree width (recovered on queries without negation). Our main algorithmic result is a variable-elimination algorithm that achieves constant-delay enumeration on input $I$ for any full $\texttt{CQ}^{\neg}$ query with preprocessing time $O(|I|^{\textsf{sfhw}})$. We further show that using multiple variable orders can improve this bound, exhibiting an $O(|I|^{3/2})$ algorithm for $k$-cycle queries with at least one negative edge.
