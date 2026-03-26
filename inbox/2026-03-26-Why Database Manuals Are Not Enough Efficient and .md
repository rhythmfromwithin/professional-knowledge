---
title: "Why Database Manuals Are Not Enough: Efficient and Reliable Configuration Tuning for DBMSs via Code-Driven LLM Agents"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.22708
priority: low
status: unread
interest: medium
next_step: skim
---
# Why Database Manuals Are Not Enough: Efficient and Reliable Configuration Tuning for DBMSs via Code-Driven LLM Agents
> 原文: [https://arxiv.org/abs/2603.22708](https://arxiv.org/abs/2603.22708)

arXiv:2603.22708v1 Announce Type: new
Abstract: Modern database management systems (DBMSs) expose hundreds of configuration knobs that critically influence performance. Existing automated tuning methods either adopt a data-driven paradigm, which incurs substantial overhead, or rely on manual-driven heuristics extracted from database documentation, which are often limited and overly generic. Motivated by the fact that the control logic of configuration knobs is inherently encoded in the DBMS source code, we argue that promising tuning strategies can be mined directly from the code, uncovering fine-grained insights grounded in system internals. To this end, we propose SysInsight, a code-driven database tuning system that automatically extracts fine-grained tuning knowledge from DBMS source code to accelerate and stabilize the tuning process. SysInsight combines static code analysis with LLM-based reasoning to identify knob-controlled execution paths and extract semantic tuning insights. These insights are then transformed into quantitative and verifiable tuning rules via association rule mining grounded in tuning observations. During online tuning, system diagnosis is applied to identify critical knobs, which are adjusted under the rule guidance. Evaluations demonstrate that compared to the SOTA baseline, SysInsight converges to the best configuration on average 7.11X faster while achieving a 19.9% performance improvement.
