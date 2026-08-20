---
interest: medium
link: https://arxiv.org/abs/2608.13685
next_step: skim
priority: low
slack_ts: '1787190024.770769'
source: cs.CR - Cryptography and Security
status: unread
title: Weird Machines in Transport Layer Security
---
# Weird Machines in Transport Layer Security
> 原文: [https://arxiv.org/abs/2608.13685](https://arxiv.org/abs/2608.13685)

arXiv:2608.13685v1 Announce Type: new
Abstract: Weird machines are latent computational capabilities that emerge from the composition of architectural components. Prior work has studied this phenomenon extensively in software systems, including x86 instructions, ELF metadata, and page tables, and more recently in cyber-physical systems such as industrial control networks. This paper extends weird machine theory to a new domain: the Transport Layer Security (TLS) handshake and its two dominant implementations, OpenSSL and BoringSSL.
We show that legitimate TLS primitives, including session cache entries, renegotiation logic, extension parsing, and certificate verification steps, compose into Turing-complete systems whose computation is coupled to authentication and trust decisions rather than physical actuation. We formalize this coupling, which we call trust actuation, and argue that any TLS implementation providing session storage, arithmetic on sequence counters, conditional branching on handshake state, and iteration through resumption or retry loops satisfies the conditions for arbitrary computation.
We validate this theory with two working demonstrations built on real OpenSSL code paths. The first, a sentinel system, composes standard TLS primitives into a defensive mechanism that detects anomalous handshake behavior. The second, an authentication bypass, composes the same class of primitives into an attack that defeats a cipher-strength policy check through mid-connection renegotiation, without any memory corruption or external malware. Both demonstrations run against real server and client binaries in Docker.
