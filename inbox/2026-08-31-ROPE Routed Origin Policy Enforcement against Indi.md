---
interest: medium
link: https://arxiv.org/abs/2608.27496
next_step: skim
priority: low
slack_ts: '1788152851.899769'
source: cs.CR - Cryptography and Security
status: unread
title: 'ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection'
---
# ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection
> 原文: [https://arxiv.org/abs/2608.27496](https://arxiv.org/abs/2608.27496)

arXiv:2608.27496v1 Announce Type: new
Abstract: Indirect prompt injection (IPI) plants instructions in the content a tool-using LLM agent reads, steering the agent into harmful tool calls. The strongest defenses are system-level, leveraging techniques such as task-conditional tool screening to prevent execution of malicious tools, and information-flow control to avoid tool execution with untrusted parameters. However, as agents grow more capable, users delegate more to automation. Consequently, tool execution sequences and parameter values are increasingly determined at runtime and cannot be reliably screened from solely user's query without significant utility loss. We present ROPE (Routed Origin Policy Enforcement), which is anchored in a structural notion of trust: a value may reach a state-changing tool only if it traces unforgeably to the user, a source the user explicitly named, or the user's own authoritative records. Enforcement is then a deterministic origin check over an audited set of sensitive tool parameters, and the only reliance on a language model involves solely the trusted user request, out of the attacker's reach. Our approach admits two provable guarantees: 1) at every step of a trajectory, no value whose only origin is attacker-writable content reaches an origin-guarded parameter, and 2) no rewording of an injection changes an admission decision. We evaluate across four agent models on open-ended agent suites, ROPE holds attack success rate to 1.6--2.6\% while retaining 82--100\% of undefended clean utility, significantly exceeding state-of-the-art system-level defenses in utility while attaining comparable or better security. Further, we show that optimizing the injection against ROPE is largely ineffective, while long-horizon attacks that defeat prior system-level defenses achieve zero success rate. Our code and logs are available at https://github.com/xhOwenMa/ROPE .
