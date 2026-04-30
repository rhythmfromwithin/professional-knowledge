---
interest: medium
link: https://arxiv.org/abs/2604.24790
next_step: skim
priority: low
slack_ts: '1777521064.254459'
source: cs.CR - Cryptography and Security
status: unread
title: Semantic Denial of Service in LLM-controlled robots
---
# Semantic Denial of Service in LLM-controlled robots
> 原文: [https://arxiv.org/abs/2604.24790](https://arxiv.org/abs/2604.24790)

arXiv:2604.24790v1 Announce Type: new
Abstract: Safety-oriented instruction-following is supposed to keep LLM-controlled robots safe. We show it also creates an availability attack surface. By injecting short safety-plausible phrases (1-5 tokens) into a robots audio channel, an adversary can trigger the models safety reasoning to halt or disrupt execution without jailbreaking the model or overriding its policy. In the embodied setting, this is a semantic denial-of-service attack: the agent stops because the injected signal looks like a legitimate alert. Across four vision-language models, seven prompt-level defenses, three deployment modes, and single- and multi-injection settings, we find that prompt-only defenses trade off attack suppression against genuine hazard response. The strongest defenses reduce hard-stop attack success on some models, but defenses change the form of disruption, not its fact: suppressed hard stops re-emerge as acknowledge loops and false alerts, which we measure with Disruption Success Rate (DSR). We further find that injection variety is consistently more effective than repeating the same phrase, suggesting that models treat diverse safety cues as corroborating evidence. The practical implication is architectural rather than prompt-level: systems that route unauthenticated audio text directly into the LLM create an avoidable security dependency between safety monitoring and action selection.
