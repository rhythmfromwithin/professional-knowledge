---
interest: medium
link: https://arxiv.org/abs/2611.03705
next_step: skim
priority: low
slack_ts: '1793859279.675489'
source: cs.SE - Software Engineering
status: unread
title: A Compact Formula-Aware Spreadsheet Abstraction for Large Language Models
---
# A Compact Formula-Aware Spreadsheet Abstraction for Large Language Models
> 原文: [https://arxiv.org/abs/2611.03705](https://arxiv.org/abs/2611.03705)

arXiv:2611.03705v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly used to assist spreadsheet users with tasks such as spreadsheet model construction, formula generation, and data analysis, yet their interaction with real-world spreadsheets remains limited by the mismatch between the structure of spreadsheets and the sequential textual representations typically provided to LLMs. We propose a compact formula-aware spreadsheet abstraction that represents large homogeneous ranges through their positions, types, R1C1 formula patterns, and selected boundary values. An efficient algorithm detects and structures these ranges before a textual serialization is supplied to an LLM. The abstraction is provided to the LLM before detailed spreadsheet content is submitted, improving the accuracy and efficiency of spreadsheet processing while reducing token consumption. We evaluate the method on 50 spreadsheet-query cases. The evaluation shows that the abstraction alone was sufficient to answer some queries. When additional spreadsheet content is required, the abstraction reduces the amount of data that must be submitted to the LLM, thereby reducing token consumption. The abstraction layer also improves the reliability and accuracy of spreadsheet processing. We conclude by discussing further techniques for combining spreadsheet static analysis with artificial intelligence to improve the reliability, accuracy, and efficiency of AI assisted spreadsheet tasks.
