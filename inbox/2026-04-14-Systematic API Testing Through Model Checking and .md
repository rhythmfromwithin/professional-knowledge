---
title: "Systematic API Testing Through Model Checking and Executable Contracts"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.08633
priority: low
status: unread
interest: medium
next_step: skim
---
# Systematic API Testing Through Model Checking and Executable Contracts
> 原文: [https://arxiv.org/abs/2604.08633](https://arxiv.org/abs/2604.08633)

arXiv:2604.08633v1 Announce Type: new
Abstract: Automated black-box testing of APIs typically relies on interface specifications that define available operations and data schemas, but offer limited or no behavioural semantics. This semantic gap amplifies the test-oracle problem and limits the generation of effective, stateful call sequences.
We introduce IcePick, a framework that achieves systematic state-space coverage for API testing by leveraging model checking. IcePick uses TLA+ to formally model API state evolution, employs the TLC model checker to exhaustively explore reachable states, and generates test sequences that provably cover the behavioural model. To mitigate state-space explosion and improve sequence extraction, we introduce a coverage-guided breadth-first traversal of the TLC state-space graph. To address oracle limitations beyond HTTP status codes, we propose Glacier, a first-order logic contract language that enriches API specifications with executable semantic contracts, enabling automated behavioural verification during test execution.
We evaluate IcePick on EvoMaster Benchmark systems, demonstrating that model-checking-guided exploration achieves complete state coverage and reveals faults in multi-operation interactions. We also analyse scalability to characterise practical limits and applicability requirements. Overall, IcePick provides reproducible test suites with strong coverage guarantees for critical API-based systems.
