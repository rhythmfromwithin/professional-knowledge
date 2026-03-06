---
title: "Bisynchronous FIFOs and the FITO Category Mistake: Silicon-Proven Interaction Primitives for Distributed Coordination"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.03470
priority: medium
status: unread
---
# Bisynchronous FIFOs and the FITO Category Mistake: Silicon-Proven Interaction Primitives for Distributed Coordination
> 原文: [https://arxiv.org/abs/2603.03470](https://arxiv.org/abs/2603.03470)

arXiv:2603.03470v1 Announce Type: new
Abstract: Bisynchronous FIFOs -- hardware buffers that mediate data transfer between independent clock domains without a shared global timebase -- have been designed, formally verified, and commercially deployed in silicon for over four decades. We survey this literature from Chapiro's 1984 GALS thesis through Cummings's Gray-code pointer techniques, Chelcea and Nowick's mixed-timing interfaces, Greenstreet's STARI protocol, and the 2015 NVIDIA pausible bisynchronous FIFO, and argue that this body of work constitutes a silicon-proven existence proof against the Forward-In-Time-Only (FITO) assumption that pervades distributed systems. The central claim is that interaction-based synchronization primitives -- handshakes, mutual exclusion, and causal flow control -- can replace timestamp-based coordination at the most demanding levels of digital engineering, directly undermining the FITO assumption in protocols such as PTP, TSN, and conventional Ethernet. We draw a structural parallel between on-chip bisynchronous coordination and the Open Atomic Ethernet (OAE) architecture, and identify the handshake -- not the timestamp -- as the fundamental primitive for coordination between independent causal domains.
