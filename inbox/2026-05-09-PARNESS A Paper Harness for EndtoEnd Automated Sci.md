---
interest: medium
link: https://arxiv.org/abs/2605.05258
next_step: skim
priority: low
slack_ts: '1778385553.842569'
source: cs.SE - Software Engineering
status: unread
title: 'PARNESS: A Paper Harness for End-to-End Automated Scientific Research with
  Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation'
---
# PARNESS: A Paper Harness for End-to-End Automated Scientific Research with Dynamic Workflows, Full-Text Indexing, and Cross-Run Knowledge Accumulation
> 原文: [https://arxiv.org/abs/2605.05258](https://arxiv.org/abs/2605.05258)

arXiv:2605.05258v1 Announce Type: new
Abstract: Recent autonomous research systems -- AI-Scientist, PaperOrchestra, AutoSOTA, DeepResearch, InternAgent, ResearchAgent and others -- show LLM agents can ideate, run experiments and write papers, but each fixes a particular control-flow shape (linear pipeline, state machine, single-agent loop, or fixed-recipe skill pack) at the framework level. We argue this rigidity has five roots: (1) workflows are dynamic and discipline-specific (lab work, surveys, simulations, theory all loop differently); (2) ideation is bounded by LLM context and cross-domain ideation needs knowledge a single context cannot hold; (3) summary-only views miss the paper body, yet full-text access is uneven, so the cumulative corpus must do the work; (4) a paper's open-source repository is often the only complete specification of its experimental scheme, but the paper-to-code link is neglected; (5) no tool persists cross-run knowledge retrievably into a finite LLM context.
We present PARNESS, an open-source framework built on four design moves. (i) A thin DAG kernel with a four-field Agent contract decouples scheduling from domain semantics, so any discipline's loop is expressible as user-editable YAML. (ii) A full-text PDF-parsing and literature-library subsystem indexes paper bodies, figures and tables as typed objects, with graceful abstract-only fall-back. (iii) A knowledge-graph index over papers, ideas, experiments and code repositories, with scenario-typed retrieval (similar / contradictory / cross-domain / counter-intuitive), surfaces a focused slice into each LLM call. (iv) A small extension surface lets any modern coding agent (Claude Code, Cursor, Copilot, OpenCode) add or replace any module. To our knowledge PARNESS is the first open-source system combining declarative pipelines, full-PDF and code-repository indexing, and cross-run knowledge. Source: https://github.com/gtrhythm/PARNESS
