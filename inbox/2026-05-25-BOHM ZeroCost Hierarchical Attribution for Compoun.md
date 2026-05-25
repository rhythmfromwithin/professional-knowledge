---
title: "BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.22866
priority: high
status: unread
interest: medium
next_step: skim
---
# BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems
> 原文: [https://arxiv.org/abs/2605.22866](https://arxiv.org/abs/2605.22866)

arXiv:2605.22866v1 Announce Type: new
Abstract: Compound AI systems route tasks through hierarchies of specialised components. Attribution is dominated by Shapley-based methods (SHAP), which decompose a coalition value function into per-component marginal contributions and require evaluation of the system on arbitrary component subsets. That requirement fails for third-party APIs, opaque endpoints, and agentic orchestrators that concentrate routing on a few tools, leaving most coalitions un-evaluable from the deployed orchestrator. We introduce BOHM, which extracts a hierarchical attribution tree directly from the routing weights such systems already maintain: leaf attribution is the path product of root-to-leaf routing weights; level-k attribution is the induced distribution over depth-k nodes. The method has zero marginal cost, requires no access to component internals, and provides multi-resolution attribution at every level simultaneously, which flat methods cannot offer at any evaluation budget. BOHM and SHAP answer different questions and converge when the deployed router routes near-optimally. On 18 LLMs in a 3-level hierarchy over 880 LiveCodeBench problems, BOHM yields Kendall tau=0.928; SHAP reaches tau=0.980 at 9,000x more coalition evaluations per seed. On a 5-driver, 7-benchmark agentic study (35 cells, complete coverage), drivers concentrate routing on a single tool (top-share median 0.65), and cell-level tau(BOHM,SHAP) is predicted by whether the driver's top pick is the empirically best tool (mean +0.22 vs ~+0.01). On a US Census hierarchy (475 leaves, 4 levels), BOHM recovers ground-truth rankings at every level (tau up to 0.722). BOHM satisfies efficiency, monotonicity, symmetry, and weak suppression but not Shapley's additivity. It is best understood as a complementary primitive: a multi-resolution decomposition computable wherever routing state exists, whose disagreement with Shapley is itself diagnostic.
