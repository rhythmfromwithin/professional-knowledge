---
interest: medium
link: https://arxiv.org/abs/2606.30783
next_step: skim
priority: low
slack_ts: '1782880937.360399'
source: cs.CR - Cryptography and Security
status: unread
title: 'Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense'
---
# Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense
> 原文: [https://arxiv.org/abs/2606.30783](https://arxiv.org/abs/2606.30783)

arXiv:2606.30783v1 Announce Type: new
Abstract: We identify a security-fidelity tradeoff in defending LLMs against indirect prompt injection: defenses resist injected instructions largely by suppressing untrusted text, which corrupts tasks that must preserve it, such as translation and document editing. Attack-success metrics cannot see this, because a model that ignores an injection and one that faithfully processes it as data score identically. We introduce SecFid, a benchmark built so that executing an injection, processing it as data, and ignoring it produce distinguishable outputs. This makes fidelity measurable and exposes a frontier: across 1,168 examples and 48 configurations, no model or defense achieves both objectives. The highest-fidelity model reaches 96.5% fidelity at 47.8% security, while the most secure defenses invert this, at 99.3% security but only 71.0%-73.9% fidelity. Even defenses with identical security differ in how they earn it: some repair hijacks into faithful processing, others simply suppress benign content. A decision-theoretic analysis shows why no fixed choice can be right everywhere: the correct behavior is not a property of the defense but of the deployment, set by its relative cost of a hijack versus a dropped span. Security alone therefore measures only half of robustness, and reporting it without fidelity hides the price at which it was bought.
