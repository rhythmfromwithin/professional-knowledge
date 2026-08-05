---
title: "Machine-Checked Dual-Write Recovery from a Committed Log"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.00501
priority: low
status: unread
interest: medium
next_step: skim
---
# Machine-Checked Dual-Write Recovery from a Committed Log
> 原文: [https://arxiv.org/abs/2608.00501](https://arxiv.org/abs/2608.00501)

arXiv:2608.00501v2 Announce Type: new
Abstract: After a crash, a delivery process faces a question its own database cannot answer: did the other side already receive the effect? Transactional outboxes and change data capture remove the application's dual write, but the relay they introduce delivers and records its own progress as two separate durable acts, so the same decision reappears one stage later.
Practitioners have handled this boundary for a decade with retries, checkpoints, idempotency keys, and fencing, and the operational advice is largely sound. What has been missing is a precise account of when it works: the exact event the guarantees refer to, the evidence they require, and how long that evidence lasts. This paper supplies the missing account as a machine-checked theory, developed in Isabelle/HOL.
At its heart is an information bound. Two reachable post-crash states can agree on everything the crashed side durably knows and still differ in what the sink accepted, so any recovery decision computed from that side must duplicate a delivery or leave one owed. This is not a story about sloppy bookkeeping. Even a single deterministic deliver-then-checkpoint protocol that consults its own durable cursor on restart is defeated by crash timing alone. Reading the sink's accepted record escapes the bound exactly, under stated premises. That answer can still become stale if an earlier request remains in flight or another recoverer acts on the same crash. Each hazard has its own proved fence at the sink's acceptance boundary, and the cost of fencing is itself a theorem. Finally, the guarantee has a lifetime: bounded deduplication memory and truncated source history each void it in a proved way. The resulting test for any exactly-once recovery claim is short: what did the sink accept, what can still change that answer, and how long will the evidence survive?
