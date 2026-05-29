---
title: "Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.28850
priority: high
status: unread
interest: medium
next_step: skim
---
# Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents
> 原文: [https://arxiv.org/abs/2605.28850](https://arxiv.org/abs/2605.28850)

arXiv:2605.28850v1 Announce Type: new
Abstract: We study behavioral alignment and representation dynamics of large language model (LLM) agents in financial decision environments. Using TradeArena, an auditable trading-agent testbed with risk reports, execution simulation, memory, and replayable trajectories, we analyze how rationales, positions, and interventions evolve under market stress. We find measurable pre-failure signatures: planning embeddings drift from normal-state centroids, fused plan-risk representations separate normal from pre-drawdown states, and manifold diagnostics show effective-rank contraction before failures. To address small-sample and embedding-choice concerns, we use 80 rolling failure anchors across eight LLM trajectories and show that contraction persists across hash, LSA, Transformer, and white-box hidden-state probes. Stress tests with CoT-free target weights, lexical controls, OHLCV noise, and false-audit reports indicate that rationale-level contraction can vanish without rationales, while intent-space contraction may remain; lexical diversity does not collapse; and fused signatures remain informative under noise. We also find that structured risk feedback can act as an external alignment signal without fine-tuning, but not as a universal performance enhancer: true audit feedback improves calibration for some models, return and drawdown for others, and reveals cases where hidden or placebo feedback has higher short-horizon return but weaker alignment diagnostics. Finally, a 51-stock intraday experiment reveals a correlation blind spot: LLM rationales often justify concentrated exposure to coupled assets that the risk layer repeatedly clips, with a rolling Markowitz baseline as a covariance reference. These results support a research claim rather than a profitability claim: auditable risk feedback and representation trajectories reveal when LLM financial reasoning is aligning, drifting, or failing.
