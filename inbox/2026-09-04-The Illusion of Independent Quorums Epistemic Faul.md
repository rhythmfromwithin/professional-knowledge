---
interest: medium
link: https://arxiv.org/abs/2609.02925
next_step: skim
priority: medium
slack_ts: '1788667879.711419'
source: cs.DC - Distributed Computing
status: unread
title: 'The Illusion of Independent Quorums: Epistemic Fault Domains and Correlated
  Cognitive Failures in Agentic Quorums'
---
# The Illusion of Independent Quorums: Epistemic Fault Domains and Correlated Cognitive Failures in Agentic Quorums
> 原文: [https://arxiv.org/abs/2609.02925](https://arxiv.org/abs/2609.02925)

arXiv:2609.02925v1 Announce Type: new
Abstract: Multi-agent quorums are widely used to authorize high-stakes infrastructure and policy mutations, yet distinct reviewers often share upstream telemetry, documents, or tool backends. When upstream inputs fail, multiple votes collapse onto a single corrupted cause: replication does not imply epistemic redundancy. We introduce Epistemic Fault Domains (EFDs) and the Structural Epistemic Cut \kappa\_E, which quantifies the minimum number of modeled root faults whose exposure covers an authorizing coalition relative to an explicit Epistemic Fault Basis. Under closed causal accounting, conservative exposure, and authorization alignment, \kappa\_E lower-bounds the number of roots required for semantic compromise (\kappa\_S). We prove that arbitrarily large quorums can retain \kappa\_E=1, that recognizing shared ancestry never increases credited resilience, and that adding voters at a fixed threshold cannot increase the cut under compatible exposure extensions. Finally, we design the Dependency-Aware Quorum Controller (DAQC) to enforce structural cuts at runtime admission, evaluate its mechanics via analytical derivations and simulations, and provide a frozen 120-task external benchmark suite.
