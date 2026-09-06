---
interest: medium
link: https://arxiv.org/abs/2609.02889
next_step: skim
priority: high
slack_ts: '1788667880.466459'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting
  Trap in Self-Evolving LLM Agents
---
# Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents
> 原文: [https://arxiv.org/abs/2609.02889](https://arxiv.org/abs/2609.02889)

arXiv:2609.02889v1 Announce Type: new
Abstract: A growing body of work improves frozen large language models (LLMs) as agents by evolving their harness: the textual scaffolding around the model, including persona, strategy, format rules, and control heuristics. Existing reflective prompt-evolution methods usually optimize this harness as one flat string. We instead ask where the optimization value actually resides. We introduce HARNESSEVO, which decomposes the harness into four separately evolvable slots: role, task-strategy, tool/format-rules, and reflection/control. Using the same reflective optimizer under an iso-budget setting, we pair this decomposition with leave-one-in and leave-one-out attribution to measure the contribution of each slot.
On ALFWorld with a frozen 7B backbone, HARNESSEVO does not significantly improve the overall binary success rate over either the stock harness or flat-string evolution: 0.657 versus 0.642 and 0.642, respectively. However, the slot-level analysis reveals that nearly all useful optimization value is localized in the reflection/control slot, which achieves a leave-one-in gain of +0.119. The other slots are individually null. We further show that uniform budget splitting is harmful: allocating 64 rollouts across four slots leaves only 16 per slot, below the optimizer's effective search floor, causing every slot to freeze at its empty seed. Concentrating the budget on the high-credit control slot recovers the lost gain, reaching 0.761 with half the split budget.
The effect is task-contingent. On WebShop, all slots freeze empty and all methods tie, indicating a genuine absence of recurrent, verbalizable control failures rather than budget starvation. Overall, our results suggest that harness value is localized, uniform budget splitting can be actively harmful, and credit assignment should precede structured agent-evolution.
