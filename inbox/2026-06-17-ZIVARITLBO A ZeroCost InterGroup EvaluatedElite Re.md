---
interest: medium
link: https://arxiv.org/abs/2606.17087
next_step: skim
priority: low
slack_ts: '1781759638.530219'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'ZIVARI-TLBO: A Zero-Cost Inter-Group Evaluated-Elite Relay Mechanism for Teaching-Learning-Based
  Optimization'
---
# ZIVARI-TLBO: A Zero-Cost Inter-Group Evaluated-Elite Relay Mechanism for Teaching-Learning-Based Optimization
> 原文: [https://arxiv.org/abs/2606.17087](https://arxiv.org/abs/2606.17087)

arXiv:2606.17087v1 Announce Type: new
Abstract: ZIVARI-TLBO is a grouped Teaching-Learning-Based Optimization (TLBO) method that augments an existing population-state controller with a fixed inter-group evaluated-elite relay. At each scheduled event, every group offers its already evaluated elite to the next group in a fixed ring; the elite replaces the receiver's worst eligible learner only when its stored objective value is better. Because the exact relay copies an already evaluated solution and its stored fitness, it requires no additional objective-function calls. The frozen gts-v4-cm-fixed implementation is evaluated under equal 10,000-evaluation budgets on eight classical functions at dimensions 10, 30, 50, and 100, with 30 matched seeds, and on five constrained engineering problems. A direct ablation against the same grouped landscape-aware controller without relay records 728/11/221 wins/ties/losses and a rank-biserial effect size of 0.624 across dimensions. In an eight-method multidimensional comparison, WOA obtains the best average rank (2.914) and ZIVARI-TLBO ranks second (3.382); ZIVARI-TLBO significantly outperforms TLBO, MCTLBO, DE, PSO, and GWO, loses significantly to WOA, and is not significantly different from HHO after Holm adjustment. Feasibility-aware engineering results are mixed and sensitive to the current static-penalty formulation. The evidence supports a scoped relay contribution and budget-consistent information-sharing mechanism, but not universal state-of-the-art, global-convergence, engineering-dominance, or CEC superiority claims.
