---
interest: medium
link: https://arxiv.org/abs/2608.27507
next_step: skim
priority: high
slack_ts: '1788237855.603979'
source: cs.LG - Machine Learning
status: unread
title: Marginal Coverage Credit Reduces Redundant Exploration in Parallel State-Entropy
  Optimization
---
# Marginal Coverage Credit Reduces Redundant Exploration in Parallel State-Entropy Optimization
> 原文: [https://arxiv.org/abs/2608.27507](https://arxiv.org/abs/2608.27507)

arXiv:2608.27507v1 Announce Type: new
Abstract: Policy Gradient for Parallel State Entropy maximization (PGPSE) expands state-space coverage by training independently parameterized policies in replicated copies of the same environment. However, its pooled team-entropy score measures only collective exploration and cannot identify policies that contribute non-redundant coverage. We introduce Marginal Coverage Credit for PGPSE (MCC-PGPSE), which combines leave-one-policy-out coverage with state-owner specialization to estimate policy-specific credit. MCC-PGPSE preserves PGPSE's pooled objective and redistributes non-negative auxiliary intrinsic rewards according to these credits without changing their total mass. This redistribution is designed to discourage redundant visitation and promote complementary coverage. We evaluated MCC-PGPSE in controlled environments, seven public discrete-state benchmarks, and representative Room and Maze settings from the original PGPSE protocol. Across all tested settings, MCC-PGPSE produced positive final window gains in normalized team state entropy and state support over the Entropy baseline. Controlled-task comparisons and the fixed-suite public aggregate were significant, whereas five-seed original-protocol comparisons were directionally consistent. Ablations and credit alignment controls indicate that most gains arise from leave-one-policy-out coverage rather than non-uniform weighting, mismatched credit, or neural novelty alone. These results support contribution-conditioned auxiliary reward allocation as an interpretable approach to improving complementary coverage among parallel policies in discrete state spaces.
