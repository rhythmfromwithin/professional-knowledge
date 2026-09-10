---
interest: medium
link: https://arxiv.org/abs/2609.09867
next_step: skim
priority: low
slack_ts: '1789013731.241489'
source: cs.DB - Databases
status: unread
title: Contextual Utility of Quantization Moves in Extreme Low-Bit LLMs
---
# Contextual Utility of Quantization Moves in Extreme Low-Bit LLMs
> 原文: [https://arxiv.org/abs/2609.09867](https://arxiv.org/abs/2609.09867)

arXiv:2609.09867v1 Announce Type: new
Abstract: Post-training quantizers select finite code changes using reconstruction proxies or local loss approximations, but the utility of a quantization move depends on the state through which it is executed. We identify two sources of this contextual dependence. First, the displacement of the move matters: evaluating the gradient at the move midpoint captures curvature accumulated along the move that a current-state linearization omits. Across frozen two-bit moves from Llama-3.2 models, midpoint evaluation predicts the direction of exact endpoint loss changes substantially more accurately than current-state gradients. Second, moves interact: exhaustive lattices of legal quantized states are well approximated by quadratic pseudo-Boolean functions, yet their small pairwise components can determine Pareto fronts and cause different evaluation functionals to prefer opposite directions. These effects explain failures of reconstruction-optimal code re-selection and additive composition. Reading each move at its own midpoint repairs the local selection step and improves downstream accuracy and held-out perplexity, while larger supports require evaluating exact endpoints from the state actually reached. Exact-endpoint beam search finds sparse changes that dominate much larger one-shot updates, and repricing the same moves after intervening changes produces widespread sign reversals. These results show that quantization utility is contextual at the granularity of a few moves: reliable construction must evaluate finite changes along their own paths and compose them from the evolving quantized state.
