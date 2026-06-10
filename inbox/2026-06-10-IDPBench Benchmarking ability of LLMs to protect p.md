---
interest: medium
link: https://arxiv.org/abs/2606.09908
next_step: skim
priority: low
slack_ts: '1781065407.231209'
source: cs.CR - Cryptography and Security
status: unread
title: 'IDP-Bench: Benchmarking ability of LLMs to protect personal information in
  interdependent privacy contexts'
---
# IDP-Bench: Benchmarking ability of LLMs to protect personal information in interdependent privacy contexts
> 原文: [https://arxiv.org/abs/2606.09908](https://arxiv.org/abs/2606.09908)

arXiv:2606.09908v1 Announce Type: new
Abstract: Large language models (LLMs) are becoming widely deployed as personal AI assistants with access to sensitive user data, making privacy a major challenge for their design and evaluation. Prior work focuses mainly on individual-level risks, overlooking \textbf{interdependent privacy (IDP)}--where one person's data may be revealed by others without their knowledge or consent. We address this gap by introducing \textbf{IDP-Bench}: the first LLM benchmark for IDP scenarios, grounded in the Contextual Integrity (CI) framework. We evaluate eight open-source LLMs on their understanding of IDP scenarios across three levels of IDP reasoning using two LLM judges. Results show strong co-ownership recognition (6/8 models exceed 90\%) but persistent weaknesses in identifying CI parameters (information attribute, primary subject) and IDP-specific parameters such as secondary subjects, where 7/8 models score below 74\%. Models also struggle to judge sharing appropriateness (5/8 scoring below 77\%). While the ability to judge the appropriateness of sharing improves with scale, performance tends to decline in smaller models, and prompt sensitivity remains high on IDP-specific questions--highlighting the need for more targeted study of IDP in LLM privacy research. Data \& code available \href{https://github.com/tisl-lab/Interdependent\_Privacy\_Bench}{here}.
