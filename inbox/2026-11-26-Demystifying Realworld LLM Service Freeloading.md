---
interest: medium
link: https://arxiv.org/abs/2611.33218
next_step: skim
priority: low
slack_ts: '1795850660.680539'
source: cs.CR - Cryptography and Security
status: unread
title: Demystifying Real-world LLM Service Freeloading
---
# Demystifying Real-world LLM Service Freeloading
> 原文: [https://arxiv.org/abs/2611.33218](https://arxiv.org/abs/2611.33218)

arXiv:2611.33218v1 Announce Type: new
Abstract: Third-party projects repackage free inference from LLM web applications and dedicated clients into independent APIs. We refer to such use beyond providers' permitted access, allocation, or redistribution conditions as LLM service freeloading (LSF). However, its scale and underlying mechanisms remain poorly understood. We present a systematic measurement study of 513 open-source projects, tracing 1,588 inference paths across 64 upstream LLM services and characterizing their development, dependencies, and operating mechanisms. We find that 93.0% of repositories were created in 2026. Direct HTTP or WebSocket requests account for 83.2% of paths, making reproduction of product protocols the dominant invocation method. Projects adapt messages, reconstruct conversation state, and convert responses to support compatible APIs. Account selection or rotation appears on 304 paths (19.1%), allowing projects with multiple eligible accounts to distribute requests across their separate allowances. Our policy analysis finds that 58 of the 62 services with available terms explicitly prohibit at least one examined practice, including automated access, account sharing, or service redistribution. These restrictions cover both downstream API provision and the means of obtaining upstream inference. Our findings inform defenses against unauthorized consumption and redistribution of free LLM resources. We have responsibly disclosed our findings to the relevant providers.
