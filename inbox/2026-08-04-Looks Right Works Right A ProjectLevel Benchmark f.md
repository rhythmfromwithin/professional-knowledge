---
title: "Looks Right, Works Right: A Project-Level Benchmark for Multi-Screen Mobile App Generation"
source: "cs.HC - Human-Computer Interaction"
link: https://arxiv.org/abs/2607.28645
priority: low
status: unread
interest: medium
next_step: skim
---
# Looks Right, Works Right: A Project-Level Benchmark for Multi-Screen Mobile App Generation
> 原文: [https://arxiv.org/abs/2607.28645](https://arxiv.org/abs/2607.28645)

arXiv:2607.28645v1 Announce Type: new
Abstract: Recent multimodal large language models can convert visual designs directly into executable code, but real mobile products require multiple screenshots to become a buildable codebase with shared components and working navigation. This project-level setting exposes three limits of existing design-to-code benchmarks: they focus on single-page generation rather than complete codebases, cannot evaluate cross-page navigation, and do not measure project-wide maintainability. We introduce MobileForge, the first benchmark for project-level multi-screen mobile app generation, comprising
real mobile apps,
human-reviewed screens, structured page-relationship annotations, and
navigation test specifications. MobileForge supports five-axis evaluation of build, navigation, visual fidelity, code maintainability, and efficiency. We also propose state-isolated navigation testing to avoid cascading failures in navigation evaluation and an anchor-referenced list-wise visual evaluation protocol to improve visual-judge reliability. Across
end-to-end runs on six frontier multimodal LLMs, current models can build mobile-app projects that compile and reach the correct pages, but interactive navigation remains unreliable and visual fidelity and maintainability still lag. The benchmark and supporting materials are available at https://github.com/anoa12159-hue/mobileforge\_eval.
