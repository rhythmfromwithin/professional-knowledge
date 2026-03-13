---
interest: medium
link: https://arxiv.org/abs/2603.08729
next_step: skim
priority: medium
slack_ts: '1773369875.545779'
source: cs.CY - Computers and Society
status: unread
title: 'Self-hosted Lecture-to-Quiz: Local LLM MCQ Generation with Deterministic Quality
  Control'
---
# Self-hosted Lecture-to-Quiz: Local LLM MCQ Generation with Deterministic Quality Control
> 原文: [https://arxiv.org/abs/2603.08729](https://arxiv.org/abs/2603.08729)

arXiv:2603.08729v1 Announce Type: new
Abstract: We present an end-to-end self-hosted (API-free) pipeline, where API-free means that lecture content is not sent to any external LLM service, that converts lecture PDFs into multiple-choice questions (MCQs) using a local LLM plus deterministic quality control (QC). The pipeline is designed for black-box minimization: LLMs may assist drafting, but the final released artifacts are plain-text question banks with an explicit QC trace and without any need to call an LLM at deployment time. We run a seed sweep on three short "dummy lectures" (information theory, thermodynamics, and statistical mechanics), collecting 15 runs x 8 questions = 120 accepted candidates (122 attempts total under bounded retries). All 120 accepted candidates satisfy hard QC checks (JSON schema conformance, a single marked correct option, and numeric/constant equivalence tests); however, the warning layer flags 8/120 items (spanning 8 runs) that expose residual quality risks such as duplicated distractors or missing rounding instructions. We report a warning taxonomy with concrete before->after fixes, and we release the final 24-question set (three lectures x 8 questions) as JSONL/CSV for Google Forms import (e.g., via Apps Script or API tooling) included as ancillary files under anc/. Finally, we position the work through the AI to Learn (AI2L) rubric lens and argue that self-hosted MCQ generation with explicit QC supports privacy, accountability, and Green AI in educational workflows.
