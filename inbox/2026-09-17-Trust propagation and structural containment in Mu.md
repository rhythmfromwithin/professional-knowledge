---
interest: medium
link: https://arxiv.org/abs/2609.17648
next_step: skim
priority: low
slack_ts: '1789619684.777459'
source: cs.CR - Cryptography and Security
status: unread
title: Trust propagation and structural containment in Multi-agent LLM pipelines
---
# Trust propagation and structural containment in Multi-agent LLM pipelines
> 原文: [https://arxiv.org/abs/2609.17648](https://arxiv.org/abs/2609.17648)

arXiv:2609.17648v1 Announce Type: new
Abstract: Multi-agent LLM systems increasingly automate tasks involving agents with different levels of privilege, creating a security risk in which a compromised low-privilege agent can influence a higher-privilege agent and trigger an unauthorized action. We study attack propagation in a four-agent LangGraph pipeline comprising a Supervisor, Researcher, Validator, and Executor. We evaluate shared-memory poisoning and indirect prompt injection through a forged approval embedded in a retrieved document. We compare the Validator's judgment with an independent authorization layer using task-bound signed tokens and a separately verified policy oracle. Our contribution is an empirical study of attack propagation, a component-level ablation of the authorization boundary, and the Judgment Bypass Rate (JBR), which measures compromise at the attacked agent rather than at the final action. Across three seeds and 60 labeled tasks, memory poisoning reaches execution in every undefended trial. With authorization enabled, it achieves 100% JBR but 0% Unsafe Action Rate, showing that the Validator can remain compromised while execution is contained. Against an attacker possessing the signing secret, the policy oracle provides the observed containment, while an independently authored least privilege policy preserves this result. An Observer layer reduces the false-positive rate for agent hijacking from 49% to 7% without weakening execution-level security. These results show that structural authorization can contain compromised agent behavior even when upstream LLM judgment fails.
