---
interest: medium
link: https://arxiv.org/abs/2608.17043
next_step: skim
priority: low
slack_ts: '1787190048.364409'
source: cs.CR - Cryptography and Security
status: unread
title: 'Remote-Timer-as-a-Service: Efficient Microarchitectural Leakage in the Cloud
  with Remote Timers'
---
# Remote-Timer-as-a-Service: Efficient Microarchitectural Leakage in the Cloud with Remote Timers
> 原文: [https://arxiv.org/abs/2608.17043](https://arxiv.org/abs/2608.17043)

arXiv:2608.17043v1 Announce Type: new
Abstract: Edge computing solutions have become a crucial part of the industry, delivering fast, flexible and scalable applications close to the end users, with typical use cases including dynamic content creation, image resizing and chatbots. Cloudflare Workers is one such framework, which handles millions of HTTP requests per second worldwide. To reduce start-up latency, Cloudflare Workers removes process-isolation boundaries between multiple tenants and leverages language-level isolation. This architecture poses the risk of Spectre attacks. To mitigate these, Cloudflare Workers previously introduced several countermeasures such as restricted timer measurements, no shared memory, no multithreading and Dynamic Process Isolation (DyPrIs), detecting potential attacks and process-isolating potentially malicious scripts.
We demonstrate that the production implementation of DyPrIs was insufficient. We adopt microarchitectural amplification techniques and discover various possibilities to measure time in the production environment of Cloudflare Workers. Given these techniques, we show that freezing and coarsening timers in the Cloudflare Workers security model is insufficient. Leveraging both timing amplification and remote timers, we demonstrate a remote Spectre attack that leaks a JWT token from a co-located victim worker in the Cloudflare Workers production environment. We outperform the existing attack by orders of magnitude, going from 2 bit/min to up to 12 bit/s at an accuracy of 99.16%, posing an immediate risk to customer data. Following our end-to-end attack, Cloudflare Workers mitigated it in a coordinated effort by integrating the V8 Sandbox limiting transient access to 64-bit pointers, improving the detection capabilities of DyPrIs, and deploying hardware-assisted MPK-based in-process isolation to confine each tenant heap under a dedicated memory-protection key.
