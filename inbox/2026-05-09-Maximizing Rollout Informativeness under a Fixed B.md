---
title: "Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of Tree Search for Tool-Use Agentic Reinforcement Learning"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.05262
priority: medium
status: unread
interest: medium
next_step: skim
---
# Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of Tree Search for Tool-Use Agentic Reinforcement Learning
> 原文: [https://arxiv.org/abs/2605.05262](https://arxiv.org/abs/2605.05262)

arXiv:2605.05262v1 Announce Type: new
Abstract: We formalize Rollout Informativeness under a Fixed Budget (RIFB) as the expected non-vanishing policy-gradient mass that a tool-use rollout set injects into Group Relative Policy Optimization (GRPO). We prove that any budget-agnostic independent sampler suffers a collapse rate bounded away from zero for hard prompts regardless of the budget. Motivated by this, we recast intermediate state selection as a monotone submodular maximization problem, where a greedy one-step selector enjoys a 1 minus 1/e approximation guarantee.
Our Uncertainty-aware Upper Confidence Bound (UUCB) terms arise as closed-form marginal gains of this objective. This turns the token-level entropy bonus from an empirical trick into an analytic consequence of the formulation. We present InfoTree, a training-time tree-search framework coupling UUCB with a learned Adaptive Budget Allocator (ABA) and an asynchronous Speculative Expansion scheme.
ABA rescues prompts whose initial tree is wasted on uniform outcomes, lifting the mixed-outcome ratio from 58.1 percent to 76.3 percent with less than 5 percent budget overhead. Speculative Expansion reduces wall-clock overhead from 14.3 percent to 4.8 percent by tolerating bounded staleness in UUCB scores.
Across nine benchmarks spanning math reasoning (AIME 2024 and 2025, MATH-500, OlympiadBench, USAMO), web-search agents (GAIA, HLE-100, BrowseComp-lite), and tool-rich coding and OS agents (APPS-verified, AgentBench-OS), InfoTree outperforms flat GRPO, DeepSearch, Tree-GRPO, AT2PO, CW-GRPO, and RC-GRPO. Head-to-head compositions with Tree-GRPO prefix sharing and CW-GRPO contribution weights deliver further gains, confirming that our selector operates orthogonally to rollout reuse and trajectory re-weighting. A 5 by 5 by 5 robustness grid reveals that over three quarters of the hyperparameter space lies on a performance plateau, confirming UUCB robustness.
