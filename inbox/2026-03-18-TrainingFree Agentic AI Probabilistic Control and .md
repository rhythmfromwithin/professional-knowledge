---
interest: medium
link: https://arxiv.org/abs/2603.13256
next_step: skim
priority: high
slack_ts: '1774234417.919839'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent
  LLM Systems'
---
# Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems
> 原文: [https://arxiv.org/abs/2603.13256](https://arxiv.org/abs/2603.13256)

arXiv:2603.13256v1 Announce Type: new
Abstract: Multi-agent large language model (LLM) systems enable complex, long-horizon reasoning by composing specialized agents, but practical deployment remains hindered by inefficient routing, noisy feedback, and high interaction cost. We introduce REDEREF, a lightweight and training-free controller for multi-agent LLM collaboration that improves routing efficiency during recursive delegation. REDEREF integrates (i) belief-guided delegation via Thompson sampling to prioritize agents with historically positive marginal contributions, (ii) reflection-driven re-routing using a calibrated LLM or programmatic judge, (iii) evidence-based selection rather than output averaging, and (iv) memory-aware priors to reduce cold-start inefficiency. Across multi-agent split-knowledge tasks, we show that while recursive retry alone saturates task success, belief-guided routing reduces token usage by 28%, agent calls by 17%, and time-to-success by 19% compared to random recursive delegation, and adapts gracefully under agent or judge degradation. These results demonstrate that simple, interpretable probabilistic control can meaningfully improve the efficiency and robustness of multi-agent LLM systems without training or fine-tuning.
