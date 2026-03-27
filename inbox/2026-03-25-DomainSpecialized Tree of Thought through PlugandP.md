---
interest: medium
link: https://arxiv.org/abs/2603.20267
next_step: skim
priority: high
slack_ts: '1774581543.735279'
source: cs.AI - Artificial Intelligence
status: unread
title: Domain-Specialized Tree of Thought through Plug-and-Play Predictors
---
# Domain-Specialized Tree of Thought through Plug-and-Play Predictors
> 原文: [https://arxiv.org/abs/2603.20267](https://arxiv.org/abs/2603.20267)

arXiv:2603.20267v1 Announce Type: new
Abstract: While Large Language Models (LLMs) have advanced complex reasoning, prominent methods like the Tree of Thoughts (ToT) framework face a critical trade-off between exploration depth and computational efficiency. Existing ToT implementations often rely on heavyweight LLM-based self-evaluation or rigid heuristics for branch pruning, making them prohibitively expensive and inflexible for broad application. To address this, we introduce DST, an adaptable, plug-and-play predictor that serves as a lightweight, supervised heuristic to guide the ToT search process. Our predictor enables dynamic, context-aware pruning, allowing the search to proceed with near-greedy efficiency on simpler reasoning steps while adaptively expanding the search beam only when encountering uncertainty or task complexity. We evaluate our approach on a diverse suite of benchmarks spanning mathematical reasoning, general reasoning, and complex logical reasoning. Experimental results demonstrate that our method achieves accuracy competitive with or superior to strong baselines, including standard ToT, while reducing computational overhead by 26-75%. Our work effectively resolves the accuracy-efficiency trade-off in tree-based reasoning, transforming ToT from a resource-intensive technique into a scalable and practical paradigm for complex problem-solving in LLMs.
