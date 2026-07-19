---
interest: medium
link: https://arxiv.org/abs/2607.14434
next_step: skim
priority: low
slack_ts: '1784432004.258089'
source: cs.CR - Cryptography and Security
status: unread
title: A Measurement Study of AI-Environment Realism Gaps in Malware-Analysis Sandboxes
---
# A Measurement Study of AI-Environment Realism Gaps in Malware-Analysis Sandboxes
> 原文: [https://arxiv.org/abs/2607.14434](https://arxiv.org/abs/2607.14434)

arXiv:2607.14434v1 Announce Type: new
Abstract: Sandboxing remains a core technique for observing suspicious program behavior, yet environment-aware malware increasingly suppresses execution when analysis is suspected. Prior generations of sandbox evasion focused on virtualization artifacts, timing discrepancies, and wear-and-tear realism. In this paper, we present the first systematic measurement study of AI-environment artifacts as a new sandbox-evasion surface. We operationalize this realism gap through AIprint, a probe framework that captures persistent artifacts left behind by AI-capable software ecosystems, including AI-assistant configuration directories, model caches, environment variables, local inference services, and package dependencies.
We systematically extract 450 unique artifacts from 284 open-source AI projects on GitHub, compile them into unprivileged Windows probes, and evaluate them across seven commercial and open-source sandbox backends together with three AI-capable reference hosts. Our results show that traditional VM-detection baselines fail to reliably distinguish real AI-capable systems from modern sandboxes, whereas twelve AI-environment artifacts appear on the reference hosts and on none of the evaluated backends. A controlled 214-step installation experiment establishes a causal relationship between AI tool and package installation and measurable AI-environment artifact accumulation, while adaptive spoofing experiments reveal a fundamental operational asymmetry: reproducing convincing AI software environments is substantially more expensive than detecting shallow spoofing.
