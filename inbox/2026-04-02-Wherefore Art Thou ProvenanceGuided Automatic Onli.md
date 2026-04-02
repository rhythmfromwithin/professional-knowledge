---
title: "Wherefore Art Thou? Provenance-Guided Automatic Online Debugging with Lumos"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.29013
priority: low
status: unread
interest: medium
next_step: skim
---
# Wherefore Art Thou? Provenance-Guided Automatic Online Debugging with Lumos
> 原文: [https://arxiv.org/abs/2603.29013](https://arxiv.org/abs/2603.29013)

arXiv:2603.29013v1 Announce Type: new
Abstract: Debugging distributed systems in-production is inevitable and hard. Myriad interactions between concurrent components in modern, complex and large-scale systems cause non-deterministic bugs that offline testing and verification fail to capture. When bugs surface at runtime, their root causes may be far removed from their symptoms. To identify a root cause, developers often need evidence scattered across multiple components and traces. Unfortunately, existing tools fail to quickly and automatically record useful provenance information at low overheads, leaving developers to manually perform the onerous evidence collection task. Lumos is an online debugging framework that exposes application-level bug provenances--the computational history linking symptoms of an incident to their root causes. Lumos leverages dependency-guided instrumentation powered by static analysis to identify program state related to a bug's provenance, and exposes them via lightweight on-demand recording. Lumos provides developers with enough evidence to identify a bug's root cause, while incurring low runtime overhead, and given only a few occurrences of a bug.
