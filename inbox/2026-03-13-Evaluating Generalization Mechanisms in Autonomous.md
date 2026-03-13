---
interest: medium
link: https://arxiv.org/abs/2603.10041
next_step: skim
priority: low
slack_ts: '1773369880.447779'
source: cs.CR - Cryptography and Security
status: unread
title: Evaluating Generalization Mechanisms in Autonomous Cyber Attack Agents
---
# Evaluating Generalization Mechanisms in Autonomous Cyber Attack Agents
> 原文: [https://arxiv.org/abs/2603.10041](https://arxiv.org/abs/2603.10041)

arXiv:2603.10041v1 Announce Type: new
Abstract: Autonomous offensive agents often fail to transfer beyond the networks on which they are trained. We isolate a minimal but fundamental shift -- unseen host/subnet IP reassignment in an otherwise fixed enterprise scenario -- and evaluate attacker generalization in the NetSecGame environment. Agents are trained on five IP-range variants and tested on a sixth unseen variant; only the meta-learning agent may adapt at test time. We compare three agent families (traditional RL, adaptation agents, and LLM-based agents) and use action-distribution-based behavioral/XAI analyses to localize failure modes. Some adaptation methods show partial transfer but significant degradation under unseen reassignment, indicating that even address-space changes can break long-horizon attack policies. Under our evaluation protocol and agent-specific assumptions, prompt-driven pretrained LLM agents achieve the highest success on the held-out reassignment, but at the cost of increased inference-time compute, reduced transparency, and practical failure modes such as repetition/invalid-action loops.
