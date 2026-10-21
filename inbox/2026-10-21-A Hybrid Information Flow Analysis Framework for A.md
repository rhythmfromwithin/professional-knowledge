---
title: "A Hybrid Information Flow Analysis Framework for Android Hybrid Apps"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.27288
priority: low
status: unread
interest: medium
next_step: skim
---
# A Hybrid Information Flow Analysis Framework for Android Hybrid Apps
> 原文: [https://arxiv.org/abs/2610.27288](https://arxiv.org/abs/2610.27288)

arXiv:2610.27288v1 Announce Type: new
Abstract: The WebView interface in Android (hybrid) applications enables the native side (e.g., Java) to exchange data with the Web (e.g., JavaScript). This creates cross-language information flow channels that existing single-language analyzers cannot analyze. Existing hybrid app analyses address only part of the problem: some build bridge-aware call graphs but provide limited information-flow analysis, some rely on coarse assumptions, and some focus only on web vulnerabilities. We present MifDroid, a static-analysis- guided dynamic-analysis framework with a lifecycle-aware per-WebView call graph, a bridge-aware type-and-effect system, and a modular JavaScript analysis engine. We evaluated MifDroid on 338 apps from the F-Droid repository (out of 4,126 total) that use addJavascriptInterface, enabling active communication between Java and JavaScript. Our guided dynamic phase adds 662 entries to the 444 produced by static analysis, raising the resolution rate from 36.5% to 74.5%, produces the resolved bridge-related entries for 115 apps that static analysis leaves empty. MifDroid reported 14 vulnerable cross-language information flows, five of which have been accepted and fixed by the maintainers.
