---
interest: medium
link: https://arxiv.org/abs/2609.13274
next_step: skim
priority: low
slack_ts: '1789446771.878709'
source: cs.SE - Software Engineering
status: unread
title: 'Abstention Errors and Segment Support in CUAD: An Auditable Contract-Extraction
  Case Study'
---
# Abstention Errors and Segment Support in CUAD: An Auditable Contract-Extraction Case Study
> 原文: [https://arxiv.org/abs/2609.13274](https://arxiv.org/abs/2609.13274)

arXiv:2609.13274v1 Announce Type: new
Abstract: Contract-clause extraction benchmarks measure reference recovery, but interpreting a system for review assistance also requires measuring unnecessary output and the evidence available within categories. This paper presents a retrospective, reproducible evaluation of a fixed public RoBERTa checkpoint on CUAD's published 102-contract test split. Candidate generation is preserved from an earlier frozen run; matching errors are corrected and category thresholds are reselected on 62 training-split contracts using the original 90% recall target. The corrected operating point recovers 82.2% of reference spans at 8.2% CUAD precision. Of 30,464 returned candidate strings, 19,562 occur on questions with no annotated answer. The system answers 1,335 of 2,938 such questions, a 45.4% false-positive rate (95% contract-bootstrap interval: 43.3-47.9%). Matching candidates constitute 20.3% of returned strings, illustrating why reference-based precision and candidate-level review burden require different denominators. Only nine of 41 categories have at least 30 positive and 30 negative contracts; this count changes to 18 and two under support minima of 20 and 40. Two categories have no negative contracts, making their no-answer false-positive rates undefined. These findings describe one checkpoint, decoder, and threshold policy. Earlier test access and uncertain checkpoint training overlap limit confirmatory interpretation. The paper supplies the original and corrected analyses, predictions, and software checks as ancillary artifacts; it establishes neither a new release criterion nor production readiness.
