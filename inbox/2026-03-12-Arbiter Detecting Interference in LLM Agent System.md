---
title: "Arbiter: Detecting Interference in LLM Agent System Prompts"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.08993
priority: low
status: unread
interest: medium
next_step: skim
---
# Arbiter: Detecting Interference in LLM Agent System Prompts
> 原文: [https://arxiv.org/abs/2603.08993](https://arxiv.org/abs/2603.08993)

arXiv:2603.08993v1 Announce Type: new
Abstract: System prompts for LLM-based coding agents are software artifacts that govern agent behavior, yet lack the testing infrastructure applied to conventional software. We present Arbiter, a framework combining formal evaluation rules with multi-model LLM scouring to detect interference patterns in system prompts. Applied to three major coding agent system prompts: Claude Code (Anthropic), Codex CLI (OpenAI), and Gemini CLI (Google), we identify 152 findings across the undirected scouring phase and 21 hand-labeled interference patterns in directed analysis of one vendor. We show that prompt architecture (monolithic, flat, modular) strongly correlates with observed failure class but not with severity, and that multi-model evaluation discovers categorically different vulnerability classes than single-model analysis. One scourer finding was structural data loss in Gemini CLI's memory system was consistent with an issue filed and patched by Google, which addressed the symptom without addressing the schema-level root cause identified by the scourer. Total cost of cross-vendor analysis: \$0.27 USD.
