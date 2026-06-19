---
slack_ts: '1781847256.737719'
---
# AgentArmor: A Framework, Evaluation, \& Mitigation of Coding Agent Failures
> 原文: [https://arxiv.org/abs/2606.19380](https://arxiv.org/abs/2606.19380)

arXiv:2606.19380v1 Announce Type: new
Abstract: Software engineering and deployment are increasingly being delegated to AI coding agents. The scale of their adoption is surfacing rare, but highly destructive, failure modes. In this paper, we study these failure modes as stemming from three distinct mechanisms: underspecification, where default model behavior is unsafe; capability errors, where the safe action is available but the model does not adhere to it due to bias or capability limitations; and agent harness errors, where the model fails to execute the safe action through the harness. We evaluate these across 8 different evaluations, each inspired by real-life deployment failures, totaling 20 coding environments and 59 synthetic transcript templates. Based on this evaluation, we propose AgentArmor, an agent harness modification, to mitigate these errors. By adding an extended system prompt, a separate command classifier, a ``3 strikes'' policy, deterministic guardrails, and tools for the agent to edit its own context, we show that AgentArmor is safer across a statistically significant number of samples. Thus, we suggest concrete mitigations for current coding agents and a design philosophy for future agent harness features.
