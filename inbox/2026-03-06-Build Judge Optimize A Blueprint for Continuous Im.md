---
title: "Build, Judge, Optimize: A Blueprint for Continuous Improvement of Multi-Agent Consumer Assistants"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.03565
priority: high
status: unread
---
# Build, Judge, Optimize: A Blueprint for Continuous Improvement of Multi-Agent Consumer Assistants
> 原文: [https://arxiv.org/abs/2603.03565](https://arxiv.org/abs/2603.03565)

arXiv:2603.03565v1 Announce Type: new
Abstract: Conversational shopping assistants (CSAs) represent a compelling application of agentic AI, but moving from prototype to production reveals two underexplored challenges: how to evaluate multi-turn interactions and how to optimize tightly coupled multi-agent systems. Grocery shopping further amplifies these difficulties, as user requests are often underspecified, highly preference-sensitive, and constrained by factors such as budget and inventory. In this paper, we present a practical blueprint for evaluating and optimizing conversational shopping assistants, illustrated through a production-scale AI grocery assistant. We introduce a multi-faceted evaluation rubric that decomposes end-to-end shopping quality into structured dimensions and develop a calibrated LLM-as-judge pipeline aligned with human annotations. Building on this evaluation foundation, we investigate two complementary prompt-optimization strategies based on a SOTA prompt-optimizer called GEPA (Shao et al., 2025): (1) Sub-agent GEPA, which optimizes individual agent nodes against localized rubrics, and (2) MAMuT (Multi-Agent Multi-Turn) GEPA (Herrera et al., 2026), a novel system-level approach that jointly optimizes prompts across agents using multi-turn simulation and trajectory-level scoring. We release rubric templates and evaluation design guidance to support practitioners building production CSAs.
