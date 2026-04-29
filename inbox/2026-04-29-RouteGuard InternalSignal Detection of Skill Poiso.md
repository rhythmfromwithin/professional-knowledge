---
title: "RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.22888
priority: low
status: unread
interest: medium
next_step: skim
---
# RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents
> 原文: [https://arxiv.org/abs/2604.22888](https://arxiv.org/abs/2604.22888)

arXiv:2604.22888v1 Announce Type: new
Abstract: Agent skills introduce a new and more severe form of indirect injection for LLM agents: unlike traditional indirect prompt injection, attackers can hide malicious instructions inside a dense, action-oriented skill that already functions as a legitimate instruction source. We study pre-execution skill-poison detection and show that successful skill poisoning induces a structured internal effect, attention hijacking, in which response-time attention shifts from trusted context to malicious skill spans and drives harmful behavior. Motivated by this mechanism, we propose RouteGuard, a frozen-backbone detector that combines response-conditioned attention and hidden-state alignment through reliability-gated late fusion. Across both real and synthetic open-source skill benchmarks, RouteGuard is consistently the strongest or most robust detector; on the critical Skill-Inject channel slice, it reaches 0.8834 F1 and recovers 90.51% of description attacks missed by lexical screening, showing that defending against skill poisoning requires internal-signal detection rather than text-only filtering
