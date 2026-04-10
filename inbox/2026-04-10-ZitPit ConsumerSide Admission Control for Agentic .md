---
interest: medium
link: https://arxiv.org/abs/2604.06241
next_step: skim
priority: low
slack_ts: '1775791758.861629'
source: cs.CR - Cryptography and Security
status: unread
title: 'ZitPit: Consumer-Side Admission Control for Agentic Software Intake'
---
# ZitPit: Consumer-Side Admission Control for Agentic Software Intake
> 原文: [https://arxiv.org/abs/2604.06241](https://arxiv.org/abs/2604.06241)

arXiv:2604.06241v1 Announce Type: new
Abstract: AI IDEs and coding agents compress discovery, fetch, workspace open, installation, and execution into one low-observability loop. Existing defenses such as provenance frameworks, package and repository firewalls, runtime protection, and tool-approval prompts each cover part of that path, but they often leave the final consumer-side execution decision implicit. ZitPit is a 100% open-source Rust system that argues for a stricter boundary: first-seen external artifacts should become durable policy events before they gain execution rights on protected developer or CI hosts. The current public evidence is intentionally narrow and explicit. It includes repeated Git smart-HTTP intake measurements showing that approved artifacts can remain faster than unmanaged public fetch, plus implemented protected-session and governed-egress proof families. The broader contribution is architectural rather than universal-coverage-by-assertion: ZitPit unifies artifact admission, repo-open state, capability-scoped execution, and durable policy records at the consumer execution boundary for agentic workflows.
