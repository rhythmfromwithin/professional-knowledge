---
interest: medium
link: https://arxiv.org/abs/2608.07776
next_step: skim
priority: low
slack_ts: '1786588255.308739'
source: cs.CR - Cryptography and Security
status: unread
title: Can AI Write Compliant Code, and to What Extent? Evaluating SOC 2 Compliance
  of Claude Fable 5, Claude Opus 4.8, and Claude Opus 5 Across Four Use Cases
---
# Can AI Write Compliant Code, and to What Extent? Evaluating SOC 2 Compliance of Claude Fable 5, Claude Opus 4.8, and Claude Opus 5 Across Four Use Cases
> 原文: [https://arxiv.org/abs/2608.07776](https://arxiv.org/abs/2608.07776)

arXiv:2608.07776v1 Announce Type: new
Abstract: Software teams now delegate production code to language models, including code that provisions storage, handles credentials, and stores regulated data, so we asked whether a model applies the controls a SOC~2 program expects (encryption, restricted access, logging, retention) when nobody mentions security, and how much one sentence naming the standard changes the answer. We tested three frontier models (Claude Fable~5, Opus~4.8, and Opus~5) across four use cases (an S3 CLI, an authentication service, an RDS Terraform module, and a file-upload handler holding personal data), each generated once from a neutral task statement and once with a single SOC~2 sentence added, scoring all 24 outputs against binary rubrics mapped to specific Trust Services Criteria and hand-verifying every failure and flagged act. Unprompted conformance ran from 47\% to 88\% and tracked whether a control is part of how the code is normally written, so password hashing and \texttt{storage\\_encrypted} appear unasked while S3 hardening calls, retention, and MFA hooks do not. The neutral prompt also shipped real vulnerabilities, including a reachable Werkzeug debugger allowing remote code execution, an unauthenticated download, and an endpoint returning every stored name and email, all scored clean by our first checklist, with a fourth defect passing because its value was computed by a conditional. One SOC~2 sentence moved every case to 86--100\%, worth 23 to 50 points, and removed every insecure construction, though controls outside the model's conception of the task survived it, including MFA hooks, cookie flags, and account lifecycle. Model choice mattered least, with same-generation models within one rubric item across all eight cells, and the pattern-matching scorer proved unreliable, disagreeing with semantic grading on 27 of 216 judgments and passing a real defect, so it needs replacing with semantic checks.
