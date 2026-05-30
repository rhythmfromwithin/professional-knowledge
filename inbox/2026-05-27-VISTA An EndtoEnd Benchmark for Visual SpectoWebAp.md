---
interest: medium
link: https://arxiv.org/abs/2605.26144
next_step: skim
priority: low
slack_ts: '1780113869.424119'
source: cs.SE - Software Engineering
status: unread
title: 'VISTA: An End-to-End Benchmark for Visual Spec-to-Web-App Coding Agents'
---
# VISTA: An End-to-End Benchmark for Visual Spec-to-Web-App Coding Agents
> 原文: [https://arxiv.org/abs/2605.26144](https://arxiv.org/abs/2605.26144)

arXiv:2605.26144v1 Announce Type: new
Abstract: We present VISTA (VIsual Spec-To-App Benchmark), a benchmark for evaluating the end-to-end web-app generation capabilities of LLM-based agents. Unlike prior code generation benchmarks that focus on algorithmic tasks, VISTA targets realistic UI-centric development, where agents must produce functional, visually coherent applications from underspecified inputs. We define five prompt-information conditions that vary along two axes, visual/structural fidelity and stack constraint: (1) text only with free stack choice, (2) text with reference screenshots under three specified stacks, (3) text with reference screenshots under free stack choice, (4) text with screenshots and pruned Figma structure under a single specified stack, and (5) text with screenshots and pruned Figma structure under free stack choice. To enable robust evaluation, each page in the benchmark is manually annotated with interactive UI components and around three visual anchor points, addressing the well-known limitations of script-based testing tools such as Playwright in open-ended code generation settings. Evaluation combines DOM-grounded reference matching, behavior-specific browser tests, and CLIP-based visual similarity, jointly measuring structural alignment, behavioral completeness, and overall visual fidelity. We use VISTA to assess four agent systems drawn from two model families and two harnesses, finding that visual fidelity and functional correctness are partially decoupled across both input conditions and agents, and that agent editing style varies sharply but is largely orthogonal to task quality. VISTA establishes a rigorous and reproducible foundation for advancing agent-based software engineering research.
