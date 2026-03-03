---
title: "Mixed Choice in Asynchronous Multiparty Session Types"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2602.23927
priority: medium
status: unread
---
# Mixed Choice in Asynchronous Multiparty Session Types
> 原文: [https://arxiv.org/abs/2602.23927](https://arxiv.org/abs/2602.23927)

arXiv:2602.23927v1 Announce Type: new
Abstract: We present a multiparty session type (MST) framework with asynchronous mixed choice (MC). We propose a core construct for MC that allows transient inconsistencies in protocol state between distributed participants, but ensures all participants can always eventually reach a mutually consistent state. We prove the correctness of our system by establishing a progress property and an operational correspondence between global types and distributed local type projections. Based on our theory, we implement a practical toolchain for specifying and validating asynchronous MST protocols featuring MC, and programming compliant gen\_statem processes in Erlang/OTP. We test our framework by using our toolchain to specify and reimplement part of the amqp\_client of the RabbitMQ broker for Erlang.
