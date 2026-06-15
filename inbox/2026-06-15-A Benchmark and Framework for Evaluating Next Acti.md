---
interest: medium
link: https://arxiv.org/abs/2606.13802
next_step: skim
priority: low
slack_ts: '1781500239.061259'
source: cs.SE - Software Engineering
status: unread
title: A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets
---
# A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets
> 原文: [https://arxiv.org/abs/2606.13802](https://arxiv.org/abs/2606.13802)

arXiv:2606.13802v1 Announce Type: new
Abstract: Predictive code completion greatly accelerates how quickly developers work. In spreadsheets, despite being much more common, such auto-completion features are virtually non-existent. To address this gap, we introduce a benchmark for systems that observe a sequence of user actions in a spreadsheet and predict future actions. Two challenges are (1) the absence of edit histories in public spreadsheet corpora and (2) the complex space of spreadsheet actions (spatial, temporal, composite). To address (1), we manually curate 52 sequences of 12K actions that recreate spreadsheets from public corpora, seeded by parametrized heuristics and LLM refinement. To address (2), we propose an online evaluation that expects a prediction after each user action, accepts or rejects that prediction, updates the future actions upon acceptance, and repeats this until the target spreadsheet is obtained. We use multiple baseline predictors (including zero-shot LLMs, fine-tuned SLMs, and classical models) and analyze different properties that our benchmark teaches us, including but not limited to: properties of saved actions and false positives, efficiency, effect of user profiles, effect of triggers, and effect of context.
