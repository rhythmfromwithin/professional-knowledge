---
title: "TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.00285
priority: high
status: unread
---
# TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?
> 原文: [https://arxiv.org/abs/2603.00285](https://arxiv.org/abs/2603.00285)

arXiv:2603.00285v1 Announce Type: new
Abstract: Evaluating AI agents in finance faces two key challenges: static benchmarks require costly expert annotation yet miss the dynamic decision-making central to real-world trading, while LLM-based judges introduce uncontrolled variance on domain-specific tasks. We introduce TraderBench, a benchmark that addresses both issues. It combines expert-verified static tasks (knowledge retrieval, analytical reasoning) with adversarial trading simulations scored purely on realized performance-Sharpe ratio, returns, and drawdown-eliminating judge variance entirely. The framework features two novel tracks: crypto trading with four progressive market-manipulation transforms, and options derivatives scoring across P&L accuracy, Greeks, and risk management. Trading scenarios can be refreshed with new market data to prevent benchmark contamination. Evaluating 13 models (8B open-source to frontier) on ~50 tasks, we find: (1) 8 of 13 models score ~33 on crypto with <1-point variation across adversarial conditions, exposing fixed non-adaptive strategies; (2) extended thinking helps retrieval (+26 points) but has zero impact on trading (+0.3 crypto, -0.1 options). These findings reveal that current agents lack genuine market adaptation, underscoring the need for performance-grounded evaluation in finance.
