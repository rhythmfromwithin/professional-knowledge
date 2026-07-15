---
interest: medium
link: https://arxiv.org/abs/2607.08809
next_step: skim
priority: low
slack_ts: '1784085266.231189'
source: cs.CR - Cryptography and Security
status: unread
title: Privacy-Preserving Intent Fulfilment and Assurance for 6G RAN
---
# Privacy-Preserving Intent Fulfilment and Assurance for 6G RAN
> 原文: [https://arxiv.org/abs/2607.08809](https://arxiv.org/abs/2607.08809)

arXiv:2607.08809v1 Announce Type: new
Abstract: Intent-based network management is the emerging paradigm for 6G service lifecycle automation, with the 3GPP intent management framework (TS~28.312) defining creation, translation, fulfilment, and assurance stages. Existing fulfilment and assurance approaches require deep packet inspection, per-flow state tracking, or access to vendor-internal node telemetry to verify that provisioned resources satisfy expressed intents. These requirements conflict with regulatory constraints (GDPR, ePrivacy Directive) in multi-tenant networks and with vendor opacity in multi-vendor O-RAN deployments.
We present an architecture for privacy-preserving intent fulfilment and assurance in which a coordinator provisions resources from declared intent categories without traffic inspection, and verifies fulfilment using only aggregate standardised PM counters at the O1 interface. A data-processing inequality argument shows that the resource allocation reveals at most $\log\_2 K$ bits about traffic content, where $K$ is the number of intent categories. We define two architectural privacy properties, intent-traffic unlinkability and node-opaque verification, and show that both hold by construction. Node-opacity does not sacrifice detection power: the aggregate verifier weakly dominates the per-agent verifier under a homogeneity condition.
We map the architecture to the 3GPP intent lifecycle and the O-RAN Non-RT RIC, identifying the concrete interfaces, data objects, and deployment points at which the mechanism operates. On production PM counter data from four operator networks, increasing intent-category granularity sharpens provisioning but weakens assurance, consistent with the theoretical prediction that the privacy ceiling is a structural side effect of the detection constraint rather than a separate design parameter.
