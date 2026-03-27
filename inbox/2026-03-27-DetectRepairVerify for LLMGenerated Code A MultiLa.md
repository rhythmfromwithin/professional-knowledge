---
title: "Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.23633
priority: low
status: unread
interest: medium
next_step: skim
---
# Detect--Repair--Verify for LLM-Generated Code: A Multi-Language, Multi-Granularity Empirical Study
> 原文: [https://arxiv.org/abs/2603.23633](https://arxiv.org/abs/2603.23633)

arXiv:2603.23633v1 Announce Type: new
Abstract: Large language models can generate runnable software artifacts, but their security remains difficult to evaluate end to end. This study examines that problem through a Detect--Repair--Verify (DRV) workflow, in which vulnerabilities are detected, repaired, and then rechecked with security and functional tests. It addresses four gaps in current evidence: the lack of test-grounded benchmarks for LLM-generated artifacts, limited evidence on pipeline-level effectiveness, unclear reliability of detection reports as repair guidance, and uncertain repair trustworthiness under verification.
To support this study, EduCollab is constructed as a multi-language, multi-granularity benchmark of runnable LLM-generated web applications in PHP, JavaScript, and Python. Each artifact is paired with executable functional and exploit test suites, and the benchmark spans project-, requirement-, and file-level settings. On this benchmark, the study compares unrepaired baselines, single-pass detect--repair, and bounded iterative DRV under comparable budget constraints. Outcomes are measured by secure-and-correct yield, and intermediate artifacts and iteration traces are analyzed to assess report actionability and repair failure modes.
The results show that bounded iterative DRV can improve secure-and-correct yield over single-pass repair, but the gains are uneven at the project level and become clearer at narrower repair scopes. Detection reports are often useful for downstream repair, but their reliability is inconsistent. Repair trustworthiness also depends strongly on repair scope. These findings highlight the need for test-grounded, end-to-end evaluation of LLM-based vulnerability management workflows.
