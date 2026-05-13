---
title: "MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.11002
priority: low
status: unread
interest: medium
next_step: skim
---
# MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks
> 原文: [https://arxiv.org/abs/2605.11002](https://arxiv.org/abs/2605.11002)

arXiv:2605.11002v1 Announce Type: new
Abstract: Multi-turn jailbreaks exploit the ability of large language models to accumulate and act on conversational context. Instead of stating a harmful request directly, an attacker can gradually steer the conversation toward an unsafe answer. Recent methods demonstrate this risk, but they are usually evaluated as black-box pipelines with different budgets, judges, retry rules, and strategy generation procedures. As a result, it is often unclear whether reported gains reflect stronger attack mechanisms or different experimental conditions. We introduce MT-JailBench, a modular evaluation framework for benchmarking multi-turn jailbreaks under fixed conditions. MT-JailBench implements each attack as five interacting modules: evaluation function, attack strategy, prompt generation, prompt refinement, and flow control. This design enables fair comparison across attack methods and component-wise analysis of what drives attack success. Using MT-JailBench, we find that resource budgets and evaluation functions are major confounders: controlling turns, retries, interactions, sampled strategies, and judges substantially change the ranking of attacks. At the component level, prompt generation accounts for most performance variation, while refinement and flow control provide moderate gains. We also find that explicit dynamic strategy generation is not always necessary; stochastic sampling from a fixed strategy can rival more elaborate diversification mechanisms. Finally, recomposing the best components yields a strong attack configuration that outperforms its source attacks and generalizes across diverse target LLMs. MT-JailBench therefore provides a modular framework for comparing multi-turn jailbreaks, understanding the impact of components, and guiding stronger red-teaming evaluations.
