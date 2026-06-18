---
title: "ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2606.18467
priority: medium
status: unread
interest: medium
next_step: skim
---
# ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift
> 原文: [https://arxiv.org/abs/2606.18467](https://arxiv.org/abs/2606.18467)

arXiv:2606.18467v1 Announce Type: new
Abstract: Modern AI agents retrieve documents, call tools, check intermediate information, and then produce a final answer or action. This creates a risk-control problem that is not visible from the final answer alone. A final response may look acceptable even when the retrieval was weak, a tool output was wrong, or an earlier step was unsupported. We propose ToolChain-CRC, a conformal risk-control method for retrieval-augmented and tool-using agents under drift. The method treats each agent run as a full trajectory of actions, observations, and final output. It builds step-level risk scores, combines them into a trajectory risk score, calibrates an accept-or-intervene rule, and adds an anytime alarm that can stop risky runs before the final answer. We prove trajectory-level risk control under exchangeable calibration runs, give a drift-aware extension with auditable constants, and prove an anytime escalation rule through a supermartingale construction. Experiments cover synthetic tool-chain drift, RAG/tool-use stress tests, public SQuAD-derived retrieval tasks, an API-free agentic QA case study, ablations, target-risk sensitivity checks, 20-seed robustness checks, a drift-margin audit, and a live RAG/tool-use agent benchmark. Across these settings, final-answer-only calibration can miss retrieval and tool failures, while trajectory-level calibration keeps accepted-trajectory risk below the target.
