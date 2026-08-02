---
interest: medium
link: https://arxiv.org/abs/2607.26066
next_step: skim
priority: high
slack_ts: '1785641746.605239'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Do Methods Support the Claims? Intra-Paper Verification for Peer Review
---
# Do Methods Support the Claims? Intra-Paper Verification for Peer Review
> 原文: [https://arxiv.org/abs/2607.26066](https://arxiv.org/abs/2607.26066)

arXiv:2607.26066v1 Announce Type: new
Abstract: The growing volume of scientific submissions has motivated interest in using large language models (LLMs) to assist peer review. Existing automated novelty assessment approaches typically compare a paper's claimed contributions against prior literature, implicitly assuming that these contributions are accurately realized in the work itself. Human reviewers, however, frequently challenge novelty claims not because similar ideas already exist, but because the methodological evidence presented in the paper does not adequately support them. This internal mismatch between claimed contributions and methodological realization is rarely examined by current LLM-based review systems. To address this gap, we introduce intra-paper claim verification, a framework that evaluates whether novelty claims articulated in a paper are substantiated by the methods used to realize them. The framework employs an LLM to extract novelty claims from the introduction, retrieve claim-relevant methodological evidence, and assess whether the methods substantiate the stated contributions. Assessment is guided by reviewer-inspired evaluation criteria derived inductively from human peer reviews collected from 182 ICLR 2025 papers. These criteria capture recurring reviewer concerns related to novelty, methodology, clarity, and other issues and are used to generate structured reviewer-style assessments of claim substantiation. We evaluate the framework by comparing LLM-generated review comments against human reviewer concerns on a balanced subset of accepted and rejected papers. Human evaluation demonstrates significant alignment between framework-generated assessments and human reviewer concerns, particularly for novelty-related issues. BERTScore further distinguishes corresponding human-LLM review pairs from mismatched controls, indicating that the framework captures concerns consistent with human reviewer observations.
