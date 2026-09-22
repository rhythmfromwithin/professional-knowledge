---
interest: medium
link: https://arxiv.org/abs/2609.22525
next_step: skim
priority: low
slack_ts: '1790051359.982829'
source: cs.CR - Cryptography and Security
status: unread
title: 'Tick-Tock on the Open Fronthaul: Securing Synchronization in O-RAN'
---
# Tick-Tock on the Open Fronthaul: Securing Synchronization in O-RAN
> 原文: [https://arxiv.org/abs/2609.22525](https://arxiv.org/abs/2609.22525)

arXiv:2609.22525v1 Announce Type: new
Abstract: The Precision Time Protocol (PTP) provides the time and phase synchronization required by disaggregated Open Radio Access Networks (O-RAN). Yet, in current open fronthaul deployments, PTP traffic lacks mandatory authentication and integrity protection, leaving synchronization vulnerable to spoofing, replay, and delay manipulation attacks that can degrade radio access performance. Existing protections are poorly suited to this setting: they either add excessive latency, do not support multicast dissemination efficiently, or fail to contain key exposure under partially trusted RUs. This paper analyzes the security risks of unprotected O-RAN PTP and develops a threat model for open fronthaul deployments. We then introduce PRTESLA-C, a lightweight synchronization protection mechanism that combines per-round delayed key disclosure with ASCON-based message authentication. PRTESLA-C uses an apply-then-verify-and-correct paradigm: timing samples are applied immediately to preserve real-time control, verified after key disclosure, and removed from persistent synchronization state if authentication fails. This design maintains sub-microsecond synchronization accuracy, provides strong protection against spoofing and replay, and bounds the impact of delay manipulation with minimal computational and latency overhead.
