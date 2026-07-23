---
interest: medium
link: https://arxiv.org/abs/2607.18347
next_step: skim
priority: low
slack_ts: '1784777496.004709'
source: cs.SE - Software Engineering
status: unread
title: A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce
---
# A Decision-Centered Reference Architecture for Trustworthy Agentic Commerce
> 原文: [https://arxiv.org/abs/2607.18347](https://arxiv.org/abs/2607.18347)

arXiv:2607.18347v1 Announce Type: new
Abstract: Agentic commerce extends agentic shopping into software agents that interpret policy, prepare checkout, generate transaction-facing language, and act under delegated payment authority. Protocols standardize external exchanges, but merchants still need one authoritative representation of commercial eligibility, actor authority, checkout validity, payment dispatch, generated claims, and evidence. This design-science study presents a protocol-agnostic architecture built around a canonical envelope, protected dependency and result hashes, Ed25519 or HMAC authentication, live-request rebinding, a seven-axis generated-claim gate, execution-time dependency revalidation, and eleven semantic invariants. Evaluation used an open-source JavaScript implementation, eight deterministic ecommerce scenarios, and five controlled ablations. Seven initially valid actions were permitted. After protected state changed, none could proceed without a fresh decision; a hostile-accessor case also remained blocked. Action status was consistent across configured surface-bound envelopes, and each scenario contained the three protected hashes and its targeted dependency reference. Each ablation produced the predicted unsafe regression when one safeguard was bypassed, while the protected path contained the same failure. The hostile accessor was read once, and the suite passed 66/66 tests, schema validation, and committed examples. Results support protected-dependency change detection, bounded outcome derivation, stale-decision prevention, surface-bound status consistency, refusal propagation, and verified-state identity under synthetic fixtures, but do not establish rule completeness, production security, performance, legal compliance, live interoperability, population error rates, or independent replication.
