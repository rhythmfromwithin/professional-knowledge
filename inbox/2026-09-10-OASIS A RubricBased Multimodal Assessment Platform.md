---
interest: medium
link: https://arxiv.org/abs/2609.09180
next_step: skim
priority: low
slack_ts: '1789013740.401509'
source: cs.SE - Software Engineering
status: unread
title: 'OASIS: A Rubric-Based Multimodal Assessment Platform Using Large Language
  Models'
---
# OASIS: A Rubric-Based Multimodal Assessment Platform Using Large Language Models
> 原文: [https://arxiv.org/abs/2609.09180](https://arxiv.org/abs/2609.09180)

arXiv:2609.09180v1 Announce Type: new
Abstract: OASIS (Open Assessment and Scoring Infrastructure Stack) is a systems platform for rubric-based grading of video, audio, and text with large language models. Scoring one artifact with an LLM is straightforward; deploying assessment at scale requires encounter management, rubric versioning, modality-aware execution, provenance capture, and human review. OASIS pairs a standalone command-line interface with a canonical integrated Elephant + MAPLES stack for encounter management and multimodal grading orchestration. Both paths can target hosted APIs or self-hosted open-weight models through Ollama and OpenAI-compatible endpoints such as vLLM. SimRubrics rubric authoring and the Wayfinder conversational agent gateway are optional extensions that use the same authenticated interfaces as human operators. Given a rubric and recorded encounters, OASIS produces per-criterion scores, evidence, and rationales, preserving execution artifacts for audit. Distinctive features include rubric-as-program compilation, progressive execution plans, content-addressable grading identity, transcript-augmented multimodal grading, explicit review state, and a shared command surface for humans and autonomous agents. Though developed in medical education, the architecture is domain-agnostic, applying wherever structured performance can be evaluated from recorded or written artifacts. In production at UT Southwestern Medical Center since Fall 2023, the platform has processed more than 7,000 encounters. This publication includes the report and project information, not application source, binaries, installation materials, sample data, or a tagged software release.
