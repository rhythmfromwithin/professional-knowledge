---
title: "SecretSifter: A Runtime Secret-Detection Engine for Live Web Traffic"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2611.28168
priority: low
status: unread
interest: medium
next_step: skim
---
# SecretSifter: A Runtime Secret-Detection Engine for Live Web Traffic
> 原文: [https://arxiv.org/abs/2611.28168](https://arxiv.org/abs/2611.28168)

arXiv:2611.28168v1 Announce Type: new
Abstract: Credentials embedded in client-delivered web artifacts, such as minified JavaScript bundles, webpack chunks, server-side-rendered state objects, and JSON or XML API responses, form a runtime attack surface that repository-time (shift-left) secret scanners do not observe, because the credential enters the served artifact at build time or at runtime, after every source-code gate has passed. This paper presents SecretSifter, an open-source runtime secret-detection engine that inspects live web traffic and reports secret-grade credentials at the point they are delivered to the browser. The engine combines format-anchored and context-gated detection rules, semantic key-name extraction, Shannon-entropy scoring, and dedicated detection of hardcoded CryptoJS/AES material across the full served surface. SecretSifter ships as three editions over one shared detection core: a Burp Suite extension, a Chrome extension, and a standalone Windows and macOS desktop application, with a Bearer-authenticated REST and MCP interface for automation. On a 198-value benchmark of real production client-exposed values (GT-198), the deterministic detection stage reached 79.8% recall at 86.8% precision in default configuration, the highest F1 of any system evaluated. The detection core is released under an open-source (MIT) license, and a de-identified reproducibility bundle and a public synthetic demo target are provided.
