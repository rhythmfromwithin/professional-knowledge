---
interest: medium
link: https://arxiv.org/abs/2610.12540
next_step: skim
priority: low
slack_ts: '1791952341.209639'
source: cs.CR - Cryptography and Security
status: unread
title: Organizational Context for the Enterprise Security Brain
---
# Organizational Context for the Enterprise Security Brain
> 原文: [https://arxiv.org/abs/2610.12540](https://arxiv.org/abs/2610.12540)

arXiv:2610.12540v1 Announce Type: new
Abstract: Agents that investigate and decide on enterprise security reason over a machine-readable view of the environment: its assets, identities, configurations, relations, and findings. The correct judgment about an asset also depends on what the organization knows about it: who owns it, what business function it serves, which policy governs it, and which risks were accepted. Part of this knowledge can be inferred from machine state, such as an ownership tag; most of it is recorded by people in policies, audit reports, architecture diagrams, tickets, and conversations, outside machine state. We call this distance the organizational context gap. Closing it poses four challenges: extracting the right claims from heterogeneous organizational data and, at inference time, detecting claims made stale by live state, checking live state against the governing policy, and binding architecture diagrams, which carry the business logic, to live resources. We introduce organizational context as a layer of the enterprise security brain and define it with a taxonomy and six properties its representation must preserve. We then define a context model in which a claim carries one meaning, an attestation records each source that asserts it, strength is derived from live evidence at read time, and claims resolve onto the entities of the asset graph. On a production environment spanning AWS, Okta, Google Workspace, and GitHub, extraction recovers 0.80 of a pooled 1,355-claim ground truth at 0.87 precision, with 0.5% of extracted claims unsupported by their source. An agent reasoning over live state and resolved context raises the conflict in 0.97 of stale-finding tasks, and reaches answer correctness of 0.83 on policy-alignment tasks and 0.86 on architecture tasks.
