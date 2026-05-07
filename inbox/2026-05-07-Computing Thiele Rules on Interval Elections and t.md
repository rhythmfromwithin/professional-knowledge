---
title: "Computing Thiele Rules on Interval Elections and their Generalizations"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.03067
priority: high
status: unread
interest: medium
next_step: skim
---
# Computing Thiele Rules on Interval Elections and their Generalizations
> 原文: [https://arxiv.org/abs/2605.03067](https://arxiv.org/abs/2605.03067)

arXiv:2605.03067v1 Announce Type: new
Abstract: Approval-based committee voting has received significant attention in the social choice community. Among the studied rules, Thiele rules, and especially Proportional Approval Voting (PAV), stand out for desirable properties such as proportional representation, Pareto optimality, and support monotonicity. Their main drawback is that computing a Thiele outcome is NP-hard in general.
A glimpse of hope comes from the fact that Thiele rules are better behaved under structured preferences. On the candidate interval (CI) domain, they are computable in polynomial time via a linear program (LP) that has a totally unimodular constraint matrix. Surprisingly, this approach fails for the related voter interval (VI) domain, and the complexity of the problem has repeatedly been posed as an open question. Our main result resolves this question: although the relevant matrix is not totally unimodular, the ``standard'' LP still admits at least one optimal integral solution, and we provide a fast algorithm for finding it.
Our technique naturally extends to the voter-candidate interval (VCI) domain, also known as the 1-dimensional voter-candidate range (1D-VCR) domain, and to the linearly consistent (LC) domain, both of which generalize the candidate and voter interval domains. Although both the VCI and LC domains have been studied in social choice, their relationship was unknown. We show, through connections to graph theory, that LC strictly contains VCI. We also provide an alternative definition of LC that is closer in spirit to VCI and has a natural interpretation in approval elections; this equivalence may be of independent interest. Finally, we study an alternative tree-based generalization of VCI and show that Thiele rules become NP-hard to compute on this domain.
